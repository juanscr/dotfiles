#!/usr/bin/env bash

killall conky
folder="$HOME"/.config/conky/
if optimus-manager --print-mode | grep "integrated"; then
    folder="$folder"/intel/
fi
num_monitors=$("$HOME"/.config/qtile/check_number_of_monitors.sh)
if [ "$num_monitors" == 2 ]; then
    conky --config="$folder"/conky.conf&
elif xrandr --listactivemonitors | grep "HDMI" ; then
    conky --config="$folder"/conky-one-hdmi.conf
else
    conky --config="$folder"/conky-one.conf &
fi

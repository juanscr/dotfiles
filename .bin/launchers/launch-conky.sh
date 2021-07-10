#!/usr/bin/env bash

killall conky
num_monitors=$("$HOME"/.config/qtile/check_number_of_monitors.sh)
if [ "$num_monitors" == 2 ]; then
    conky &
elif xrandr --listactivemonitors | grep "HDMI" ; then
    conky --config="$HOME"/.config/conky/conky-one-hdmi.conf
else
    conky --config="$HOME"/.config/conky/conky-one.conf &
fi

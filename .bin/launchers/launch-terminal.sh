#!/usr/bin/env bash

script="$HOME"/.config/qtile/check_number_of_monitors.sh
if [ `$script` == 1 ] && xrandr --listactivemonitors | grep "eDP" ; then
    alacritty -o=font.size=9
else
    alacritty
fi

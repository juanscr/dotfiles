#!/usr/bin/env bash

prev_num_monitors=$("$HOME/.config/qtile/check_number_of_monitors.sh")
layout=$(find "$HOME"/.bin/monitor-layouts/ -type f -printf "%f\n"| \
         dmenu -p 'Select Layout:' )
if [ "$layout" != "" ]; then
   "$HOME"/.bin/monitor-layouts/"$layout"
   num_monitors=$("$HOME/.config/qtile/check_number_of_monitors.sh")

   i3-msg restart || qtile cmd-obj -o cmd -f restart
   "$HOME"/.bin/launchers/launch-conky.sh &
   "$HOME"/.bin/bg.sh
fi

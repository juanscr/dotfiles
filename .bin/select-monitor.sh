#!/usr/bin/env bash

prev_num_monitors=$("$HOME/.config/qtile/check_number_of_monitors.sh")
layout=$(find "$HOME"/.bin/monitor-layouts/ -type f -printf "%f\n"| \
         dmenu -p 'Select Layout:' )

"$HOME"/.bin/monitor-layouts/"$layout"
num_monitors=$("$HOME/.config/qtile/check_number_of_monitors.sh")

i3-msg restart || qtile cmd-obj -o cmd -f restart
if [ "$num_monitors" != "$prev_num_monitors" ]; then
   killall conky

   if [ "$num_monitors" == 1 ]; then
      conky --config="$HOME"/.config/conky/conky-one.conf
   else
      conky
   fi
fi

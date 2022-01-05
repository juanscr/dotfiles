#!/usr/bin/env bash

HDMI_NAME=HDMI-0
EDP_NAME=eDP-1-1
if optimus-manager --print-mode | grep "integrated"; then
  HDMI_NAME=HDMI-1-1
  EDP_NAME=eDP-1
fi

prev_num_monitors=$("$HOME/.config/qtile/check_number_of_monitors.sh")
layout=$(find "$HOME"/.bin/monitor-layouts/ -type f -printf "%f\n" | \
         sort | \
         dmenu -p 'Select Layout:' )
if [ "$layout" != "" ]; then
   "$HOME"/.bin/monitor-layouts/"$layout" "$EDP_NAME" "$HDMI_NAME"
   num_monitors=$("$HOME/.config/qtile/check_number_of_monitors.sh")

   i3-msg restart || qtile cmd-obj -o cmd -f restart
   "$HOME"/.bin/launchers/launch-conky.sh &
fi

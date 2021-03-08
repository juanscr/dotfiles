#!/usr/bin/env bash

layout=$(find "$HOME"/.bin/monitor-layouts/ -type f -printf "%f\n"| \
         dmenu -p 'Select Layout:' )

"$HOME"/.bin/monitor-layouts/"$layout"
i3-msg restart

if [ "$layout" = "replicate.sh" ]; then
  sleep 1
  "$HOME"/.config/polybar/launch-bar-one.sh
fi

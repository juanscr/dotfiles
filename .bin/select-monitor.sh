#!/usr/bin/env bash

layout=$(find "$HOME"/.bin/monitor-layouts/ -type f -printf "%f\n"| \
         dmenu -p 'Select Layout:' )

"$HOME"/.bin/monitor-layouts/"$layout"
i3-msg restart

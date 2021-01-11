#!/usr/bin/env bash

layout=$(find "$HOME"/.bin/monitor-layouts/ -type f -printf "%f\n"| dmenu -nf \
         '#F8F8F2' -nb '#282A36' -sb '#6272A4' -sf '#F8F8F2' \
         -fn 'DejaVu Sans-11' -p 'Select Layout:' )

"$HOME"/.bin/monitor-layouts/"$layout"
i3-msg restart

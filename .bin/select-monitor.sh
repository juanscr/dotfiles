#!/usr/bin/env bash

layout=$(find "$HOME"/.bin/monitor-layouts/ | dmenu)
"$HOME"/.bin/monitor-layouts/"$layout"

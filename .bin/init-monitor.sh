#!/usr/bin/env bash

if type "xrandr"; then
    monitors=$(xrandr --query | grep " connected" | cut -d" " -f1)
    numMonitors=$(echo "$monitors" | wc -l)
    if [ "$numMonitors" != 1 ]; then
        "$HOME"/.bin/monitor-layouts/default.sh
    fi
fi

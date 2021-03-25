#!/usr/bin/env bash

# Kill bar
killall -q polybar

# Launch bar in different monitors
monitors=$(xrandr --query | grep " connected" | cut -d" " -f1)
numMonitors=$(echo "$monitors" | wc -l)
if [ "$numMonitors" == 1 ]; then
    polybar --reload jscbar &
else
    for m in $monitors; do
        if [ "$m" == 'HDMI-0' ]; then
            MONITOR=$m polybar --reload jscbar &
        else
            MONITOR=$m polybar --reload monitor2 &
        fi
    done
fi

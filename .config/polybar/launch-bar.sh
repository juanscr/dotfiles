#!/usr/bin/env bash

# Kill bar
killall -q polybar

# Launch bar in different monitors
if type "xrandr"; then
    monitors=$(xrandr --query | grep " connected" | cut -d" " -f1)
    numMonitors=$(echo $monitors | awk '{print NF}' | sort -nu | tail -n 1)
    if [ $numMonitors == 1 ]; then
        polybar --reload jscbar &
    else
        for m in $monitors; do
            if [ $m == 'HDMI-0' ]; then
                MONITOR=$m polybar --reload jscbar &
            else
                MONITOR=$m polybar --reload monitor2 &
            fi
        done
    fi
else
    polybar --reload jscbar &
fi

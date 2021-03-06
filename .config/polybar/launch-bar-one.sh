#!/usr/bin/env bash

# Kill bar
killall -q polybar

# Launch only main bar
if type "xrandr"; then
    polybar --reload jscbar &
else
    polybar --reload jscbar &
fi

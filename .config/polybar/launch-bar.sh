#!/usr/bin/env bash

# Kill bar
killall -q polybar

# Function for checking mirror displays
mirrored="same"
nmirrored="diff"
checkMirrorDisplays () {
    awkInput="(NR > 1) { split(\$3, a, \"+\"); print a[2] \"+\" a[3] }"
    coords=$(xrandr --listactivemonitors | awk "$awkInput")

    # Check if all coordinates are the same
    outputAwk="{ print count == 1 ? \"$mirrored\" : \"$nmirrored\" }"
    echo "$coords" | awk "!unique[\$0]++ { count++ } END $outputAwk"
}

# Launch bar in different monitors
monitors=$(xrandr --query | grep " connected" | cut -d" " -f1)
numMonitors=$(echo "$monitors" | wc -l)
if [ "$numMonitors" == 1 ]; then
    polybar --reload jscbar &
else
    mirror=$(checkMirrorDisplays)
    if [ "$mirror" = "$mirrored" ]; then
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
fi

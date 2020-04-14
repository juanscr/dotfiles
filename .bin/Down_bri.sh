#!/bin/bash

bright=$(cat /sys/class/backlight/intel_backlight/brightness)
max_bright=$(cat /sys/class/backlight/intel_backlight/max_brightness)
step=$(($max_bright / 10 ))
if [ "$bright" -gt 0 ]; then
    bright=$(( $bright - $step))
    echo "$bright" > /sys/class/backlight/intel_backlight/brightness
fi

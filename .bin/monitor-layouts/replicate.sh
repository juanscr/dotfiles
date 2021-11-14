#!/bin/sh
resHDMI=1920x1080
xrandr --output HDMI1 --primary --mode "$resHDMI" --pos 0x0 --rotate normal \
       --output eDP1 --mode 1366x768 --same-as HDMI1 --rotate normal \
       --scale-from "$resHDMI"

#!/bin/sh
xrandr --output $2 --primary --mode 1920x1080 --pos 0x0 --rotate normal \
       --output $1 --off

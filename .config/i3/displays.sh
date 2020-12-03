#!/usr/bin/env bash

if xrandr | grep "HDMI-0 connected"; then
    xrandr --output eDP-1-1 --auto --output HDMI-0 \
           --auto --primary --right-of eDP-1-1
fi

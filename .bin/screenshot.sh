#!/bin/bash

if xrandr | grep "HDMI-0 connected"; then
    flameshot screen -r -c -p "$HOME"/pictures/screenshots
else
    flameshot full -c -p "$HOME"/pictures/screenshots
fi

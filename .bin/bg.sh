#!/bin/bash

photo=$(find "$HOME"/pictures/wallpapers/ -name '*.jpg' | shuf -n 1)

feh --no-fehbg --bg-scale $photo
betterlockscreen -u $photo

#!/bin/bash

photo=$(find $HOME/pictures/wallpapers/*.jpg | shuf -n 1)

feh --no-fehbg --bg-scale $photo
betterlockscreen -u $photo

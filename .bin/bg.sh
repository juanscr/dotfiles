#!/bin/bash

photo=$(find /home/juanscr/pictures/wallpapers/*.jpg | shuf -n 1)

feh --no-fehbg --bg-scale $photo
betterlockscreen -u $photo

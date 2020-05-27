#!/bin/bash

photo=$(find /home/juanscr/Pictures/wallpapers/* | shuf -n 1)

feh --no-fehbg --bg-scale $photo
betterlockscreen -u $photo

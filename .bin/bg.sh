#!/bin/bash

photo=$(find /home/juanscr/Pictures/* | shuf -n 1)

feh --no-fehbg --bg-scale $photo
betterlockscreen -u $photo

#!/usr/bin/sh

# Screen, background and conky
autorandr --change --force &

# Compositor
picom &

# Tray icons
flameshot &
nm-applet &
discord &

# Browser
firefox &

# Terminal
"$HOME"/.bin/launchers/launch-terminal.sh &

# Aesthetics
xrdb "$HOME"/.config/X11/Xresources &

# Notification daemon
dunst &

# File manager
pcmanfm &

# Applet
blueman-applet &

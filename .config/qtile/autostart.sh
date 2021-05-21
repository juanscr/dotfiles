#!/usr/bin/sh

# Background
"$HOME"/.bin/bg.sh &

# Compositor
picom &

# Tray icons
nm-applet &
"$HOME"/.bin/launchers/tray-optimus-manager.sh &
bitwarden &

# Browser
firefox &

# Terminal
alacritty &

# Emacs Daemon
emacs --daemon &

# Aesthetics
xrdb "$HOME"/.config/X11/Xresources &

# Screenshot tool
flameshot &

# Conky
conky &

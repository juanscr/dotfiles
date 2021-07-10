#!/usr/bin/sh

# Nvidia Force full composition
nvidia-force-comp-pipeline

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
"$HOME"/.bin/launchers/launch-terminal.sh &

# Emacs Daemon
emacs --daemon &

# Aesthetics
xrdb "$HOME"/.config/X11/Xresources &

# Screenshot tool
flameshot &

# Conky
"$HOME"/.bin/launchers/launch-conky.sh &

# Polkit
polkit-dumb-agent &

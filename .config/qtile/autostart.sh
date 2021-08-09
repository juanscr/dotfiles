#!/usr/bin/sh

# Nvidia Force full composition
nvidia-force-comp-pipeline

# Background
"$HOME"/.bin/bg.sh &

# Compositor
picom &

# Tray icons
flameshot &
"$HOME"/.bin/launchers/tray-optimus-manager.sh &
nm-applet &

# Browser
firefox &

# Terminal
"$HOME"/.bin/launchers/launch-terminal.sh &

# Emacs Daemon
emacs --daemon &

# Aesthetics
xrdb "$HOME"/.config/X11/Xresources &

# Conky
"$HOME"/.bin/launchers/launch-conky.sh &

# Notification daemon
dunst &

# Polkit
polkit-dumb-agent &

# Launch slack if day of the week
[[ $(date +"%u") < 6 ]] && slack &

#!/usr/bin/sh

# Nvidia Force full composition
if optimus-manager --print-mode | grep "nvidia"; then
    nvidia-force-comp-pipeline
fi

# Background
"$HOME"/.bin/bg.sh &

# Compositor
picom &

# Tray icons
flameshot &
"$HOME"/.bin/launchers/tray-optimus-manager.sh &
nm-applet &

# Browser
brave &

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

# Slack
slack &

# Blueman
blueman-applet &

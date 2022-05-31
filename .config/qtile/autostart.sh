#!/usr/bin/sh

# Background
"$HOME"/.bin/bg.sh &

# Compositor
picom &

# Tray icons
flameshot &
nm-applet &
discord &

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

# File manager
pcmanfm &

# Pomodoro timer
"$HOME"/.bin/launchers/pomotroid.sh &

# Bluetooth applet
blueman-applet &
sleep 1
blueman-tray &

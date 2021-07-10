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
alacritty &

# Emacs Daemon
emacs --daemon &

# Aesthetics
xrdb "$HOME"/.config/X11/Xresources &

# Screenshot tool
flameshot &

# Conky
num_monitors=$("$HOME"/.config/qtile/check_number_of_monitors.sh)
if [ "$num_monitors" == 2 ]; then
    conky &
else
    conky --config="$HOME"/.config/conky/conky-one.conf &
fi

# Polkit
polkit-dumb-agent &

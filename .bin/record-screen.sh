#!/bin/bash

# Record screen with audio of the PC and mic
# Specific for computer audiochannels
ffmpeg \
-f pulse -ac 2 -ar 44100 -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor \
-f pulse -ac 2 -ar 48000 -i alsa_input.pci-0000_00_1f.3.analog-stereo \
-filter_complex amix=inputs=2 \
-async 1 \
-f x11grab -r 24 -s 1920x1080 -i :0.0 \
 -c:v libx264 -preset veryfast -crf 18 \
 -c:a libmp3lame -ar 44100 -q:a 1 "$1"
#!/bin/bash

# Create proxy for a video to a 1080p quality
mkdir proxies
for line in $1; do
    echo Encoding "$line"...
    file=$(basename "$line") && \
    name="${file%.*}" && \
    ffmpeg -loglevel quiet -i "$line" -vf scale=1920:1080 proxies/"$name".mp4 &&
    echo Finished!
done

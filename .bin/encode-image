#!/bin/bash

# Downgrade image to 240p
mkdir lower_res_images
for line in $1; do
    echo Encoding "$line"...
    file=$(basename "$line") && \
    name="${file%.*}" && \
    ffmpeg -loglevel quiet -i "$line" -vf scale=70:-1 lower_res_images/"$name".jpeg &&
    echo Finished!
done

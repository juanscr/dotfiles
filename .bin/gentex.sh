#!/bin/bash

# Creates generic template for given parameter
if [ "$#" -lt 1 ]; then
    echo "A template name is needed to generate one."
    exit 2
elif [ "$#" -gt 1 ]; then
    echo "Only one template at a time is supported."
    exit 2
elif [[ $1 == "slides" ]]; then
    file="slides.tex"
    comms=true
elif [[ $1 == "art" ]]; then
    file="generic.tex"
    comms=true
elif [[ $1 == "artsp" ]]; then
    file="generic-spanish.tex"
    comms=true
elif [[ $1 == "poster" ]]; then
    file="poster.tex"
    comms=true
elif [[ $1 == "exam" ]]; then
    file="exam.tex"
    comms=true
elif [[ $1 == "letter" ]]; then
    file="letter.tex"
    comms=false
else
    echo "Not supported template."
    exit 2
fi


if $comms; then
    cp ~/juanscr/jsc/templates/commands.tex .
fi
cp ~/juanscr/jsc/templates/"$file" .
NAME="$(basename "$PWD")"
mv "$file" "$NAME".tex


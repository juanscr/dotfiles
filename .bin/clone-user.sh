#!/bin/bash

# Clones a git for a list of users with the same name
input=$1
while IFS= read -r line
do
    git clone https://github.com/"$line"/"$2" && mv "$2" "$line"-"$2"
done < "$input"

#!/usr/bin/env bash

# URL extraction with awk
regex="{ match(\$0, \"(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+\", a) }"
url=$(xsel --clipboard --output | awk "$regex END { print a[0] }")

# Check if url
if [ "$url" != "" ]; then
    google-chrome-stable --new-window "$url"
else
    google-chrome-stable
fi

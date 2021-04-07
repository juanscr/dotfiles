#!/usr/bin/env bash

clipboard=$(xsel --clipboard --output)

# Regex for URLS
regex1="[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]"
regex="(https?|ftp|file)://$regex1"

# Check if url
if [[ "$clipboard" =~ $regex ]]; then
    google-chrome-stable --new-window "$clipboard"
else
    google-chrome-stable
fi

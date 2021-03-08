#!/usr/bin/env bash

# Kill bar
killall -q polybar

# Launch only main bar
polybar --reload jscbar &

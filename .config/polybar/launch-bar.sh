#!/usr/bin/env bash

killall -q polybar
# If all your bars have ipc enabled, you can also use
# polybar-msg cmd quit

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar1.log
polybar jscbar >>/tmp/polybar1.log 2>&1 &

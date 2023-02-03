#!/bin/sh

sudo true;
sudo openfortivpn -c /etc/openfortivpn/config &
PID=$!
sleep 5
sudo systemd-resolve --interface ppp0 --set-dns 192.10.5.21
while true; do sleep 60; done;
kill $PID

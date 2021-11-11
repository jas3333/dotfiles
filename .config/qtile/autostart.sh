#!/bin/sh
xset r rate 300 50
wal -R -q
picom --experimental-backend &
bluetoothctl -- power on &
pa-applet &
nm-applet &
flameshot &

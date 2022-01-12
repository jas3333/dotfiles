#!/bin/sh
xset r rate 300 50
#xrandr --output DP-2 --off --output DP-4 --off
xrandr --output HDMI-0 --off --output DP-2 --auto --primary --output DP-4 --mode 2560x1440 --rate 144.00 --right-of DP-2
picom --experimental-backend &
bluetoothctl -- power on &
dunst &
nm-applet &
flameshot &
wal -R

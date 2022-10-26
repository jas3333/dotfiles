#!/bin/sh
xset r rate 300 50
#xrandr --output DP-2 --off --output DP-4 --off
xrandr --output HDMI-A-0 --off --output DisplayPort-0 --auto --primary --output DisplayPort-2 --mode 2560x1440 --rate 144.00 --right-of DisplayPort-0
picom --experimental-backends &
bluetoothctl -- power on &
blueman-applet &
dunst &
nm-applet &
flameshot &
wal -R

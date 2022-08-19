#!/bin/sh
xset r rate 300 50
cp ~/.config/qtile/configs/copy_on_start/settings.ini ~/.config/gtk-3.0/
xrandr --output HDMI-A-0 --auto --output DisplayPort-0 --off --output DisplayPort-2 --off
#xrandr --output HDMI-0 --off 
picom --experimental-backends &
bluetoothctl -- power on &
blueman-applet &
dunst &
nm-applet &
flameshot &
wal -R

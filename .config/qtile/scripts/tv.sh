#! /bin/bash
cp ~/.config/qtile/configs/.Xresources.tv ~/.Xresources
cp ~/.config/qtile/configs/config.chair ~/.config/qtile/config.py
cp ~/.config/qtile/configs/autostart.tv ~/.config/qtile/autostart.sh
xrdb -merge ~/.Xresources
xrandr --output HDMI-0 --auto --output DP-4 --off --output DP-2 --off
qtile cmd-obj -o cmd -f restart

#! /bin/bash
cp ~/.config/qtile/configs/.Xresources.tv ~/.Xresources
cp ~/.config/qtile/configs/config.chair ~/.config/qtile/config.py
cp ~/.config/qtile/configs/autostart.tv ~/.config/qtile/autostart.sh
cp ~/.config/qtile/configs/rofi.tv ~/.config/rofi/config.rasi
xrdb -merge ~/.Xresources
xrandr --output HDMI-A-0 --auto --primary --output DisplayPort-2 --off --output DisplayPort-0 --off
qtile cmd-obj -o cmd -f restart

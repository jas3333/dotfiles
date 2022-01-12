#! /bin/bash
cp ~/.config/qtile/configs/config.desk ~/.config/qtile/config.py
cp ~/.config/qtile/configs/.Xresources.desk ~/.Xresources
cp ~/.config/qtile/configs/autostart.desk ~/.config/qtile/autostart.sh
xrdb -merge ~/.Xresources
xrandr --output HDMI-0 --off --output DP-2 --auto --primary --output DP-4 --mode 2560x1440 --rate 144.00 --right-of DP-2
qtile cmd-obj -o cmd -f restart

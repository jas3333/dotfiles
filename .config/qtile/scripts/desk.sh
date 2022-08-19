#! /bin/bash
cp ~/.config/qtile/configs/config.desk ~/.config/qtile/config.py
cp ~/.config/qtile/configs/.Xresources.desk ~/.Xresources
cp ~/.config/qtile/configs/autostart.desk ~/.config/qtile/autostart.sh
cp ~/.config/qtile/configs/rofi.desk ~/.config/rofi/config.rasi
xrdb -merge ~/.Xresources
xrandr --output HDMI-A-0 --off --output DisplayPort-0 --rate 144.00 --mode 2560x1440 --primary --output DisplayPort-2 --mode 2560x1440 --rate 144.00 --right-of DisplayPort-0 
qtile cmd-obj -o cmd -f restart

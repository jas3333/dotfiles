#!/bin/bash

if pgrep -f "python /home/jas/.config/qtile/scripts/./hotkeys" > /dev/null 
then
    process=$(pgrep -f "python /home/jas/.config/qtile/scripts/./hotkeys")
    kill $process
else
    ~/.config/qtile/scripts/./hotkeys
fi
#! /bin/bash

amixer sget Master | grep 'Right:' | awk -F'[][]' '{print $2}'

#!/bin/sh

# use this thing below to find out values for next line
# cvt 1070 900
xrandr --newmode "1072x900_60.00"   78.75  1072 1136 1240 1408  900 903 913 934 -hsync +vsync
xrandr --addmode LVDS-1 "1072x900_60.00"
xrandr --output LVDS-1 --fb 1072x900 --panning 1072x900 --mode "1072x900_60.00"
xrandr --fb 1070x900 --output LVDS-1 --mode 1600x900


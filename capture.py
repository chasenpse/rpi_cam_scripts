#!/usr/bin/env python

# Import some frameworks
import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# Define image capture size, max WxH is 2048x1536
imgWidth = 2048
imgHeight = 1152

# Get current date/time for creating folders
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDay = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)
initSecs = "%02d" % (d.second)

# Ask user if VF & HF should be applied
flip = None
while flip not in ['y','n']:
    flip = raw_input("Apply VF & HF? (Hint: if cable connection is on bottm = N, top = Y) [y/n]: ").lower()
    if flip in ['y','n']:
        break

# Define file path & part of file name
file = "/home/pi/Pictures/{}{}{}-{}{}{}".format(initYear,initMonth,initDay,initHour,initMins,initSecs)

if flip == 'y':
    os.system("raspistill -w {} -h {} -o {}.jpg -vf -hf -sh 40 -q 60 -awb auto -v -n".format(imgWidth, imgHeight, file))
else:
    os.system("raspistill -w {} -h {} -o {}.jpg -sh 40 -q 60 -awb auto -v -n".format(imgWidth, imgHeight, file))
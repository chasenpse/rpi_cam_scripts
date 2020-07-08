#!/usr/bin/env python3

# Import some frameworks
import os
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
    flip = input("Apply VF & HF? (Hint: if cable connection is on bottm = N, top = Y) [y/n]: ").lower()
    if flip in ['y','n']:
        break

# Define file path & part of file name
file = os.path.expanduser(f"~/Pictures/{initYear}{initMonth}{initDay}-{initHour}{initMins}{initSecs}")

if flip == 'y':
    os.system(f"raspistill -w {imgWidth} -h {imgHeight} -o {file}.jpg -vf -hf -sh 40 -q 60 -awb auto -v -n")
else:
    os.system(f"raspistill -w {imgWidth} -h {imgHeight} -o {file}.jpg -sh 40 -q 60 -awb auto -v -n")
#!/usr/bin/env python3

# Import libraries
import os
from datetime import datetime

# Delay 60 seconds to avoid creating unnecessary files
#time.sleep(60)

# Get current date/time for creating folders
d = datetime.now()
initYear = "%04d" % (d.year)
initMonth = "%02d" % (d.month)
initDay = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)
initSecs = "%02d" % (d.second)

# Define the save dir
savepath = os.path.expanduser(f"~/Pictures/Timelapses/lapse_{initYear}{initMonth}{initDay}-{initHour}{initMins}{initSecs}")
os.mkdir(savepath)

# Define image capture size & frequency
imgWidth = 1280  # Max = 2592
imgHeight = 720  # Max = 1944

while True:
    try:
        captureRate = int(input("Enter capture rate (ms): ")) # in milliseconds, Min ~ 200
        captureTime = int(input("Enter timelapse capture length (min): ")) * 60000 # 1 hour = 3600000, 24 hours = 86400000
    except ValueError:
        print("Please provide a whole integer.")
        continue
    else:
        break

flip = None
while flip not in ['y','n']:
    flip = input("Apply VF & HF? (Hint: if cable connection is on bottm = N, top = Y) [y/n]: ").lower()
    if flip in ['y','n']:
        break

if flip == 'y':
    os.system(f"raspistill -t {captureTime} -tl {captureRate} -w {imgWidth} -h {imgHeight} -o {savepath}/%06d.jpg -vf -hf -sh 40 -q 60 -awb auto -v -n")
else:
    os.system(f"raspistill -t {captureTime} -tl {captureRate} -w {imgWidth} -h {imgHeight} -o {savepath}/%06d.jpg -sh 40 -q 60 -awb auto -v -n")
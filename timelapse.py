#!/usr/bin/env python

# Import some frameworks
import os
import time
import RPi.GPIO as GPIO
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

# Define the save directory
# If apache is running you can set this to /var/www/ to make
# them accessible via web browser.
folderToSave = "/var/www/html/timelapses/lapse_" + str(initYear) + str(initMonth) + str(initDay) + "-" + str(initHour) + str(initMins) + str(initSecs)
os.mkdir(folderToSave)

# Define image capture size & frequency
imgWidth = 1280  # Max = 2592
imgHeight = 720  # Max = 1944
imgRate = 6000   # in milliseconds, Min ~ 200

#86400000 = 24 hours / 6 zeros
#3600000 = 1 hour / 5 zeros
os.system("raspistill -t 28800000 -tl " + str(imgRate) + " -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/" + str("%06d") + ".jpg -vf -hf  -sh 40 -awb auto -mm average -v -n")

#!/usr/bin/env python

# Import some frameworks
import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# Define the save directory
# If apache is running you can set this to /var/www/ to make
# them accessible via web browser.
folderToSave = "/var/www/html/pics"

# Define image capture size & frequency
imgWidth = 2048
imgHeight = 1536

# Get current date/time for creating folders
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDay = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)
initSecs = "%02d" % (d.second)

os.system("raspistill -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/img_" + str(initYear) + str(initMonth) + str(initDay) + "-" + str(initHour) + str(initMins) + str(initSecs) + ".jpg -vf -hf  -sh 40 -awb auto -mm average -v -n")

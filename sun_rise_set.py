#!/usr/bin/env python3

# Import libraries
import os
import requests
import pytz
import datetime

# API call for sun rise/set times
response = requests.get("https://api.sunrise-sunset.org/json?lat=41.0017643&lng=-73.6656834&date=today&formatted=0")
data = response.json()

# Set format to match API response formatting
# ex: 2020-07-08T09:31:12+00:00
format = "%Y-%m-%dT%H:%M:%S%z"

# create datetime objects from JSON strings and use astimezone for US/Eastern times
sunrise = datetime.datetime.strptime(data["results"]["sunrise"],format).astimezone(pytz.timezone('US/Eastern'))
civil_twilight_begin = datetime.datetime.strptime(data["results"]["civil_twilight_begin"],format).astimezone(pytz.timezone('US/Eastern'))
civil_twilight_end = datetime.datetime.strptime(data["results"]["civil_twilight_end"],format).astimezone(pytz.timezone('US/Eastern'))
nautical_twilight_begin = datetime.datetime.strptime(data["results"]["nautical_twilight_begin"],format).astimezone(pytz.timezone('US/Eastern'))
nautical_twilight_end = datetime.datetime.strptime(data["results"]["nautical_twilight_end"],format).astimezone(pytz.timezone('US/Eastern'))

# calculate timedelta for total timelapse runtime
runTimeOffset = (civil_twilight_begin - nautical_twilight_begin) / 2

# Get current date/time for creating folders
d = datetime.datetime.now()
initYear = "%04d" % (d.year)
initMonth = "%02d" % (d.month)
initDay = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)
initSecs = "%02d" % (d.second)

# Define the save dir
savepath = f"/home/pi/Pictures/Timelapses/lapse_{initYear}{initMonth}{initDay}-{initHour}{initMins}{initSecs}"

os.mkdir(savepath)

os.system(f"raspistill -t 10000 -tl 2000 -w 1280 -h 720 -o {savepath}/%06d.jpg -vf -hf -sh 40 -q 60 -v -n -awb sun")
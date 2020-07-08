#!/usr/bin/env python3

# Import libraries
import os
import requests
import pytz
import datetime
import time
import json

lastModDate = ''
lat = 41.0017643
lng = -73.6656834

# Check if info.json exists, sets lastModDate
if os.path.exists(os.path.expanduser('~/Pictures/Timelapses/info.json')):
    lastModDate = os.stat(os.path.expanduser('~/Pictures/Timelapses/info.json')).st_mtime
    lastModDate = time.strftime('%Y-%m-%d', time.localtime(lastModDate))

# If lastModDate is before today's date OR if the file doesn't exist (first time running, passes blank str), fetch data from API
if lastModDate < str(datetime.datetime.now().date()):
    # API call for sun rise/set times
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date=today&formatted=0")
    data = response.json()
    # Save response
    with open(os.path.expanduser("~/Pictures/Timelapses/info.json"),mode='w') as f:
        json.dump(data,f)
        f.close()

# Open and parse JSON into dict object
with open(os.path.expanduser("~/Pictures/Timelapses/info.json"),mode='r') as f:
    data = json.load(f)
    f.close()

# Set format to match API response formatting
# ex: 2020-07-08T09:31:12+00:00
format = "%Y-%m-%dT%H:%M:%S%z"

# Set timezone object
tzone = pytz.timezone('US/Eastern')

# create datetime objects from JSON strings and use astimezone for US/Eastern times
timenow = tzone.localize(datetime.datetime.now())
sunrise = datetime.datetime.strptime(data["results"]["sunrise"],format).astimezone(tzone)
sunset = datetime.datetime.strptime(data["results"]["sunset"],format).astimezone(tzone)
civil_twilight_begin = datetime.datetime.strptime(data["results"]["civil_twilight_begin"],format).astimezone(tzone)
civil_twilight_end = datetime.datetime.strptime(data["results"]["civil_twilight_end"],format).astimezone(tzone)
nautical_twilight_begin = datetime.datetime.strptime(data["results"]["nautical_twilight_begin"],format).astimezone(tzone)
nautical_twilight_end = datetime.datetime.strptime(data["results"]["nautical_twilight_end"],format).astimezone(tzone)

# calculate timedelta for total timelapse runtime for sunrise and sunset
sr_startTimeOffset = (civil_twilight_begin - nautical_twilight_begin) / 2
sr_startTime = civil_twilight_begin - sr_startTimeOffset
sr_timelapse_runtime = (sunrise - sr_startTime) * 2

ss_startTimeOffset = (nautical_twilight_end - civil_twilight_end) / 2
ss_timelapse_runtime = ((civil_twilight_end + ss_startTimeOffset) - sunset) * 2
ss_startTime = sunset - (ss_timelapse_runtime / 2)

while True:
    if (timenow == sr_startTime):
        # Get current date/time for creating folders
        d = datetime.datetime.now()
        initYear = "%04d" % (d.year)
        initMonth = "%02d" % (d.month)
        initDay = "%02d" % (d.day)
        initHour = "%02d" % (d.hour)
        initMins = "%02d" % (d.minute)
        initSecs = "%02d" % (d.second)

        # Define the save dir & make path
        savepath = os.path.expanduser(f"~/Pictures/Timelapses/lapse_{initYear}{initMonth}{initDay}-{initHour}{initMins}{initSecs}")
        os.mkdir(savepath)

        # Run raspistill
        os.system(f"raspistill -t {sr_timelapse_runtime.seconds} -tl 2000 -w 1280 -h 720 -o {savepath}/%06d.jpg -vf -hf -sh 40 -q 60 -v -n -awb sun")
    elif (timenow == ss_startTime):
        # Get current date/time for creating folders
        d = datetime.datetime.now()
        initYear = "%04d" % (d.year)
        initMonth = "%02d" % (d.month)
        initDay = "%02d" % (d.day)
        initHour = "%02d" % (d.hour)
        initMins = "%02d" % (d.minute)
        initSecs = "%02d" % (d.second)

        # Define the save dir & make path
        savepath = os.path.expanduser(f"~/Pictures/Timelapses/lapse_{initYear}{initMonth}{initDay}-{initHour}{initMins}{initSecs}")
        os.mkdir(savepath)

        # Run raspistill
        os.system(f"raspistill -t {ss_timelapse_runtime.seconds} -tl 2000 -w 1280 -h 720 -o {savepath}/%06d.jpg -vf -hf -sh 40 -q 60 -v -n -awb sun")
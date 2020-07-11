#!/usr/bin/env python3

# Import libraries
import os
import requests
import pytz
import datetime
import time

lastCallDate = ''
lat = 41.0017643
lng = -73.6656834

# Set format to match API response formatting
# ex: 2020-07-08T09:31:12+00:00
format = "%Y-%m-%dT%H:%M:%S%z"

# Set timezone object
tzone = pytz.timezone('US/Eastern')

# Start date watch while loop
while True:

    # If this returns true it's either the next day or evaluated against the initial value, ''
    if lastCallDate < str(datetime.datetime.now().date()):
        
        # Update to today's date
        lastCallDate = str(datetime.datetime.now().date())

        # Make request call for sun rise/set times and store response
        response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date=today&formatted=0")
        data = response.json()

        # Create localized aware datetime objects from JSON responses
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

    # Start time of day while loop
    while True:

        timenow = tzone.localize(datetime.datetime.now())
        
        if timenow.strftime("%H:%M:%S") == sr_startTime.strftime("%H:%M:%S"):

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
            os.system(f"raspistill -t {sr_timelapse_runtime.seconds * 1000} -tl 2000 -w 1280 -h 720 -o {savepath}/%06d.jpg -vf -hf -sh 40 -q 60 -v -n -awb sun")
            break

        elif timenow.strftime("%H:%M:%S") == ss_startTime.strftime("%H:%M:%S"):
            
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
            os.system(f"raspistill -t {ss_timelapse_runtime.seconds * 1000} -tl 2000 -w 1280 -h 720 -o {savepath}/%06d.jpg -vf -hf -sh 40 -q 60 -v -n -awb sun")
            break
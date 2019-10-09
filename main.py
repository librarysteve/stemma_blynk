#!/usr/bin/env python3

## Local Server Instructions ##
'''
If you're using a local server you can find the
Auth Token in the server management interface.
By default the web interface runs on port 9443

Initializing an an instance of blynk depends on
if you're using a local or managed server.
For a local server uncomment the line below and
remove the second initialization definition.
By default the blynk service runs on port 8080.

To use the app with a local server instance,
Open the app, hit the log in button, then click
on the three dot icon just above the "Next" button
This will allow you to select between using the
default(managed/paid) server and the free local one

The default username:admin@blynk.cc
The default password:admin
'''
import busio
import blynklib
import blynktimer
from time import sleep
from board import SCL, SDA
from adafruit_seesaw.seesaw import Seesaw

global INTERVAL
# Interval between samples
INTERVAL = 3


AUTH = 'AUTH_TOKEN_HERE' # Can be found in the app


## Initialize a blynk instance ##
# blynk = blynklib.Blynk(AUTH, server='<SERVER IP HERE>', port='<SERVER PORT HERE')
blynk = blynklib.Blynk(AUTH) # Remove this line if you run your own server.


## Define the sensor and protocol ##
bus = busio.I2C(SCL, SDA)
ss = Seesaw(bus, addr=0x36)
timer = blynktimer.Timer()

# Function to read the temp data and write it to blynk
def read_temp(vpin_num=0):
    c_temp = ss.get_temp()              # Define temp in celsius
    l_temp = (c_temp * 1.8) + 32        # Convert to fahrenheit, it's celsius by default
    temp = round(l_temp, 2)             # Round to 2 decemal places
    print("Temp: {} Degrees F".format(temp))      # Output message format
    blynk.virtual_write(vpin_num, temp) # Send the data to blynk server

# Function to read moisture data and write it to blynk
def read_moisture(vpin_num=1):
    moisture = ss.moisture_read()           # Define moisture
    print("Moisture: {} out of 2000".format(moisture))  # Output message format, moisture range 0-2000
    blynk.virtual_write(vpin_num, moisture) # Send data to blynk server


@timer.register(vpin_num=2, interval=INTERVAL, run_once=False) # Interval sets the time between sample readings
def main(vpin_num=2):                                   # The timer will run this function every three seconds
    read_moisture() # Run the the functions from above
    read_temp()

while True:
    blynk.run() # Run the blynk service
    timer.run() # Use the timer to set sample intervals

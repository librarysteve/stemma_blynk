import busio
import blynklib
import blynktimer
from time import sleep
from board import SCL, SDA
from adafruit_seesaw.seesaw import Seesaw

AUTH = '<INSERT API KEY HERE>'

# If you're using a local server or one that you
# run elsewhere, uncomment the first option.

#blynk = blynklib.Blynk(AUTH, server='<SERVER IP HERE>', port='8080') # Port 8080 is the default
                                                                      # use which ever port matched your configuration
# Remove this line if you run your own server. 
blynk = blynklib.Blynk(AUTH)


bus = busio.I2C(SCL, SDA)
ss = Seesaw(bus, addr=0x36)
timer = blynktimer.Timer()

# Function to read the temp data and write it to blynk
def read_temp(vpin_num=0):
    c_temp = ss.get_temp() # Read temp data, in celcious by default
    l_temp = (c_temp * 1.8) + 32 # Convert to fahrenheit
    temp = round(l_temp, 2) # Round to 2 decemal places
    print("Temp {}".format(temp)) # print to terminal on the device attached to the stemma
    blynk.virtual_write(vpin_num, temp) # send the data to blynk server/app

# Function to read moisture data and write it to blynk
def read_moisture(vpin_num=1):
    moisture = ss.moisture_read()
    print("Moisture: {}".format(moisture))
    blynk.virtual_write(vpin_num, moisture)

@timer.register(vpin_num=2, interval=3, run_once=False) # Timer sets the interval between each data read.
def main(vpin_num=2):                                   # This is set to 3 seconds!
    read_moisture()
    read_temp()

while True:
    blynk.run()
    timer.run()

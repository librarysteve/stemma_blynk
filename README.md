# stemma_blynk
Reading data from the Adafruit STEMMA with Blynk on the Raspbery Pi

This script is intended for use with the Adafruit Stemma I2C Soil moisture and temperature sensor and the Blynk IoT server/app for Android and iOS. It uses Adafruit's Circuitpython project and the blynk library

 
[Adafruit](https://www.adafruit.com/)


[Blynk](https://blynk.io/)

### How To Use:

### 0) Before you start!
Asside from the python modules - you also need to enable i2c.
Run:
```sh
sudo raspi-config
```
And select "Interfacing Options > I2C > YES"

You need python3 and some debugging tools will be useful
Run:
```sh
sudo apt install python3 python3-pip i2c-tools -y
```
*You should reboot before moving on*


### 1) Wire your stemma accroding to [Adafruit's guide](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test#step-3016121). 
Use the following command to check your wiring:
```sh
i2cdetect -y 1
```
You should see the following output:
```sh
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- 36 -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
If you don't see the 36(the default i2c address), check your wiring!

### 2) On your Raspberry pi this repo with the following command:
```sh
git clone https://github.com/librarysteve/stemma_blynk
```

### 3) Install the required packages with pip
```sh 
pip install -r requirements.txt
```
### 4) Add your Blynk authorization token to main.py
After logging in and creating a project, the authorizatiuon token 
can be found under the project settings (the bolt icon in the top right).
Touch the "Email" button to email it to yourself. (Copy and paste for accuracy!)

### 5) Add widgets to your project and configure
The Following widget configurations are most effective:
  a. Two Value Displays
  b. Two Labeled Value Displays
  c. The SuperChart widget
  
Configureation for Value Displauy(with or without a label) is the same.

#### Value Display/Labeled Value Display:
  
  a. Add two widgets to the workspace
  
  b. To enter the settings menu, touch the widget while the app isn't running
  
  c. Under the "pin" option, select "virtual" : "V0" - This will be our Temp sensor
      you will also need to adjust the input range. This script converts the data to 
      fahrenheit(so 0-120 is a good range)
  
  d. Do the same for the second display, this time setting it to "V1"
     set the range to 0-2000
(If you choose the labeled display simply edit the label section accordingly)

#### For SuperChart:
  
  a. Add the SuperChart widget
  b. Enter the settings menu
  c. By default there is one data stream. Name it "Temperature"
  d. Click the icon next to the title of the data stream to bring up the settings
  e. Set the Temp pin to "Virtual:V0" with and the moisture pin to "Virtual:V1"
  (You'll have to adjust the scaling settings accordingly!)
  
### 6) Start it up!
Run the script on the pi with:
```sh
python3 ./main.py
```

If you see ascii art and data readings, then hit the play button in the top right corner of the app. 

You should start to see your data!

#### If you see ascii art and no data:
1) check your auth token/check for the "blynklib.BlynkError: Invalid Auth Token" error message on killing the script!
2) check your pin/virtual pin settings
3) make sure your phone/tablet is connected to the internets!


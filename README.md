# stemma_blynk
reading data from the Adafruit STEMMA with Blynk

This script is intended for use with the Adafruit Stemma I2C Soil moisture and temporature sensor and the Blynk IoT server/app for Android and iOS. It uses Adafruit's Circuitpython project and the blynk library

### How To Use:
### #0) Use python3

#### 1) Wire your stemma accroding to [Adafruit's guide](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test#step-3016121). 

#### 2) Clone this repo with the following command:
```sh
git clone https://github.com/librarysteve/stemma_blynk
```

#### 3) Install the required packages with pip
```sh 
pip install -r requirements.txt
```

#### 4) Add your Blynk authorization token to main.py

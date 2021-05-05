# import all libraries needed
import sys
sys.path.append('../')
import RPi.GPIO as GPIO
import rgb1602
import time

lcd = rgb1602.RGB1602(16,2)
GPIO.setmode(GPIO.BCM)

import os
import glob
import time

# Define keys
lcd_key     = 0
key_in  = 0

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)

# Read the key value
def read_LCD_buttons():
  key_in17 = GPIO.input(17)
  key_in18 = GPIO.input(18)

#these tow lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_path = glob.glob(base_dir + '28*')[0] #get file path of sensor
rom = device_path.split('/')[-1] #get rom name

def read_temp_raw():
    with open(device_path +'/w1_slave','r') as f:
        valid, temp = f.readlines()
    return valid, temp
 
def read_temp():
    valid, temp = read_temp_raw()

    while 'YES' not in valid:
        time.sleep(0.2)
        valid, temp = read_temp_raw()

    pos = temp.index('t=')
    if pos != -1:
        #read the temperature .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        temp_string = temp[pos+2:]
        temp_c = float(temp_string)/1000.0 
        temp_f = temp_c * (9.0 / 5.0) + 32.0
        return temp_c, temp_f
    
    
    if temp_c < 30:
        lcd.setCursor(0,0)
        lcd.printout("TOO HOT!")
        time.sleep(0.1) 
            
 
print(' ROM: '+ rom)

while True:
    c, f = read_temp()
    print('C={:,.3f} F={:,.3f}'.format(c, f))
    7
    # Setup LCD display
    lcd.setCursor(0,0)
    lcd.printout("current temp:")
    lcd.setCursor(0,1)
    lcd.printout('{:,.3f} C'.format(c, f))
    time.sleep(0.1) 

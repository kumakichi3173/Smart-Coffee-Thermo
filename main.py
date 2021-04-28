# import all libraries needed
import sys
sys.path.append('../')
import RPi.GPIO as GPIO
import rgb1602
import time

lcd = rgb1602.RGB1602(16,2)
GPIO.setmode(GPIO.BCM)

# Define keys
lcd_key     = 0
key_in  = 0

btnUP     = 0
btnDOWN   = 1

count = 0

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)

# Read the key value
def read_LCD_buttons():
  key_in17 = GPIO.input(17)
  key_in18 = GPIO.input(18)

  if (key_in17 == 1):
    return btnUP
  if (key_in18 == 1):
    return btnDOWN

# Setup LCD display
lcd.setCursor(0,0)
lcd.printout("Up =+1 Down =-1")

lcd.setCursor(0,1)
lcd.printout(count)

# Loop to read in button presses and update LCD
while True:
  lcd.setCursor(0,1)
  lcd_key = read_LCD_buttons()  #  Reading keys

  time.sleep(0.2)
  
  if (lcd_key == btnUP):
    count = count + 1
    lcd.setCursor(0,1)
    lcd.printout("          ")
    lcd.setCursor(0,1)
    lcd.printout(count)
  if (lcd_key == btnDOWN):
    count = count - 1
    lcd.setCursor(0,1)
    lcd.printout("          ")
    lcd.setCursor(0,1)
    lcd.printout(count)
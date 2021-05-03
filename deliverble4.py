import time 
import board
from adafruit_motorkit import Motorkit 
from adafruit_motor import stepper


motor = Motorkit(i2c=board.I2C(),address=0x61)

while True: 
    for i in range(100): 
        motor.stepper1.onestep(direction=stepper.FORWARD) 
        time.sleep(0.01) 
    for i in range(100): 
        motor.stepper1.onestep(direction=stepper.BACKWARD) 
        time.sleep(0.01)
    for i in range(100): 
        motor.stepper2.onestep(direction=stepper.FORWARD) 
        time.sleep(0.01) 
    for i in range(100): 
        motor.stepper2.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)



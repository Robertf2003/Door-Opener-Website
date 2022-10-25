import RPi.GPIO as GPIO
import RPIO
import time
outputPin = 14
RPIO.setup(outputPin, RPIO.OUTPUT, initial=RPIO.LOW)
def openDoor():
    RPIO.output(outputPin, True)

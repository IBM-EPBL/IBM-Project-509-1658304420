import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
while True:
 GPIO.output(8, GPIO.HIGH)
 print("Red light On : Stop")
 sleep(7)
 GPIO.output(8, GPIO.LOW)
 print("Red Light Off : Wait")
 GPIO.output(9, GPIO.HIGH)
 print("Yellow light On : Wait")
 sleep(2)
 GPIO.output(9, GPIO.LOW)
 print("Yellow Light Off : Start")
 GPIO.output(10, GPIO.HIGH)
 print("Green light On : Start")
 sleep(10)
 GPIO.output(10, GPIO.LOW)
 print("Green Light Off : Wait")
 GPIO.output(9, GPIO.HIGH)
 print("Yellow light On : Wait")
 sleep(2)
 GPIO.output(9, GPIO.LOW)
 print("Yellow Light Off : Stop")
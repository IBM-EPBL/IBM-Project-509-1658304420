#Python Code for Traffic Light in Raspberry Pi

from gpiozero import Button,TrafficLights
from time import sleep
button=Button(21)
lights=TrafficLights(25,8,7)
while True:
    button.wait_for_press()
    lights.red.on()
    sleep(90)
    lights.amber.on()
    sleep(10)
    lights.green.on()
    sleep(45)
    lights.red.on()
    lights.amber.on()
    sleep(10)
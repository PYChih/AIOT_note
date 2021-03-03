from gpiozero import PWMLED
from time import sleep

led = PWMLED(4)

while True:
    led.value = 0
    sleep(1)
    led.value = 0.1
    sleep(1)
    led.value = 0.3
    sleep(1)
    led.value = 0.5
    sleep(1)
    led.value = 0.7
    sleep(1)
    led.value = 1
    sleep(1)
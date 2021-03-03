import RPi.GPIO as gpio
import time
 
gpio.setmode(gpio.BOARD)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(11, gpio.OUT)
 
def action(channel):
    print("Motion detected")
    for i in range(10):
        gpio.output(11, True)
        time.sleep(0.2)
        gpio.output(11, False)
        time.sleep(0.2)
 
try:
    gpio.add_event_detect(26, gpio.RISING, callback=action, bouncetime=200)
    while True:
        time.sleep(1)
except:
    gpio.cleanup()
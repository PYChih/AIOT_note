import RPi.GPIO as GPIO
from time import sleep
relay_pin = 4
# BOARD與BCM: BOARD依照針腳編號，BCM依照ex: GPIO4編號
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setwarnings(False)


try:
    while True:
        GPIO.output(relay_pin, 0)
        sleep(1)
        GPIO.output(relay_pin, 1)
        sleep(1)
except KeyboardInterrupt:
    print("STOP")
except:
    print("Other error or exception occurred!")
finally:
    GPIO.cleanup()

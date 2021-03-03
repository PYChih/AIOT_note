from gpiozero import PWMLED
from gpiozero import Button
from signal import pause
led = PWMLED(4)
button = Button(2)

def set30p():
    led.value = 0.3
def set100p():
    led.value = 1

button.when_pressed = set30p
button.when_released = set100p
pause()
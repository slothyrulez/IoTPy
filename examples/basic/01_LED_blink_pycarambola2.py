from time import sleep
from IoTPy.core.gpio import GPIO
from IoTPy.pycarambola2.carambola2 import Carambola2

# This is platform dependent - please configure to your application
LED_PIN_ID = 1

with Carambola2() as board, board.GPIO(LED_PIN_ID) as gpio_pin:

    gpio_pin.setup(GPIO.OUTPUT)  # set GPIO pin to be output

    while True:
        gpio_pin.write(0)  # Turn led ON
        sleep(0.1)
        gpio_pin.write(1)  # Turn led OFF
        sleep(0.1)

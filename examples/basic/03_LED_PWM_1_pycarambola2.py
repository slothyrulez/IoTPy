from time import sleep
from IoTPy.pyuper.uper import UPER1
from IoTPy.pycarambola2.carambola2 import Carambola2

"""
DEVICE: Carambola2

"""

with Carambola2() as board, board.PWM(27) as redPin:

    redPin.set_frequency(1000)

    while True:
        for i in xrange(0, 100):
            redPin.set_duty_cycle(i)
            sleep(0.01)
        for i in reversed(xrange(0, 100)):
            redPin.set_duty_cycle(i)
            sleep(0.01)
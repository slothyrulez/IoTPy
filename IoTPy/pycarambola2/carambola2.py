#! -*- coding: utf-8 -*-

from IoTPy.pycarambola2.ioboard import Carambola2IoBoard
from IoTPy.pycarambola2.pinouts import CARAMBOLA2_DEVBOARD_PINOUT

class Carambola2(Carambola2IoBoard):
    """
    Overridable carambola2 board class
    """
    def __init__(self, pinout=None):
        super(Carambola2, self).__init__(CARAMBOLA2_DEVBOARD_PINOUT)

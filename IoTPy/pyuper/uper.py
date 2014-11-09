#! -*- coding: utf-8 -*-

from IoTPy.pyuper.ioboard import UpperIoBoard
from IoTPy.pyuper.pinouts import UPER1_PINOUT


class UPER1(UpperIoBoard):

    def __init__(self, serial_port=None):
        super(UPER1, self).__init__(UPER1_PINOUT, serial_port)

from IoTPy.pyuper.ioboard import UpperIoBoard
from IoTPy.pyuper.pinouts import WEIO_PINOUT


class WeIO(UpperIoBoard):

    def __init__(self, serial_port=None):
        super(WeIO, self).__init__(WEIO_PINOUT, serial_port)

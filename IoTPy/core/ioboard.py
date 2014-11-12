#! -*- coding: utf-8 -*-


class IoBoard(object):

    """
    This is a template class for IoTPy boards with GPIO functionality. Each such module should implement
    :class:`GPIO` functions according to their description.
    Usually GPIO modules will be a part of a device or board. In these cases the device (or board) should
    implement :class:`GPIOProducer` class and :func:`IoTPy.core.gpio.GPIOProducer.GPIO` method be called
    to retrieve an underlying GPIO module.

    """

    """
    Base template for boards

    :param pinout: A list describing physical board pin layout and capabilities.
    :type pinout: :class:`IoTPy.core.pinouts.IoPinout`
    """

    def __init__(self, pinout):
        """
        Initialize ioboard
        """
        self.pinout = pinout
        raise NotImplementedError()

    def get_info(self):
        """
        Get information
        """
        raise NotImplementedError()

    def stop(self):
        """
        Stop all communications with the board
        """
        raise NotImplementedError()

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError()

from IoTPy.core.utils import IoTPy_APIError

CAP_RESERVED = 0x0
CAP_GPIO     = 0x1
CAP_ADC      = 0x2
CAP_PWM      = 0x4
CAP_SPI      = 0x8

class IoParams:
    """
    Class describing IO pin.

    :param int capabilities: Integer describing pin capabilities. Can be a combination of CAP_CAP_RESERVED, CAP_GPIO, CAP_ADC, CAP_PWM and CAP_SPI.
    :param int pinID: Pin ID.
    :param str name: Pin alias name.
    :param list extra: Extra data for pin capabilities.
    """

    def __init__(self, capabilities, pinID, name, extra=None):
        self.capabilities = capabilities
        self.pinID = pinID
        self.pinName = name
        self.extra = extra

class IoPinout(dict):
    """
    A dictionary consisting of integer keys and :class:`IoParams` values which describe board pin mapping and capabilities.
    """

    def __init__(self, *args, **kw):
        super(IoPinout,self).__init__(*args, **kw)
        for key in self:
            if not isinstance(key, int) or not isinstance(self[key], IoParams):
                raise IoTPy_APIError("IoPinout must consist of integer keys and IoParams values.")

    def __delitem__(self, key):
        raise IoTPy_APIError("IoPinout can not be modified.")

    def __setitem__(self, key, value):
        raise IoTPy_APIError("IoPinout can not be modified.")

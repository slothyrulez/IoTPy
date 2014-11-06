from IoTPy.core.utils import IoTPy_APIError
from IoTPy.core.pinouts import CAP_RESERVED, CAP_GPIO, CAP_ADC, CAP_PWM, CAP_SPI
from IoTPy.core.pinouts import IoParams, IoPinout

J12 = {
    1:  {"gpio": 17, "alt": ["LED6"]},
    2:  {"gpio": 16, "alt": ["LED5"]},
    3:  {"gpio": 15, "alt": ["LED4"]},
    4:  {"gpio": 14, "alt": ["LED3"]},
    5:  {"gpio": 13, "alt": ["LED2"]},
    6:  {"gpio": 1, "alt": ["LED1"]},
    7:  {"gpio": 0, "alt": ["LED0"]},
    8:  {"gpio": 11, "alt": ["LED5"]},
    9:  {"gpio": 12, "alt": ["LED5"]},
    10: {"gpio": 18, "alt": ["I2S"]},
    11: {"gpio": 19, "alt": ["I2S"]},
    12: {"gpio": 20, "alt": ["I2S"]},
    13: {"gpio": 21, "alt": ["I2S"]},
    14: {"gpio": 22, "alt": ["I2S"]},
    15: {"gpio": 23, "alt": ["SPDIF"]},
    16: {"gpio": None, "alt": ["3.3VD"]},
    17: {"gpio": None, "alt": ["3.3VD"]},
    18: {"gpio": None, "alt": ["5VD"]},
    19: {"gpio": None, "alt": ["5VD"]},
    20: {"gpio": None, "alt": ["GND"]},
}
J13 = {
    1:  {"gpio": 9, "alt": ["UART TX"]},
    2:  {"gpio": 10, "alt": ["UART RX"]},
    3:  {"gpio": "??", "alt": ["UART TX C"]},
    4:  {"gpio": "??", "alt": ["UART TX C"]},
    5:  {"gpio": None, "alt": ["GND"]},
    6:  {"gpio": None, "alt": ["USB+"]},
    7:  {"gpio": None, "alt": ["USB-"]},
    8:  {"gpio": None, "alt": ["USB+ C"]},
    9:  {"gpio": None, "alt": ["USB- C"]},
    10: {"gpio": None, "alt": ["GND"]},
    11: {"gpio": 2, "alt": ["SPI CS"]},
    12: {"gpio": 3, "alt": ["SPI CLK"]},
    13: {"gpio": 4, "alt": ["SPI MOSI"]},
    14: {"gpio": 5, "alt": ["SPI MISO"]},
    15: {"gpio": None, "alt": ["RESET"]},
    16: {"gpio": None, "alt": ["3.3VD"]},
    17: {"gpio": None, "alt": ["3.3VD"]},
    18: {"gpio": None, "alt": ["5VD"]},
    19: {"gpio": None, "alt": ["5VD"]},
    20: {"gpio": None, "alt": ["GND"]},
}

CARAMBOLA2_DEVBOARD_GPIO_PINS = {0: {num: val["gpio"] for num, val in J12.items()},
                                 1: {num: val["gpio"] for num, val in J13.items()}}
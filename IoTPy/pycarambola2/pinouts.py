from IoTPy.core.utils import IoTPy_APIError
from IoTPy.core.pinouts import (CAP_RESERVED, CAP_GPIO, CAP_ADC,
                                CAP_PWM, CAP_SPI)
from IoTPy.core.pinouts import IoParams, IoPinout

"""
Carambola2 development board pin description
:link 8devices:
:link openwrt:
"""

CARAMBOLA2_DEVBOARD_PINOUT = IoPinout({
    1: IoParams(CAP_GPIO,       17,     "J12_1"),
    2: IoParams(CAP_GPIO,       16,     "J12_2"),
    3: IoParams(CAP_GPIO,       15,     "J12_3"),
    4: IoParams(CAP_GPIO,       14,     "J12_4"),
    5: IoParams(CAP_GPIO,       13,     "J12_5"),
    6: IoParams(CAP_GPIO,       1,      "J12_6"),
    7: IoParams(CAP_GPIO,       0,      "J12_7"),
    8: IoParams(CAP_GPIO,       11,     "J12_8"),
    9: IoParams(CAP_GPIO,       12,     "J12_9"),
    10: IoParams(CAP_GPIO,      18,     "J12_10"),
    11: IoParams(CAP_GPIO,      19,     "J12_11"),
    12: IoParams(CAP_GPIO,      20,     "J12_12"),
    13: IoParams(CAP_GPIO,      21,     "J12_13"),
    14: IoParams(CAP_GPIO,      22,     "J12_14"),
    15: IoParams(CAP_GPIO,      23,     "J12_15"),
    16: IoParams(CAP_RESERVED,  -1,     "3.3VD"),
    17: IoParams(CAP_RESERVED,  -1,     "3.3VD"),
    18: IoParams(CAP_RESERVED,  -1,     "5VD"),
    19: IoParams(CAP_RESERVED,  -1,     "5VD"),
    20: IoParams(CAP_RESERVED,  -1,     "GND"),
    21: IoParams(CAP_GPIO,      9,      "J13_1"),
    22: IoParams(CAP_GPIO,      10,     "J13_2"),
    23: IoParams(CAP_GPIO,      9,      "J13_3"),
    24: IoParams(CAP_GPIO,      10,     "J13_4"),
    25: IoParams(CAP_RESERVED,  -1,     "GND"),
    26: IoParams(CAP_RESERVED,  -1,     "J13_6"),
    27: IoParams(CAP_RESERVED,  -1,     "J13_7"),
    28: IoParams(CAP_RESERVED,  -1,     "J13_8"),
    29: IoParams(CAP_RESERVED,  -1,     "J13_9"),
    30: IoParams(CAP_RESERVED,  -1,     "GND"),
    31: IoParams(CAP_GPIO,      2,      "J12_11"),
    32: IoParams(CAP_GPIO,      3,      "J13_12"),
    33: IoParams(CAP_GPIO,      4,      "J13_13"),
    34: IoParams(CAP_GPIO,      5,      "J13_14"),
    35: IoParams(CAP_RESERVED,  -1,     "RESET"),
    36: IoParams(CAP_RESERVED,  -1,     "3.3VD"),
    37: IoParams(CAP_RESERVED,  -1,     "3.3VD"),
    38: IoParams(CAP_RESERVED,  -1,     "5VD"),
    39: IoParams(CAP_RESERVED,  -1,     "5VD"),
    40: IoParams(CAP_RESERVED,  -1,     "GND"),
})

"""
Carambola2 board pin description
:link 8devices:
:link openwrt:
"""

# J13 = {
#     1:  {"gpio": 9, "alt": ["UART TX"]},
#     2:  {"gpio": 10, "alt": ["UART RX"]},
#     3:  {"gpio": "??", "alt": ["UART TX C"]},
#     4:  {"gpio": "??", "alt": ["UART TX C"]},
#     5:  {"gpio": None, "alt": ["GND"]},
#     6:  {"gpio": None, "alt": ["USB+"]},
#     7:  {"gpio": None, "alt": ["USB-"]},
#     8:  {"gpio": None, "alt": ["USB+ C"]},
#     9:  {"gpio": None, "alt": ["USB- C"]},
#     10: {"gpio": None, "alt": ["GND"]},
#     11: {"gpio": 2, "alt": ["SPI CS"]},
#     12: {"gpio": 3, "alt": ["SPI CLK"]},
#     13: {"gpio": 4, "alt": ["SPI MOSI"]},
#     14: {"gpio": 5, "alt": ["SPI MISO"]},
#     15: {"gpio": None, "alt": ["RESET"]},
#     16: {"gpio": None, "alt": ["3.3VD"]},
#     17: {"gpio": None, "alt": ["3.3VD"]},
#     18: {"gpio": None, "alt": ["5VD"]},
#     19: {"gpio": None, "alt": ["5VD"]},
#     20: {"gpio": None, "alt": ["GND"]},
# }

# J12 = {
#     1:  {"gpio": 17, "alt": ["LED6"]},
#     2:  {"gpio": 16, "alt": ["LED5"]},
#     3:  {"gpio": 15, "alt": ["LED4"]},
#     4:  {"gpio": 14, "alt": ["LED3"]},
#     5:  {"gpio": 13, "alt": ["LED2"]},
#     6:  {"gpio": 1, "alt": ["LED1"]},
#     7:  {"gpio": 0, "alt": ["LED0"]},
#     8:  {"gpio": 11, "alt": ["LED5"]},
#     9:  {"gpio": 12, "alt": ["LED5"]},
#     10: {"gpio": 18, "alt": ["I2S"]},
#     11: {"gpio": 19, "alt": ["I2S"]},
#     12: {"gpio": 20, "alt": ["I2S"]},
#     13: {"gpio": 21, "alt": ["I2S"]},
#     14: {"gpio": 22, "alt": ["I2S"]},
#     15: {"gpio": 23, "alt": ["SPDIF"]},
#     16: {"gpio": None, "alt": ["3.3VD"]},
#     17: {"gpio": None, "alt": ["3.3VD"]},
#     18: {"gpio": None, "alt": ["5VD"]},
#     19: {"gpio": None, "alt": ["5VD"]},
#     20: {"gpio": None, "alt": ["GND"]},
# }

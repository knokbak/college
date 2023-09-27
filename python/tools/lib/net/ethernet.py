############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Interface with the ethernet layer and TX/RX frames
# OK - 27 Sep 2023

import socket
from typing import Callable

ETH_P_ALL = 3

def rx_socket(callback: Callable):
    sock = socket.socket(socket.AF_PACKET)

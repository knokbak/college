############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Crappy port scanner
# OK - 27 Sep 2023

from functools import partial
import socket
import threading

def scan(target: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = sock.connect((target, port))
        print(f'{port} ... open')
    except:
        print(f'{port} ... closed')

def main():
    target = input('Enter domain or IP address: ')

    for port in range(26):
        thread = threading.Thread(None, partial(scan, target, port))
        thread.run()
    

if __name__ == '__main__':
    main()

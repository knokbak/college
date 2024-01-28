############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Encrypt/decrypt values with a Ceaser cipher
# OK - 24 Jan 2024

import sys

def encrypt_value(val: str, key: int) -> str:
    encrypted = ''
    for char in val:
        encrypted += stream_cipher(char, key)
    return encrypted


def decrypt_value(val: str, key: int) -> str:
    decrypted = ''
    for char in val:
        decrypted += stream_cipher(char, -key)
    return decrypted


def stream_cipher(char: str, manipulate_by: int) -> str:
    # ord converts a character to its unicode value (an integer)
    # chr converts an integer to its unicode character (a string)
    # sys.maxunicode is the maximum unicode value (an integer)
    return chr(ord(char) + (manipulate_by % (sys.maxunicode - 1)))


def get_key() -> int:
    try:
        return int(input('Enter key: '))
    except ValueError:
        print('Invalid key')
        return get_key()


def main():
    while True:
        option = input('Encrypt or decrypt? [e/d]: ')
        match option:
            case 'e':
                value = input('Enter value to encrypt: ')
                key = get_key()
                print(f'Encrypted value: {encrypt_value(value, key)}')
            case 'd':
                value = input('Enter value to decrypt: ')
                key = get_key()
                print(f'Decrypted value: {decrypt_value(value, key)}')
            case _:
                print('Exiting...')
                exit()
        
        print('\n\n')


if __name__ == '__main__':
    main()

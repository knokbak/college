############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Testing menu system library
# OK - 26 Sep 2023

from main import prompt_menu

def func_one():
    print('hello 1')

def func_two():
    print('hello 2')

def main():
    prompt_menu('Select an action!', [ ('line 1', func_one), ('line 2', func_two) ])

if __name__ == '__main__':
    main()

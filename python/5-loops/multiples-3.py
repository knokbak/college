############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# End of day task
# OK - 27 Sep 2023

from ..menu.main import prompt_menu

def multiples_of_3():
    for i in range(0, 100, 3):
        print(i)

def fav_number():
    name = input('Enter name: ')
    number = int(input('Enter number: '))
    count = 0

    while True:
        if (number == count):
            print(f'{count} is the number {name} chose')
            break
        count += 1

def times_table():
    num = int(input('Enter number: '))

    for i in range(13):
        print(f'{i} * {num} = {i * num}')

def main():
    prompt_menu('Select a mode', [
        ('3 is the tragic number', multiples_of_3),
        ('Got your number', fav_number),
        ('Times table', times_table)
    ])

if __name__ == '__main__':
    main()

############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Random search function - this is horrifically inefficient
# OK - 6 Dec 2023

from random import randint

def search(lst: list, param):
    count = 0
    checked = []
    while len(checked) < len(lst):
        count += 1
        index = randint(0, len(lst) - 1)
        if lst[index] == param:
            print(f'Took {count} iterations')
            return index
        else:
            if not index in checked:
                checked.append(index)
    print(f'Took {count} iterations')
    return -1


def main():
    lst = input('Enter items seperated by a space: ').split(' ')
    param = input('Enter item to search for: ')
    result = search(lst, param)
    if result == -1:
        print(f'{param} could not be found in the list')
        return
    print(f'{param} is at index {result}')


if __name__ == '__main__':
    main()

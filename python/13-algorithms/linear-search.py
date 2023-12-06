############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Linear search function
# OK - 6 Dec 2023

def linear_search(lst: list, param):
    for i in range(0, len(lst)):
        item = lst[i]
        if item == param:
            return i
    return -1


def main():
    lst = input('Enter items seperated by a space: ').split(' ')
    param = input('Enter item to search for: ')
    result = linear_search(lst, param)
    if result == -1:
        print(f'{param} could not be found in the list')
        return
    print(f'{param} is at index {result}')


if __name__ == '__main__':
    main()

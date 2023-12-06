############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

def count_duplicates(array: list, value: str) -> int:
    count = 0
    for item in array:
        if item == value:
            count = count + 1
        
    return count


def main():
    lst = input('Enter a list of values split using spaces: ').split(' ')
    val = input('Enter the value to count for: ')
    print(f'{val} is found {count_duplicates(lst, val)} times in the list')


if __name__ == '__main__':
    main()

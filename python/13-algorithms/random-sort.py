############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Laughably inefficient sorting algorithm
# Literally just shuffles the list until it is sorted
# OK - 7 Dec 2023

from random import shuffle
from time import perf_counter

def sort(lst: list) -> list:
    count = 0
    in_right_order = False
    while not in_right_order:
        count += 1
        if is_sorted(lst):
            in_right_order = True
        else:
            shuffle(lst)
    print(f'Took {count:,} iterations')
    return lst


def is_sorted(lst: list) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def main():
    lst = input('Enter items seperated by a space: ').split(' ')
    task_started = perf_counter()
    result = sort(lst)
    task_finished = perf_counter()
    print(f'Task took {task_finished - task_started} seconds')
    print(f'Sorted list: {result}')


if __name__ == '__main__':
    main()

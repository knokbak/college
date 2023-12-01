def find_min(arr: list[int | float]) -> float:
    if len(arr) == 0:
        raise ValueError('Cannot find minimum value of empty list')
    
    min = arr[0]
    for num in arr:
        if num < min:
            min = num

    return min


def main():
    lst = input('Enter a list of numbers seperated by spaces: ').split(' ')
    nums = []
    for num in lst:
        nums.append(float(num))
    
    print(f'Lowest number is: {find_min(nums)}')


if __name__ == '__main__':
    main()

def find_max(arr: list[int | float]) -> float:
    if len(arr) == 0:
        raise ValueError('Cannot find maximum value of empty list')
    
    max = arr[0]
    for num in arr:
        if num > max:
            min = num

    return max


def main():
    lst = input('Enter a list of numbers seperated by spaces: ').split(' ')
    nums = []
    for num in lst:
        nums.append(float(num))
    
    print(f'Highest number is: {find_max(nums)}')


if __name__ == '__main__':
    main()

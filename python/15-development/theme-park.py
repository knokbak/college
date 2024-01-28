def get_daily_totals() -> "list[int]":
    totals = []
    print('Enter the number of visitors for each day of the week...')
    for i in range(7):
        value = get_valid_input(i)
        totals.append(value)
    return totals


def get_valid_input(day: int) -> int:
    try:
        value = int(input(f'Enter tickets purchased for {get_weekday_by_index(day)}: '))
    except ValueError:
        print('Invalid input')
        return get_valid_input(day)
    else:
        if value < 0:
            print('Number cannot be negative')
            return get_valid_input(day)
        else:
            return value


def get_average_guests(totals: "list[int]") -> float:
    return sum(totals) / len(totals)


def get_minimum_maximum_index(totals: "list[int]") -> "tuple[int, int]":
    maximum = 0
    minimum = 0
    for i in range(len(totals)):
        if totals[i] > totals[maximum]:
            maximum = i
        if totals[i] < minimum:
            minimum = i
    return (minimum, maximum)


def get_minimum_maximum(totals: "list[int]") -> "tuple[int, int]":
    (min_index, max_index) = get_minimum_maximum_index(totals)
    return (totals[min_index], totals[max_index])


def get_weekday_by_index(index: int) -> str:
    values = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return values[index]


def main():
    totals = get_daily_totals()
    average = round(get_average_guests(totals), 1)
    (minimum, maximum) = get_minimum_maximum(totals)
    (quietest_day, busiest_day) = get_minimum_maximum_index(totals)
    print(f'AVERAGE: {average}')
    print(f'BUSIEST DAY: {get_weekday_by_index(busiest_day)} ({maximum})')
    print(f'QUIETEST DAY: {get_weekday_by_index(quietest_day)} ({minimum})')


if __name__ == '__main__':
    main()

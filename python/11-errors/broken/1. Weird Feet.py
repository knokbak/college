def take_input() -> float:
    try:
        return float(input('Enter number of feet:\t'))
    except ValueError:
        print('Error: Cannot convert to a number')
        return take_input()

feet = take_input()
metres = feet * 0.305
print(str(feet) + " Feet is " + str(metres) + " Meters")

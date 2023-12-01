def valid_input(prompt: str) -> int:
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('Please enter a number!')
            return valid_input(prompt)
        else:
            if num >= 0 and num <= 5:
                return num
            else:
                print('Please enter a number between 0 and 5!')
                return valid_input(prompt)


def main():
    num = valid_input('Enter a number between 0 and 5: ')
    print(f'You entered {num}')


if __name__ == '__main__':
    main()

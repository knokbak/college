############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Check if a password is in a list of passwords
# OK - 15 Nov 2023

def read_lines() -> list[str]:
    f = open('rockyou1000.txt', 'r')
    lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip().lower()
    f.close()
    return lines


def append_to_file(text: str) -> None:
    f = open('rockyou1000.txt', 'a')
    f.write(text + '\n')
    f.close()


def main():
    lines = read_lines()
    while True:
        passwd = input('Enter password: ')
        if passwd.lower() in lines:
            print('Password is in the list! PANIC!!!!!')
        else:
            append_to_file(passwd)
            print('Password is not in the list, but now is! PANIC!!!!!')


if __name__ == '__main__':
    main()

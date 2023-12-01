############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# File nonsense
# OK - 15 Nov 2023

def append_to_file(text: str) -> None:
    f = open('file.txt', 'a')
    f.write(text + '\n')
    f.close()


def main():
    while True:
        append_to_file(input('Enter text to append to file: '))
    

if __name__ == '__main__':
    main()

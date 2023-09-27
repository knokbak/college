############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Does weird countdown stuff
# OK - 27 Sep 2023

def countdown():
    for i in range(20, 0, -1):
        if i % 3 == 0:
            break
        print(i)

def main():
    countdown()

if __name__ == '__main__':
    main()

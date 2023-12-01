############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Ooooooooo.... passwords!!!
# OK - 15 Nov 2023

def read_lines() -> list[str]:
    f = open('rockyou1000.txt', 'r')
    lines = f.readlines()
    f.close()
    lines.sort()
    f = open('rockyou1000.txt', 'w')
    f.writelines(lines)
    f.close()
    return lines


def main():
    lines = read_lines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
    print(lines)


if __name__ == '__main__':
    main()

############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Convert a 3 digit number to words
# OK - 8 Nov 2023

def num_to_word(num: int, position: str) -> str:
    if num < 0 or num > 10:
        raise ValueError('num must be between 0 and 10')
    
    if position == 'hundreds' or position == 'units':
        words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        if position == 'hundreds' and num == 0:
            raise ValueError('hundreds cannot be zero!')
        return words[num]
    elif position == 'tens':
        words = [None, 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        return words[num]
    else:
        raise ValueError('position must be "hundreds", "tens" or "units"')


def prompt():
    num = int(float(input('Enter a 3 digit number: ')))
    if num < -999 or num > 999:
        raise ValueError('num must be between -999 and 999')
    
    negative = False
    if num < 0:
        num = abs(num)
        negative = True
    
    num_str = str(num)
    output = ''
    for (i, digit) in enumerate(num_str):
        if int(digit) == 0:
            continue

        if len(num_str) == 3 and i == 0:
            output += num_to_word(int(digit), 'hundreds') + ' hundred '
            if not int(num_str[1]) == 0 or not int(num_str[2]) == 0:
                output += 'and '
        elif (len(num_str) == 3 and i == 1) or (len(num_str) == 2 and i == 0):
            if int(digit) == 1:
                words = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
                output += words[int(num_str[len(num_str) - 1])] + ' '
                break;
            output += num_to_word(int(digit), 'tens') + ' '
        else:
            output += num_to_word(int(digit), 'units')
    
    if negative:
        output = 'minus ' + output

    return output
    

def main():
    while True:
        print(prompt())


if __name__ == '__main__':
    main()

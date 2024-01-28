############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Calculate strength of password
# OK - 17 Jan 2024

# Receive password as input, string
def get_password() -> str:
    try:
        password = input('Enter password: ')
    except KeyboardInterrupt:
        print('\nGoodbye')
        exit()
    else:
        return password


# Check if password contains lower case letters
def check_for_lower_case(password: str) -> bool:
    for char in password:
        if char.islower():
            return True
    return False


# Check if password contains upper case letters
def check_for_upper_case(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


# Check if password contains numbers
def check_for_number(password: str) -> bool:
    for char in password:
        if char.isdigit():
            return True
    return False


# Check if password contains symbols
def check_for_symbol(password: str) -> bool:
    for char in password:
        if not char.isalnum():
            return True
    return False


# Check password strength, return list of reasons
def get_strength(password: str) -> "list[str]":
    values = []
    if len(password) <= 6:
        return []
    
    if check_for_lower_case(password):
        values.append('lower case')
    if check_for_upper_case(password):
        values.append('upper case')
    if check_for_number(password):
        values.append('number')
    if check_for_symbol(password):
        values.append('symbol')

    if len(password) >= 26:
        values.append('length')
    
    return values


# Convert list of reasons to strength
def strength_to_str(strength: "list[str]") -> str:
    match len(strength):
        case 0:
            print('Your password is one of the worst passwords I have ever seen')
            exit()
        case 1:
            return 'VERY WEAK'
        case 2:
            return 'WEAK'
        case 3:
            return 'MEDIUM'
        case 4:
            return 'STRONG'
        case _:
            raise ValueError('Invalid strength')


def main():
    password = get_password()
    strength = get_strength(password)
    print(', '.join(strength))

    if len(strength) == 0:
        print('Password is too short!')
        print('Strength: WEAK')
        return
    
    print(f'Strength: {strength_to_str(strength)}')
    

if __name__ == '__main__':
    main()

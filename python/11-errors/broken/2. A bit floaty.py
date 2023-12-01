def take_float_input(prompt: str) -> float:
    try:
        val = float(input(prompt))
    except ValueError:
        print('Error: Provide a numeric value')
        return take_float_input(prompt)
    else:
        if val == 0:
            print('Error: Cannot divide by zero')
            return take_float_input(prompt)
        else:
            return val

firstNumber = take_float_input('Please enter first value:\t')
secondNumber = take_float_input('Please enter second value:\t')

answer = firstNumber / secondNumber
 
print('The result of division is ' + str(answer))

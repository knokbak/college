subTotal = 0.0 
gratuityRate = 0.0 
gratuity = 0.0 
total = 0.0 

def take_float_input(prompt: str, min: float | None, max: float | None) -> float:
    try:
        val = float(input(prompt))
    except ValueError:
        print('Error: Provide a numeric value')
        return take_float_input(prompt, min, max)
    else:
        if not round(val, 2) == val:
            print('Error: Provide a value with up to two decimal places')
            return take_float_input(prompt, min, max)
        elif min is not None and val < min:
            print('Error: Provide a value greater than or equal to ' + str(min))
            return take_float_input(prompt, min, max)
        elif max is not None and val > max:
            print('Error: Provide a value less than or equal to ' + str(max))
            return take_float_input(prompt, min, max)
        else:
            return val

subTotal = take_float_input('Please enter the bill sub-total ', 0, None)
gratuityRate = take_float_input('Please enter the gratuity rate ', 0, 100)

if gratuityRate == 0:
    gratuity = 0
else:
    gratuity = subTotal * (gratuityRate / 100)

total = subTotal + gratuity

print('The gratuity is £', gratuity)
print("The grand total is £",  total)

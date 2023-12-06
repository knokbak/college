############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

def division(a, b):
    try:
        val = float(a) / float(b)
    except ValueError:
        print("Error: Cannot divide by a non-numeric value")
        exit(1)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        exit(1)
    else:
        print("Oh my goodness, I can divide!!!!")
        return val

def main():
    num1 = input("enter number: ")
    num2 = input("enter another number: ")
    print(f"the answer is...{division(num1, num2)}")

if __name__ == "__main__":
    main()

while True:
    num = input("Please give the number you would like to multiply: ")
    if num.isdigit():
        for table in range(1, 13):
                ans = int(num) * table
                print(f"{num} x {table} = {ans}")
    else:
        print("Error! Please enter a number: ")

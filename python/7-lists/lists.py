############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Print even values from a list
# OK - 26 Oct 2023

def even_values(values: list[int]) -> list[int]:
    even = []
    for value in values:
        if value % 2 == 0:
            even.append(value)
    return even

def main():
    numbers = [0, 5, 4, 3, 6, 8, 7, 9, 2, 1]
    print(even_values(numbers))

if __name__ == "__main__":
    main()

"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""

def main():
    subtraction_interface()


def subtraction_interface():
    """
    This function asks the user for two real numbers, will return an
    error is real numbers are not give. Once two real numbers have been
    submitted the function will subtract the second given value from the
    first.
    PRE:  user enters two real numbers
    POST:  total equals the difference between the first and second numbers
    shown as a real number
    """
    print('This program subtracts one number from another.')
    num1 = input('Enter first number: ')
    num1 = float(num1)
    num2 = input('Enter second number: ')
    num2 = float(num2)
    total = num1 - num2
    print('The result is : ' + str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

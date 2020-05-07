"""
File: moon_weight.py
--------------------
Write a program to prompt the user for a weight on earth
and print the equivalent weight on the moon. The user (an earthling)
enters a weight on earth. Your program will print the corresponding
weight on the moon, which is 16.5% of the weight on earth.
"""


def main():
    convert_weight()

def convert_weight():
    """
    This program takes a user input defined as the weight in pounds of
    an object on earth and formats it as a float and then converts
    the value to the equivalent weight in pounds on the moon.
    PRE: Value entered is valid; defined as string value in pounds.
    POST: Converted value is returned to the user in float format.
    """
    weight = float(input('Enter weight on Earth in pounds: '))
    weight *= .165
    print(f'Equivalent weight on moon: {weight}')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

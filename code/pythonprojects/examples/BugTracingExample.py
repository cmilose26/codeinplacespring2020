"""
File: buggytrace.py
-------------------
This program is an example to help you trace through code.
The "bug" is that parameters of primitive types (such as int)
are passed by value, so changes to a parameter in a function
don't change the variable outside the function.
"""

# NOTE: This program is buggy!!

def main():
    x = 3
    add_five(x)
    print("x = " + str(x))

def add_five(x):
    x += 5


def fix_bug(x):
    return x
    # This function is empty but shows the answer to
    # how to fixe the add_five program and the expected
    # out put for running add_five in the main function
    # To fix the add_five function in a new line below
    # x += 5 put a return function that returns the
    # variable x. Or go see the BugTracingSolution.py file.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

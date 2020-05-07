"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    count_down()

def count_down():
    """
    This function count down from 10 ending at 1 after which we
    have liftoff.
    PRE:  start is assigned the value ten
    POST:  Liftoff
    """
    start = 10
    print(start)
    for i in range(9):
        start -= 1
        print(start)
    print ('Liftoff!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

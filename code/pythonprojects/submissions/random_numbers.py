"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100


def main():
    generate_random()


def generate_random():
    """
    This function generates a set of random numbers based on the values
    given for the constants NUM_RANDOM, MIN_RANDOM, and MAX_RANDOM.
    PRE:  The three named constants have been assigned valid values
    POST:  i in range random numbers have been generated
    """
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

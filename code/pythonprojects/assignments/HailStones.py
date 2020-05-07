"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""

def main():
    hailstones()


def hailstones():
    """
    PRE:
    POST:
    """
    n = float(input('Enter a number: '))
    while n.is_integer() == False or n < 1:
        print('\nInvalid entry. Number must be a positive integer.')
        n = float(input('Please enter another number: '))
    count = 0
    print(f'\nUser entered {int(n)}.')
    while n != 1:
        n = int(n)
        if (n % 2) == 0:
            print(f'{n} is even, so take half: ' + str(int(n/2)))
            n /= 2
            count += 1
        else:
            print(f'{n} is odd, so make 3n + 1: ' + str(int((3*n)+1)))
            n *= 3
            n += 1
            count += 1
    print(f'This process took {count} steps to reach 1.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

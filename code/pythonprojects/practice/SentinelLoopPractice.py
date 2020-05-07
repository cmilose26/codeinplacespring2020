"""
File: sentinelloop.py
------------------
A sentinel is a value that signals the end of user input.
A sentinel loop repeats until a sentinal value is seen.
"""


def main():
    """
    Takes user inputs and adds them to a total variable unless the
    user's input is equal to -1, the sentinel value.
    PRE: none
    POST: User has entered -1.
    """

    #defines the variables required in a sentinel loop that outputs the total
    # the integers the user has input
    total = 0
    num = 0

    # While user input is not the sentinel value take user input and add to total
    while num != -1:
        num = int(input('Enter a number: '))
        if num == -1:
            break
        total += num
    print(f'Total is {total}')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
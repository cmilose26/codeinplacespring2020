"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

# NUM_RIGHT is the number of consecutive correct responses needed
# to pass the test
NUM_RIGHT = 3
RANDOM_MIN = 10
RANDOM_MAX = 99

def main():
    addition_problem()


def addition_problem():
    """
    This function generates two random integers between the values
    assigned for the constants RANDOM_MIN and RANDOM_MAX and then asks
    the user to find the sum of the two numbers. Function then checks whether 
    the user's answer is correct and continously runs until they have answered
    a set number of questions in a row correctly. Number required to answer in
    a row is assinged by the constant NUM_RIGHT.
    """
    correct_answer = 0
    while correct_answer < NUM_RIGHT:
        num1 = int(random.randint(RANDOM_MIN, RANDOM_MAX))
        num2 = int(random.randint(RANDOM_MIN, RANDOM_MAX))
        answer = num1 + num2
        print('What is '+ str(num1) + ' + ' + str(num2) + '?')
        user_answer = input('Your answer: ')
        if int(user_answer) == int(answer):
            correct_answer += 1
            if correct_answer == 1:
                print("Correct! You've answered " + str(correct_answer) + " question in a row right.")
            else:
                print("Correct! You've answered " + str(correct_answer) + " questions in a row right.")
        else:
            correct_answer = 0
            print('Incorrect. The expected answer is ' + str(answer) +'.')
    print('Congratulations! You mastered addition.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

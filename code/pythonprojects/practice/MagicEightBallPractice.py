"""
Write a program to simulate a magic eight ball. The program should
prompt the user to type a yes or no question and give a random
answer from a set of predetermined answers.
"""

import random


def main():
    print('\nType QUIT to end the program.')
    magic_eight_ball()


def magic_eight_ball():
    """
    Program randomly answers yes or no questions with six preset responses.
    PRE: None
    POST: User has input "quit".
    """
    # While loop enables program to run constantly until it is stopped by the user.
    while True:
        question = input('Ask a yes or no question: ')

        # Conditions under which function will run
        if question != ' ':
            response = random.randint(0,5)
            if response == 0:
                print('Concentrate and ask again.\n')
            elif response == 1:
                print('You must be patient.\n')
            elif response == 2:
                print('Prosperity comes to those who wait!\n')
            elif response == 3:
                print('Indubitably!\n')
            elif response == 4:
                print('It is so.\n')
            elif response == 5:
                print('Comme ci comme ca...\n')

        #Conditions that are not valid inputs and prompt the user to enter another question
        else:
            print('Ask actual questions, run again!\n')
            break

        # Condition under which the while loop is stopped.
        if question.lower() == 'quit':
            print('Program Stopped.\n')
            break


# Calls the function
if __name__ == '__main__':
    main()
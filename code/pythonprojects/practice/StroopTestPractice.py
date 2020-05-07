"""
File StroopTestPractice.py
__________________________
In psychology, the Stroop effect is a demonstration
of cognitive interference where a delay in the reaction
time of a task occurs due to a mismatch in stimuli. Use the
starter code below to create a program that tests the Stroop
Effect.

"""

import time
import random

from termcolor import colored

PHASE_TIME_S = 10
is_phase_1 = True

def main():
    print_intro()
    run_single_test(True)


def print_intro():
    '''
    Function: print intro
    Prints a simple welcome message
    '''
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('pink', 'pink')


def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'pink'])


def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'pink': # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


def run_single_test(is_phase_1):
    color = random_color_name()
    if True:
        print_in_color(color, color)
    else:
        print_in_color(color, random_color_name())



if __name__ == '__main__':
    main()
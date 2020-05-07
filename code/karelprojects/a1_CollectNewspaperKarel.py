from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def main():
    collect_newspaper()
    return_to_start()

def collect_newspaper():
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    pick_beeper()


def return_to_start():
    turn_around()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()


def move_to_wall():
    while front_is_clear():
        move()


def turn_right():
    """
    Turns karel right using three turn lefts
    """
    for i in range (3):
        turn_left()

def turn_around():
    """
    Turns karel around by 180 degrees
    """
    for i in range (2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program("CollectNewsPaperKarel.w")


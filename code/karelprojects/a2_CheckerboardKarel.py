from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    create_checkerboard()

def create_checkerboard():
    """
    Tells Karel to lay down beepers on every other space both horizontally
    and vertically to create a checkerboard pattern made out of beepers and
    blank corners.
    PRE: Karel starts in position (1,1), her front is clear and she is facing east
    POST: Karel has finished laying the last row, is facing east, and her front is blocked
    """
    place_odd_row()
    while left_is_clear():
        get_into_position()
        place_even_row()
        if left_is_clear():
            get_into_position()
            place_odd_row()


def place_odd_row():
    """
    Tells Karel to place a beeper on in the first space in a row and
    then another beeper every two spaces from then on out.
    PRE: Karel is in an odd numbered row facing east with her front clear
    POST: Karel has finished placing beepers, leaving the last space blank
    and is facing east with her front blocked.
    """
    put_beeper()
    move()
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


def place_even_row():
    """
    Tells Karel to leave the first space in a row blank, then move to the second
    space and place a beeper, after which Karel places a beeper once ever other space.
    PRE: Karel is in an even numbered row facing east with her front clear
    POST: Karel has finished placing beepers, leaving the first space blank and
    has put a beeper in the last space in the row. Additionally, Karel is facing
    east with her front blocked.
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


def get_into_position():
    """
    Tells Karel to turnaround, move as far west as she can, the move north/up
    one space and face east in preparation to fill in another row.
    PRE: Karel is facing east with her front blocked.
    POST: Karel is facing east with her front clear.
    """
    turn_around()
    move_to_wall()
    face_north()
    move()
    face_east()


def move_to_wall():
    """
    Tells Karel to continue to move as long as her front is clear.
    PRE: Karel's front is clear
    POST: Karel's front is blocked
    """
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

def face_north():
    """
    Turns karel left as many times as needed to face north
    """
    while not_facing_north():
        turn_left()

def face_south():
    """
    Turns karel left as many times as needed to face south
    """
    while not_facing_south():
        turn_left()

def face_east():
    """
    Turns karel left as many times as needed to face east
    """
    while not_facing_east():
        turn_left()

def face_west():
    """
    Turns karel left as many times as needed to face east
    """
    while not_facing_west():
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program("CheckerboardKarel.w")

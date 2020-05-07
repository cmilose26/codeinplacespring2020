from karel.stanfordkarel import *

"""
File: OurSteepleChaseKarel.py
--------------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():
    for i in range (8):
        if front_is_clear():
            move()
        else:
            jump_steeples()

def jump_steeples():
    """
    Tells Karel to jump multiple steeples.
    PRE: Karel is facing east and her front is clear or blocked
    POST: Karel is facing east and her front is clear or blocked.
    """
    move_to_wall()
    face_north()
    up_steeple()
    down_steeple()
    face_east()


def up_steeple():
    """
    Tells Karel to go up a single steeple.
    PRE: Karel is facing north and her right is blocked.
    POST: Karel is facing east and her front is clear.
    """
    while right_is_blocked():
        move()
    turn_right()
    move()


def down_steeple():
    """
    Tells Karel to go down a single steeple
    PRE: Karel is facing east and her front is clear
    POST: Karel is facing south and her front is blocked.
    """
    face_south()
    while front_is_clear():
        move()


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
    run_karel_program("SteepleChaseKarel.w")

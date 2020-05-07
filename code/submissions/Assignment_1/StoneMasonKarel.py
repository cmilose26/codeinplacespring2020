from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.

Global Assumptions:
    Karel starts at (1, 1) facing east and has an infinite number
        of beepers
    Columns are always four spaces apart w/ inclusive counting
    The last column is always has a wall after it
    The height of arches is variable but will always be market by
        a wall at the end
    No multiple beepers per space allowed, columns may already have
        beepers present
"""

def main():
    while front_is_clear():
        build_columns()
    build_column()

# Has Karel replace missing beepers in all columns except for the
# last one and then finds the next column
def build_columns():
    """
    pre: Karel is in row 1 at the bottom of a column
    post: Karel replaced the misssing beepers and returned to the bottom of the column,
    faces east, and then finds the next column to fix
    """
    face_north()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()
    if front_is_blocked():
        turn_around()
        while front_is_clear():
            move()
    face_east()
    for i in range (4):
        move()

# Has Karel build one column, the last column
def build_column():
    """
    pre: Karel is in row 1 at the bottom of a column
    post: Karel replaced the misssing beepers and returned to the bottom of the column
    and then faces east
    """
    face_north()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()
    if front_is_blocked():
        turn_around()
        while front_is_clear():
            move()
    face_east()

# Checks if Karel's back is blocked
def back_is_blocked():
    turn_around()
    front_is_blocked()

# Turns Karel right using three turn lefts
def turn_right():
    for i in range (3):
        turn_left()

# Turns Karel around by 180 degrees
def turn_around():
    for i in range (2):
        turn_left()

# Turns Karel left as many times as needed to face north
def face_north():
   while not_facing_north():
       turn_left()

# Turns Karel left as many times as needed to face south
def face_south():
   while not_facing_south():
       turn_left()

# Turns Karel left as many times as needed to face east
def face_east():
   while not_facing_east():
       turn_left()

# Turns Karel left as many times as needed to face east
def face_west():
   while not_facing_west():
       turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

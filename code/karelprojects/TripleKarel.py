from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    for i in range (3):
        paint_building()
    turn_left()
     
# Has Karel paint one building ie three walls
def paint_building():
    """
    pre: The left of Karel is blocked
    post: Karel has painted three walls and moved to the start
          of a new building 
    """
    for i in range (3):
        paint_wall()
    turn_around()
    move()

# Has Karel paint one wall of a building
def paint_wall():
    """
    pre: The left of Karel is blocked
    post: The wall has ended and Karel has turned a corner
    """
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()

# Turns Karel right using three turn lefts
def turn_right():
    for i in range (3):
        turn_left()

# Turns Karel around by 180 degrees
def turn_around():
    for i in range (2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program("Triple1.w")

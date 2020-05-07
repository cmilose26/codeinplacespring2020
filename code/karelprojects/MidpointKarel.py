from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    if front_is_blocked():
        put_beeper()
    else:
        mark_corners()
        find_midpoint()
        move_to_wall()
        turn_around()
        pick_beepers()
        return_to_midpoint()

def return_to_midpoint():
    """
    Has Karel turnaround and move to the single remaining beeper so that
    she ends on the midpoint
    pre: Karel's front is not clear and she has executed the pick_beepers()
         function
    post: Karel is positioned on the corner that is in the middle of the row
    """
    turn_around()
    move_to_beeper()

def find_midpoint():
    """
    Tells Karel where the midpoint of a row in a world is by having 
    Karel place beepers from the outside in until Karel has moved to the
    middle most corner where she then places a second beeper
    pre: Karel is on a beeper free corner
    post: Karel places the second beeper on the midpoint
    """
    while no_beepers_present():
        move_to_beeper()
        turn_around()
        move()
        put_beeper()
        move()
    # While loop above has Karel actually move one space too far
    # hence code below which moves Karel one corner back to the midpoint
    turn_around()
    move()
    put_beeper()

def mark_corners():
    """
    Given Karel is starting on the coordinates (1, 1) function has Karel mark
    the corners of the world with beepers
    pre: Karel starts on coordinate (1, 1)
    post: Karel has placed a beeper on the opposite corner, turnaround and 
          moved one space towards the center from that beeper
    """
    put_beeper()
    move_to_wall()
    put_beeper()
    turn_around()
    move()

def pick_beepers():
    """
    Picks up one beeper per corner in a row
    """
    while front_is_clear():
        pick_beeper()
        move()
    pick_beeper()

def move_to_wall():
    """
    Moves Karel to the nearest wall
    """
    while front_is_clear():
        move()   

def move_to_beeper():
    """
    Moves Karel while no beepers present
    """
    while no_beepers_present():
        move()  

def turn_right():
    """
    Turns Karel right using three turn lefts
    """
    for i in range (3):
        turn_left()

def turn_around():
    """
    Turns Karel around by 180 degrees
    """
    for i in range (2):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()

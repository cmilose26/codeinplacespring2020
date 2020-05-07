from karel.stanfordkarel import *

# File: Hopsitalkarel.py
# -----------------------------
# Here is a place to program your section problem

"""
Main keeps karel moving east as long as front is clear
"""
def main():
    while front_is_clear():
        keep_moving()

"""
Keeps karel moving when no beepers are present and
if a beeper is present builds a hospital 
pre:  There are no beepers present
post: A beeper is present
"""
def keep_moving():
    while no_beepers_present():
       move()
    if beepers_present():
        build_hospital()

"""
Moves karel when beeper is present in fashion to
create a 2 x 3 hospital of beepers.
pre:  karel is on a beeper
post: karel is facing east and has moved past the
      eastern most edge of the most recent hospital
"""
def build_hospital():
   while beepers_present():
       turn_left()
       move()
       for i in range (2):
           put_beeper()
           move()
       turn_corner()
       for i in range (2):
           put_beeper()
           move()
   put_beeper()
   turn_left()
   if   front_is_clear():
       move()

# turns karel right using three turn lefts
def turn_right():
   for i in range (3):
      turn_left()

# turns karel to face south
def turn_corner():
   turn_right()
   move()
   turn_right()
   move()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program("HospitalKarel.w")
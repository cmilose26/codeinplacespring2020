from karel.stanfordkarel import *


def main():
    move()
    while beepers_present():
        pick_beeper()
    turn_around()
    move()
    turn_around()


# still a classic.
def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("DoubleBeepers.w")
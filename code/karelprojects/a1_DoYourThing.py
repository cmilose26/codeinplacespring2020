from karel.stanfordkarel import *

def main():
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()

# This function turns Karel to the left three times
def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
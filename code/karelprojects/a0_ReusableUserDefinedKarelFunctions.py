

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

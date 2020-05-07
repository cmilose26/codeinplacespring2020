"""
File: nimm.py
-------------------------
Add your comments here.
"""

# STARTING_STONES is the constant that determines how many stones are in the pile at the start of a game of Nimm
STARTING_STONES = 20

def game_of_nimm():
    """
    The function game_of_nimm allows a user to alternate turns as player 1 and player 2 to complete a game of Nimm. The game starts with a number of stones
    defined by the constant STARTING_STONES and proceeds until there are no stones left. The last player to take a stone loses.
    PRE: STARTING_STONES > 0, though to truly play game STARTING_STONES should be at least 4
    POST: There are no stones left.
    """
    stonesleft = STARTING_STONES
    stonesremoved = 0
    turn = 0
    # This section of the function game_of_nimm starts the game and declares how many stones are starting in the pile
    print(f'There are {STARTING_STONES} stones left')
    while stonesleft > 0:
        # This section of the function game_of_nimm keeps track of which turn it is and which players turn it is
        turn += 1
        player = 2 if turn % 2 == 0 else 1
        stonesremoved = int(input(f'Player {player} would you like to remove 1 or 2 stones? '))
        # This section of the function game_of_nimm holds the mechanics for each turn and makes sure user entries are valid
        while stonesremoved not in [1, 2]:
            stonesremoved = int(input("Please enter 1 or 2: "))
        stonesleft -= stonesremoved
        if stonesleft > 0:
            print(f'\nThere are {stonesleft} stones left')
        else:
            print(f'\nPlayer {2 if player == 1 else 1} wins!') # Choose opposite player to get winner


game_of_nimm()
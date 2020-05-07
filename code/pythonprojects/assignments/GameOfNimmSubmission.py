"""
File: nimm.py
-------------------------
Add your comments here.
"""

# STARTING_STONES is the constant that determines how many stones are in the pile at the start of a game of Nimm
STARTING_STONES = 20

def main():
    game_of_nimm()

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
    print('There are ' + str(STARTING_STONES) + ' stones left')
    while stonesleft > 0:
        # This section of the function game_of_nimm keeps track of which turn it is and which players turn it is
        turn += 1
        if (turn % 2) == 0:
            player= 2
        else:
            player = 1
        stonesremoved = int(input('Player ' + str(player) + ' would you like to remove 1 or 2 stones? '))
        # This section of the function game_of_nimm holds the mechanics for each turn and makes sure user entries are valid
        while stonesremoved != 1 and stonesremoved != 2:
            stonesremoved = int(input("Please enter 1 or 2: "))
        if stonesremoved == 1:
            stonesleft -= int(stonesremoved)
            if stonesleft == 0:
                # This section of the function game_of_nimm determines which player won
                if player == 1:
                    player = 2
                else:
                    player = 1
                # This section of the function game_of_nimm declares the game over and names the winner
                print('')
                print('Player ' + str(player) + ' wins!')  
            else:
                print('')
                print('There are ' + str(stonesleft) + ' stones left')
        elif stonesremoved == 2:
            stonesleft -= int(stonesremoved)
            if stonesleft == 0:
                # This section of the function game_of_nimm determines which player won
                if player == 1:
                    player = 2
                else:
                    player = 1
                # This section of the function game_of_nimm declares the game over and names the winner
                print('')
                print('Player ' + str(player) + ' wins!')
            else:
                print('')
                print('There are ' + str(stonesleft) + ' stones left')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
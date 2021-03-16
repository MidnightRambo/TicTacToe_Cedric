# This is a tictactoe game for cedric. 
# Because it's just a small game i wanted to make no use of any outside libraries except random.
import random

# Creating my gamefield
game_orig = [
             "0", "\033[4m1\033[0m","\033[4m2\033[0m","\033[4m3\033[0m",
             "1", " "," "," ",
             "2", " "," "," ",
            "3", " ", " ", " "]

# this is just for resetting the field after a successful match
game = game_orig.copy()

# "graphical" interface
def game_print():
    print (game[0] + " " + game[1] + " " + game[2] + " " + game[3])
    print (game[4] + "|" + game[5] + "|" + game[6] + "|" + game[7])
    print (game[8] + "|" + game[9] + "|" + game[10] + "|" + game[11])
    print (game[12] + "|" + game[13] + "|" + game[14] + "|" + game[15])


# defining which row/column the user selects
row = None 
column = None

def intake():
    global row
    global column
    row = int(input("Row number: "))
    if row >= 1 and row <= 3:
        column = int(input("Column number: "))
        if column >= 1 and column <= 3:
            row = row
            column = column
        else:
            print("Number has to be between 1 and 3")
            column = None
    else:
        print("Number has to be between 1 and 3")
        row = None

# dfining our play
def play(): 
    if row == 1:
        game[4 + column]="X"
    elif row == 2:
        game[8 + column]="X"
    elif row == 3: 
        game[12 + column]="X"
        
# defining the computers play
def opponent_play():
    opponent_index=[]
    for (i, item) in enumerate(game):
        if item == " ":
            opponent_index.append(i)
    game[random.choice(opponent_index)] = "O"

# choosing if we won or lose 
def winner():
    # if the player wins
    if ( 
        # horizontal lines 
        game[5:8] == ['X','X','X'] or
        game[9:12] == ['X','X','X'] or 
        game[13:16] == ['X','X','X'] or
        # vertical lines 
        list(game[i] for i in [5, 9, 13]) == ['X','X','X'] or 
        list(game[i] for i in [6, 10, 14]) == ['X','X','X'] or 
        list(game[i] for i in [7, 11, 15]) == ['X','X','X'] or 
        # diagonal lines 
        list(game[i] for i in [5, 10, 15]) == ['X','X','X'] or 
        list(game[i] for i in [13, 10, 7]) == ['X','X','X'] 
    ):
        global winning
        winning = 1
        
def loser():        
    # if the computer wins
    if ( 
        # horizontal lines 
        game[5:8] == ['O','O','O'] or
        game[9:12] == ['O','O','O'] or 
        game[13:16] == ['O','O','O'] or
        # vertical lines 
        list(game[i] for i in [5, 9, 13]) == ['O','O','O'] or 
        list(game[i] for i in [6, 10, 14]) == ['O','O','O'] or 
        list(game[i] for i in [7, 11, 15]) == ['O','O','O'] or 
        # diagonal lines 
        list(game[i] for i in [5, 10, 15]) == ['O','O','O'] or 
        list(game[i] for i in [13, 10, 7]) == ['O','O','O'] 
    ):
        global winning
        winning = 2
    else: 
        pass
    
# merging all together
def play_game():
    while winning == 0: 
        intake()
        play()
        opponent_play()
        game_print()
        print("\n")
        winner()
        loser()
    if winning == 1:
        print("Congratulations, you won!")
    if winning == 2:
        print("You lost. Better luck next time!")
        
# adding a replay function
def tictactoe():
    print("You start")
    global game
    game = game_orig.copy()
    global winning
    winning = 0
    while True:    
        play_game()

        play_again = input('Do you want a rematch? y/n: ') == 'y'
        
        if play_again:
            winning = 0
            game = game_orig.copy()
        if not play_again:
            return  
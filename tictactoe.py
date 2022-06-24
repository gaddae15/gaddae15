from tkinter import *
import random

Player1 = "X"
Player2 = "O"
players = [Player1, Player2]
player = random.choice(players)

# Go to next turn function


def next_turn(row, column):

    global player  # initialize global variable player
    # Check If the clicked button is empty and there is no winner yet
    if buttons[row][column]['text'] == "" and not check_winner():
        # Check if the player is the first in the players list, If yes
        if player == players[0]:
            # Replace empty button with player name(X)
            buttons[row][column]['text'] = player
            # Check if there is a winner
            # If not
            if not check_winner():
                # It is the next player O's turn
                player = players[1]
                label.config(text=("Player 2's Turn"))
            # If yes
            elif check_winner() == True:
                # Display X wins and Turn the O Squares red
                turning_red(0)
                label.config(text=("Player 1 Wins!"))
            # If it is a tie
            elif check_winner() == "Draw":
                # Display that it is a tie
                label.config(text="Draw!")
        # If player is not the first in the list:
        else:
            # Replace empty button with player name(O)
            buttons[row][column]['text'] = player
            # Check if there is a winner
            # If not
            if not check_winner():
                # It is the next player X's turn
                player = players[0]
                label.config(text=("Player 1's Turn"))
            # If yes, Display O wins and Turn the X squares red
            elif check_winner() == True:
                turning_red(1)
                label.config(text=("Player 2 Wins"))
            # Display Draw if it is a tie
            elif check_winner() == "Draw":
                label.config(text="Draw!")


# Check if there is a winner function
def check_winner():
    # Check if any of the rows has all 3 buttons with the same value.
    # If that is the case, change the colour of all those buttons to green and return True
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    # Check if any of the columns has all 3 buttons with the same value.
    # If that is the case, change the colour of all those buttons to green and return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    # Check if any of the diagonals has all 3 buttons with the same value.
    # If that is the case, change the colour of all those buttons to green and return True for each diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    # Check if there are any empty spaces left
    # If there aren't any then it is a tie.
    # Change the colour of all buttons in the grid to orange
    elif not empty_spaces():

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="orange")
        return "Draw"
    # Else return false
    else:

        return False

# Check if there are empty spaces fucntion definition


def empty_spaces():
    # Initialize original number of spaces
    spaces = 9
    # Check if the are any buttons that contan X or O and subtract the number from the spaces variable
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    # Return False if Spaces are 0 else keep returning True till they are 0
    if spaces == 0:
        return False
    else:
        return True

# Turn the loser's answers red function


def turning_red(index):
    # Locate all the buttons that were not filled with the winner's value(X or O) and turn them red
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != players[index]:
                buttons[row][column].config(bg="red")
                buttons[row][column].config(bg="red")
                buttons[row][column].config(bg="red")

# Reset the game function


def new_game():

    global player
    # Pick a player and random at the start of the game
    label.config(text=player+" Starts")
    # Chnage the button conditions back to empty and colourless at start of new game
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


# Assign tkinter to window
window = Tk()
# Give the window the title Tic-Tac-Toe
window.title("Tic-Tac-Toe")
# Initialize the variable buttons for the 3x3 grid
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
# At start of game, state the player to start
label = Label(text=player + " Starts", font=('consolas', 40))
label.pack(side="top")
# Create a reset button to reset the game when it ends
reset_button = Button(text="RESET", font=('consolas', 20), command=new_game)
reset_button.pack(side="bottom")

# Create the game area in a frame
# Create 3 rows and 3 columns in a grid
# Make each cell of the 3x3, an empty button of width 5 and height 2
# Assign a lambda function to each button, to move to the next turn when the button is pressed
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 30), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()

import random
class MyBattleship:
    """
    This class holds all the code for the battleship game
    """
    #define a board attribute with an empty list
    board=[]
    def __init__(self):
        """
        This is the class constructor method for
        initializing the game board and also
        for calling defined class methods
        """
        for b in range(10):
            self.board.append(["0"]*10)
        self.display_board()
        self.play_game()

    def display_board(self):
        """
        This method displays the game board
        with the values in the board list
        """
        v=0
        print("  0 1 2 3 4 5 6 7 8 9 ")
        for row in self.board:
            print(v, " ".join(row))
            v+=1
    def random_row(self):
        """
        Generate random value for the board row
        """
        return random.randint(0, 2)

    def random_column(self):
        """
        Generate random value for the game column
        """
        return random.randint(0, 2)

    def play_game(self):
        """
        This method contains the logic for the user to play
        the battleship game
        """
        for play in range(10):
            
            random_r=self.random_row()
            random_c=self.random_column()
            guess_row=int(input("Guess_Row:"))
            guess_column=int(input("Guess_Column:"))
            if guess_row==random_r and guess_column==random_c:
                print("Congrats! You hit the ship.\n")
                print("You Won! Begin new game")
                break;
            else:
                if (guess_row<0 or guess_row>9) or (guess_column<0 or guess_column>9):
                    print("Sorry your guess was out of range")
                elif(self.board[guess_row][guess_column]=="X"):
                    print("You have already guessed that before")
                else:
                    print("Sorry. You missed your hit")
                    self.board[guess_row][guess_column]=="X"
                    print(play+1)
                    self.display_board()



    

print("Welcome to the Battleship Game")
battleship_game=MyBattleship()


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

battleship_game=MyBattleship()

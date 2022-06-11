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

battleship_game=MyBattleship()

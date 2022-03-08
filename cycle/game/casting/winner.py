import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Winner(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Winner is to keep track of who has won the game. Client should use get_text() to get a string 
    representation of who is currently winning.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._winner = ""
        

    def declare_winner(self, winner):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._winner = winner
        self.set_text(f"Winner: {self._winner}")

        x = int((constants.MAX_X / 2) - 43)
        y = int((constants.MAX_Y / 2) + 30) 
        self._position = Point(x, y)
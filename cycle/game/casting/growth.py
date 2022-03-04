from game.casting.actor import Actor


class Growth(Actor):
    """
    A tasty item that snakes like to eat.
    
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "initializes count to add a segment to tail in increments"
        super().__init__()
        self._count = 0       

    def _handle_growth(self, cast):
        """Grows the cycle at an increment of 5.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._count += 1
        

        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]

        
        if (self._count % 5) == 0:
            cycle1.grow_tail(1)
            cycle2.grow_tail(1)
        
        # if head.get_position().equals(food.get_position()):
        #     points = food.get_points()
        #     snake.grow_tail(points)
        #     score.add_points(points)
        #     food.reset()
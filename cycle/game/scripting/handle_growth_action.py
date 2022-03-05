# from game.casting.actor import Actor
from game.scripting.action import Action


class HandleGrowthAction(Action):
    """
    An update action that handles the growth of the segments of the cycles.
    
    The responsibility of HandleGrowthAction is to handle the growth of the segments
    of the cycles as the update actions execute.
    
    Attributes:
        _self._count (int): The number of counts.
    """
    def __init__(self):
        "initializes count to add a segment to tail in increments"
        self._count = 0       

    def execute(self, cast, script):
        """Grows the cycle at an increment of 40 execute update actions.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._count += 1
        
        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        
        if (self._count % 40) == 0:
            cycle1.grow_tail(1)
            cycle2.grow_tail(1)

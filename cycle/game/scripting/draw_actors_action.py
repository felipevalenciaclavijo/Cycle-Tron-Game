from game.scripting.action import Action
from game.casting.growth import Growth


class DrawActorsAction(Action, Growth):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        # snake = cast.get_first_actor("snakes")
        # segments = snake.get_segments()

        cast._handle_growth(cast)

        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        cycle1_segments = cycle1.get_segments()
        cycle2_segments = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food)
        # self._video_service.draw_actors(segments)
        self._video_service.draw_actors(cycle1_segments)
        self._video_service.draw_actors(cycle2_segments)
        # on the example he had this three times and I think it might have been an error...
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
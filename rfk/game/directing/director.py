from game.casting.gem import Gem
from game.casting.rock import Rock

CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._points = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()


    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        
   

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        actors = cast.get_all_actors()
        # banner.set_text(f"You have {points} points")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        gem = cast.get_actors("gems")
        rock = cast.get_actors("rocks")
        
        for actor in actors:
            actor.move_next(max_x, max_y)
        
        for gem in gem:  
            if robot.get_position().equals(gem.get_position()):
                self._points += 1
                banner.set_text(f"You have {self._points} points")
                cast.remove_actor("gems", gem)
                gem = Gem(COLS, CELL_SIZE, FONT_SIZE, 1)
                cast.add_actor("gems", gem)

                
        
        for rock in rock:  
            if robot.get_position().equals(rock.get_position()):
                self._points -= 1
                banner.set_text(f"You have {self._points} points")
                cast.remove_actor("rocks", rock)
                rock = Rock(COLS, CELL_SIZE, FONT_SIZE, 1)
                cast.add_actor("rocks", rock)
           
  
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
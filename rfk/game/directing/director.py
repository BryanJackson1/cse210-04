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
        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        gem = cast.get_actors("gems")
        rock = cast.get_actors("rocks")
        
        for actor in actors:
            actor.move_next(max_x, max_y)

            if actor._position.get_y() == max_y:
                cast.remove_actor(cast, actor)

    """for gem in gems:  #Maybe rework this for the scoring detection.
        
        for gem in gem:  #Maybe rework this for the scoring detection.
            if robot.get_position().equals(gem.get_position()):
                message = "You got 1 point!"
                banner.set_text(message) 
        """     
        
        for rock in rock:  #Maybe rework this for the scoring detection.
            if robot.get_position().equals(rock.get_position()):
                message = "You lost 1 points"
                banner.set_text(message)
           
  
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
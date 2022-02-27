from game.casting.actor import Actor
from game.shared.point import Point



class Rock(Actor):
    """
    A destructive actor. Subtracts one from the player when hit

    Attributes:
        character velocity and score
    """
    def __init__(self):
        """define properties. Will need score, velocity, and character"""
        self._text = "O"
        self._cell_size = 1
        

    def get_velocity(self):
        direction = Point(0,1)
        direction = direction.scale(self._cell_size)
        return direction

    def get_velocity2(self):
        direction = Point(0, 3)
        direction = direction.scale(self._cell_size)
        return direction

    def get_velocity3(self):
        direction = Point(0, 5)
        direction = direction.scale(self._cell_size)
        return direction

    def get_text(self):
        return self._text
        

        
    
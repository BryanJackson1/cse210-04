from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    """
    An item of value. 
    
    The responsibility of an gem is to provide a positive value.

    Attributes:
        _message (string): A short description about the gem.
    """
    def __init__(self):
        """define properties"""
        self._text = "O"
        self._cell_size = 1

    def get_velocity(self):
        direction = Point(0, -1)
        direction = direction.scale(self._cell_size)
        return direction

        

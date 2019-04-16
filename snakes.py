class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def __init__(self):
        self.likes_music = True
        self.likes_to_dance = True
        self.wears_sombreros = True
    
    def bite(self, other):
        """Deliver a dose of venom."""
        print('You\'ve been bitten by a deadly cobra snake. Ow.')

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        print('Hrrrnnggraaawrrr!!!!')

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"

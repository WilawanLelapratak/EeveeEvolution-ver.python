import arcade.key
from random import randint, random

class Eevee :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def animate(self, delta) :
        if self.y > 600 :
            self.y = 0
        self.y += 5

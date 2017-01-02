import arcade.key
from random import randint, random

class Eevee :
    def __init__(self, world, x, y) :
        self.world = world
        self.x = x
        self.y = y

    def animate(self, delta) :
        if self.y > self.world.height :
            self.y = 0
        self.y += 5

class World :
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.eevee = Eevee(self, 100, 100)

    def animate(self, delta) :
        self.eevee.animate(delta)

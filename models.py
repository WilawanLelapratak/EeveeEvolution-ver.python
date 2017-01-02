import arcade.key
from random import randint, random

class Eevee :
    DIR_RIGHT = 0
    DIR_UP = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Eevee.DIR_RIGHT

    def switch_direction(self):
        if self.direction == Eevee.DIR_RIGHT:
            self.direction = Eevee.DIR_UP
        else:
            self.direction = Eevee.DIR_RIGHT

    def animate(self, delta):
        if self.direction == Eevee.DIR_UP:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5

class Candy :
    def __init__(self, world, x, y) :
        self.world = world
        self.x = x
        self.y = y

class World :
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.eevee = Eevee(self, 100, 100)
        self.candy = Candy(self, 400, 400)

    def animate(self, delta) :
        self.eevee.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.eevee.switch_direction()

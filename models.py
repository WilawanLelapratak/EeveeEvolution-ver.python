import arcade.key
from random import randint, random

class Model :
    def __init__(self, world, x, y, angle) :
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Meow(Model) :
    def __init__(self, world, x, y, vx, vy) :
        super().__init__(world, x, y, 0)
        self.vx = vx
        self.vy = vy
        self.angle = randint(0,359)

    def random_direction(self):
        self.vx = 5 * random()
        self.vy = 5 * random()

    def animate(self, delta):
        if (self.x < 0) or (self.x > self.world.width):
            self.vx = - self.vx

        if (self.y < 0) or (self.y > self.world.height):
            self.vy = - self.vy

        self.x += self.vx
        self.y += self.vy
        self.angle += 3


class Eevee(Model) :
    DIR_RIGHT = 0
    DIR_UP = 1

    def __init__(self, world, x, y):
        super().__init__(world, x,y, 0)
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

class Candy(Model) :
    def __init__(self, world, x, y) :
        super().__init__(world, x, y, 0)

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)

class World :
    NUM_MEOW = 3

    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.gameset()

    def gameset(self) :
        self.score = 0
        self.eevee = Eevee(self, 100, 100)
        self.candy = Candy(self, 400, 400)
        self.game_over = False
        self.meows = []
        for i in range(World.NUM_MEOW):
            meow = Meow(self, 0, 0, 0, 0)
            meow.random_direction()
            self.meows.append(meow)

    def animate(self, delta) :
        self.eevee.animate(delta)

        if self.eevee.hit(self.candy, 25) :
            self.candy.random_location()
            self.score += 1

        for meow in self.meows :
            meow.animate(delta)

            if self.eevee.hit(meow, 20) :
                self.game_over = True

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.eevee.switch_direction()

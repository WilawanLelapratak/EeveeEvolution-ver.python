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
        if (self.x < 30) or (self.x > (self.world.width -30)):
            self.vx = - self.vx

        if (self.y < 38) or (self.y > (self.world.height - 38)):
            self.vy = - self.vy

        self.x += self.vx
        self.y += self.vy
        self.angle += 3


class Eevee(Model) :

    def __init__(self, world, x, y) :
        super().__init__(world, x,y, 0)
        self.x = x
        self.y = y
        self.left_right = 0
        self.up_down = 0
        self.speed = 5

    def start_moving(self, key) :
        if key == arcade.key.UP :
            self.up_down = 1
        if key == arcade.key.DOWN :
            self.up_down = -1
        if key == arcade.key.RIGHT :
            self.left_right = 1
        if key == arcade.key.LEFT :
            self.left_right = -1

    def stop_moving(self, key) :
        if key in [arcade.key.UP, arcade.key.DOWN] :
            self.up_down = 0
        if key in [arcade.key.LEFT, arcade.key.RIGHT] :
            self.left_right = 0

    def animate(self, delta) :
        self.x += self.speed * self.left_right
        self.y += self.speed * self.up_down
        self.stay_in_frame()

    def stay_in_frame(self) :
        if self.x < 35 :
            self.x = 35
        if self.x > self.world.width - 35 :
            self.x = self.world.width - 35
        if self.y < 35 :
            self.y = 35
        if self.y > self.world.height - 35 :
            self.y = self.world.height - 35

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
        self.eevee = Eevee(self, 200, 200)
        self.candy = Candy(self, 400, 400)
        self.game_over = False
        self.meows = []
        for i in range(World.NUM_MEOW):
            meow = Meow(self, 30, 38, 0, 0)
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

    def on_key_press(self, key, key_modifiers) :
        self.eevee.start_moving(key)

    def on_key_release(self, key, key_modifiers) :
        self.eevee.stop_moving(key)

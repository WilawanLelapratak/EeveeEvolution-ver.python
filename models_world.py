import arcade
from models import Eevee, Meow, Candy, Stone

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
        self.stone = Stone(self, -50, -50)
        self.is_stone = False
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

        if self.score % 5 == 0 and not self.is_stone and self.score != 0 :
            self.stone.random_stone_type()
            self.stone.random_location()
            self.is_stone = True

        if self.eevee.hit(self.stone, 25) :
            self.stone.set_out_of_frame();
            self.is_stone = False

        for meow in self.meows :
            meow.animate(delta)

            if self.eevee.hit(meow, 20) :
                self.game_over = True

    def on_key_press(self, key, key_modifiers) :
        self.eevee.start_moving(key)

    def on_key_release(self, key, key_modifiers) :
        self.eevee.stop_moving(key)

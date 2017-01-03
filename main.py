import arcade
from models import Eevee,World

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite) :
    def __init__(self, *args, **kwargs) :
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self) :
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self) :
        self.sync_with_model()
        super().draw()

class EeveeGameWindow(arcade.Window) :
    def __init__(self, width, height) :
        super().__init__(width, height)
        self.world = World(width, height)
        self.gameset()

    def gameset(self) :
        self.image = arcade.load_texture('desertbg.png')
        self.eevee_sprite = ModelSprite('eevee.png', model = self.world.eevee)
        self.candy_sprite = ModelSprite('Caandyy.png', model = self.world.candy)
        self.meow_sprites = []
        for meow in self.world.meows :
            self.meow_sprites.append(ModelSprite('meow.png', model = meow))

    def on_draw(self) :
        arcade.start_render()
        arcade.draw_texture_rectangle(300, 300, SCREEN_WIDTH, SCREEN_HEIGHT,self.image)
        if self.world.game_over :
            arcade.draw_text("Game Over", 210, self.height/2 + 30, arcade.color.BLACK, 30)
            arcade.draw_text("Press Space Bar to Continue", 150, self.height/2 - 30, arcade.color.BLACK, 20)
        self.eevee_sprite.draw()
        self.candy_sprite.draw()
        for sprite in self.meow_sprites :
            sprite.draw()
        arcade.draw_text(str(self.world.score), self.width -60, self.height - 30, arcade.color.BLACK, 20)

    def animate(self, delta) :
        if not self.world.game_over :
            self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if self.world.game_over and key == arcade.key.SPACE :
            self.world.gameset()
            self.gameset()
            self.world.game_over = False
        elif not self.world.game_over :
            self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__' :
    window = EeveeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

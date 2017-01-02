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
        self.image = arcade.load_texture('desertbg.png')
        self.world = World(width, height)
        self.eevee_sprite = ModelSprite('eevee.png', model = self.world.eevee)
        self.candy_sprite = ModelSprite('Caandyy.png', model = self.world.candy)

    def on_draw(self) :
        arcade.start_render()
        arcade.draw_texture_rectangle(300, 300, SCREEN_WIDTH, SCREEN_HEIGHT,self.image)
        self.eevee_sprite.draw()
        self.candy_sprite.draw()

    def animate(self, delta) :
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__' :
    window = EeveeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

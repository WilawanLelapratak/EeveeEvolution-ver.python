import arcade
from models import Eevee,World

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class EeveeGameWindow(arcade.Window) :
    def __init__(self, width, height) :
        super().__init__(width, height)
        self.image = arcade.load_texture('desertbg.png')
        self.eevee_sprite = arcade.Sprite('eevee.png')
        self.world = World(width, height)

    def on_draw(self) :
        arcade.start_render()
        arcade.draw_texture_rectangle(300, 300, SCREEN_WIDTH, SCREEN_HEIGHT,self.image)
        self.eevee_sprite.draw()

    def animate(self, delta) :
        self.world.animate(delta)
        self.eevee_sprite.set_position(self.world.eevee.x, self.world.eevee.y)

if __name__ == '__main__' :
    window = EeveeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

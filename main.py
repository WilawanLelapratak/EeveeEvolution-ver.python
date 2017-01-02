import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class EeveeGameWindow(arcade.Window) :
    def __init__(self, width, height) :
        super().__init__(width, height)
        self.image = arcade.load_texture('desertbg.png')

    def on_draw(self) :
        arcade.start_render()
        arcade.draw_texture_rectangle(300, 300, SCREEN_WIDTH, SCREEN_HEIGHT,self.image)

if __name__ == '__main__' :
    window = EeveeGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

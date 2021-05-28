"""
  Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 944
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Platformer"
CHARACTER_SCALING = 1

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 192
        self.player_list.append(self.player_sprite)

        # add map to game
        my_map = arcade.tilemap.read_tmx("my_map1.tmx")
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name="ground")
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



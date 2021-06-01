"""
  Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 944
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Platformer"
SPRITE_PIXEL_SIZE = 128
TILE_SCALING = 0.5
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement of player
CHARACTER_SCALING = 1
MOVEMENT_SPEED = 3
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Position of player
PLAYER_START_X = 256
PLAYER_START_Y = 192


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        # Add physics engine
        self.physics_engine = None

        self.end_of_map = 0
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()

        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # add map to game
        my_map = arcade.tilemap.read_tmx("my_map1.tmx")
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name="ground")
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # cut the right side of map
        self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                # play sound

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        # Move the player with the physics engine
        self.physics_engine.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



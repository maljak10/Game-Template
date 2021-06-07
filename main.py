"""
  Platformer Game
"""
import arcade
import time
import sys

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Platformer"
SPRITE_PIXEL_SIZE = 128

# Movement of player
MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Position of player
PLAYER_START_X = 256
PLAYER_START_Y = 192

# Viewpoint margin
LEFT_VIEWPORT_MARGIN = 300
RIGHT_VIEWPORT_MARGIN = 900
TOP_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 150


class GameMenu(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture(f"png_ground/BG/BG.png"))
        arcade.draw_text("Press ENTER to select the level or I for instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            game_view = LevelSelect()
            self.window.show_view(game_view)
        elif key == arcade.key.I:
            instructions_view = Instructions()
            self.window.show_view(instructions_view)


class LevelSelect(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture(f"png_ground/BG/BG.png"))
        arcade.draw_text("SELECT THE LEVEL. PRESS KEY ON YOUR KEYBOARD", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("ESC TO BACK TO MENU", SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.KEY_1:
            game_view = MyGame()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.KEY_2:
            game_view = MyGame()
            game_view.level = 2
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            title_view = GameMenu()
            self.window.show_view(title_view)


class Instructions(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture(f"png_ground/BG/BG.png"))
        arcade.draw_text("Collect coins and find the exit! Use arrow keys to run and space bar for jump.",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Press escape to return to the menu",
                         SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6, arcade.color.BLACK, font_size=30, align="right")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            title_view = GameMenu()
            self.window.show_view(title_view)


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

        self.fill_color = arcade.make_transparent_color(arcade.color.WHITE, transparency=150)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(
            left=self.game_view.view_left,
            right=self.game_view.view_left + SCREEN_WIDTH,
            top=self.game_view.view_bottom + SCREEN_HEIGHT,
            bottom=self.game_view.view_bottom,
            color=self.fill_color,
        )
        arcade.draw_text("PAUSED, PRESS P TO RESUME", self.game_view.view_left + 100, self.game_view.view_bottom + 600,
                         arcade.color.YELLOW_ROSE, font_size=50, align="center")
        arcade.draw_text("TO BACK TO MENU PRESS ESC", self.game_view.view_left + 100, self.game_view.view_bottom + 200,
                         arcade.color.YELLOW_ROSE, font_size=50, align="right")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.P:
            self.window.show_view(self.game_view)
        elif key == arcade.key.ESCAPE:
            title_view = GameMenu()
            self.window.show_view(title_view)
            arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)


class ScoreTable(arcade.View):
    pass


class GameOver(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.fill_color = arcade.make_transparent_color(arcade.color.WHITE, transparency=10)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(
            left=self.game_view.view_left,
            right=self.game_view.view_left + SCREEN_WIDTH,
            top=self.game_view.view_bottom + SCREEN_HEIGHT,
            bottom=self.game_view.view_bottom,
            color=self.fill_color,
        )
        arcade.draw_text("GAME OVER", self.game_view.view_left + 200, self.game_view.view_bottom + 200,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            self.game_view.player_sprite.change_x = 0
            self.game_view.player_sprite.change_y = 0
            self.game_view.return_to_start()
            self.game_view.life = 3
            self.game_view.score = 0
            self.window.show_view(self.game_view)
            arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)
        elif key == arcade.key.ESCAPE:
            title_view = GameMenu()
            self.window.show_view(title_view)
            arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)


class Congrats(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_draw(self):
        self.game_view.on_draw()
        arcade.draw_text("CONGRATULATION", self.game_view.view_left + 100, self.game_view.view_bottom + 600,
                         arcade.color.YELLOW_ROSE, font_size=50, align="center")
        arcade.draw_text("TO NEXT LEVEL PRESS ENTER", self.game_view.view_left + 100, self.game_view.view_bottom + 400,
                         arcade.color.YELLOW_ROSE, font_size=30, align="right")
        arcade.draw_text("TO BACK TO MENU PRESS ESC", self.game_view.view_left + 100, self.game_view.view_bottom + 200,
                         arcade.color.YELLOW_ROSE, font_size=30, align="right")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            title_view = GameMenu()
            self.window.show_view(title_view)
            arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)

        elif key == arcade.key.ENTER:
            arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)
            self.game_view.level += 1
            self.game_view.score = 0
            self.game_view.life = 3
            self.game_view.setup()
            self.window.show_view(self.game_view)


class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.background = None
        self.foreground = None
        self.goal = None
        self.moving = None
        self.pins = None

        # Set up the player
        self.player_sprite = None

        # Add physics engine
        self.physics_engine = None

        # self.back = None
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.end_of_map = 0
        self.view_left = 0
        self.view_bottom = 0
        self.score = 0
        self.level = 1
        self.life = 3

        # sounds
        self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.lost_life_sound = arcade.load_sound(":resources:sounds/hit4.wav")
        self.finish_level_sound = arcade.load_sound(":resources:sounds/upgrade1.wav")
        self.game_over_sound = arcade.load_sound(":resources:sounds/hit4.wav")

        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None

    def advance_song(self):
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0

    def play_song(self):
        # stop currently playing
        if self.music:
            self.music.stop(self.current_player)

        # play next song
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(volume=0.1, loop=True)
        time.sleep(0.03)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Reset the viewport
        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        # if not self.player_sprite:
        self.player_sprite = self.create_player_sprite()
        self.player_list.append(self.player_sprite)

        # add map to game
        my_map = arcade.tilemap.read_tmx(f"my_map{self.level}.tmx")
        self.background = arcade.tilemap.process_layer(map_object=my_map, layer_name="background", scaling=0.7)
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name="ground", scaling=0.7)
        self.pins = arcade.tilemap.process_layer(map_object=my_map, layer_name="don'touch", scaling=0.7)
        self.goal = arcade.tilemap.process_layer(map_object=my_map, layer_name="goal", scaling=0.7)
        self.foreground = arcade.tilemap.process_layer(map_object=my_map, layer_name="foreground", scaling=0.7)
        self.moving = arcade.tilemap.process_layer(map_object=my_map, layer_name="moving-platform", scaling=0.7)
        self.coin_list = arcade.tilemap.process_layer(map_object=my_map, layer_name="collectable", scaling=0.7)

        for sprite in self.moving:
            self.wall_list.append(sprite)

        self.end_of_map = my_map.map_size.width
        self.map_width = (my_map.map_size.width - 1) * my_map.tile_size.width

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

        # Setup music
        self.music_list = ["sounds/childish_theme.WAV", "sounds/sky_loop.WAV"]
        self.current_song_index = 0
        self.play_song()

        # Move the player sprite back to the beginning
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y

    def create_player_sprite(self) -> arcade.AnimatedWalkingSprite:
        """Creates the animated player sprite

        Returns:
            The properly set up player sprite
        """
        # Where are the player images stored?
        texture_path = ":resources:images/animated_characters/female_adventurer/"

        # Set up the appropriate textures
        walking_paths = [texture_path + f"femaleAdventurer_walk{x}.png" for x in range(0, 7)]
        standing_path = texture_path + "femaleAdventurer_idle.png"
        jumping_path = texture_path + "femaleAdventurer_jump.png"

        # Load them all now
        walking_right_textures = [arcade.load_texture(texture) for texture in walking_paths]
        walking_left_textures = [arcade.load_texture(texture, mirrored=True) for texture in walking_paths]

        standing_right_textures = [arcade.load_texture(standing_path)]
        standing_left_textures = [arcade.load_texture(standing_path, mirrored=True)]

        jumping_right_textures = [arcade.load_texture(jumping_path)]
        jumping_left_textures = [arcade.load_texture(jumping_path, mirrored=True)]

        # Create the sprite
        player = arcade.AnimatedWalkingSprite(scale=0.8)

        # Add the proper textures
        player.stand_left_textures = standing_left_textures
        player.stand_right_textures = standing_right_textures
        player.walk_left_textures = walking_left_textures
        player.walk_right_textures = walking_right_textures
        player.jumping_right_textures = jumping_right_textures
        player.jumping_left_textures = jumping_left_textures

        # Move the player sprite back to the beginning
        player.center_x = PLAYER_START_X
        player.center_y = PLAYER_START_Y
        player.state = arcade.FACE_RIGHT

        # Set the initial texture
        player.texture = player.stand_right_textures[0]

        return player

    def scroll_viewport(self) -> None:
        """Scrolls the viewport when the player gets close to the edges"""
        change_viewport = False
        # Scroll left
        # Find the current left boundary
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN

        # Are we to the left of this boundary? Then we should scroll left.
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            change_viewport = True
            # But don't scroll past the left edge of the map
            if self.view_left < 0:
                self.view_left = 0

        # Scroll right
        # Find the current right boundary
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN

        # Are we to the right of this boundary? Then we should scroll right.
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            change_viewport = True
            # Don't scroll past the right edge of the map
            if self.view_left > self.map_width - SCREEN_WIDTH:
                self.view_left = self.map_width - SCREEN_WIDTH

        self.view_bottom = int(self.view_bottom)
        self.view_left = int(self.view_left)

        # Do the scrolling
        if change_viewport:
            arcade.set_viewport(
                left=self.view_left,
                right=SCREEN_WIDTH + self.view_left,
                bottom=self.view_bottom,
                top=SCREEN_HEIGHT + self.view_bottom,
            )

    def draw_life_counter(self):
        life = self.life
        life_table = [150, 200, 250]
        if life == 3:
            for l in life_table:
                arcade.draw_texture_rectangle(l + self.view_left, 570 + self.view_bottom,
                                              SCREEN_WIDTH / 20, SCREEN_HEIGHT / 15,
                                              arcade.load_texture("images/HUD/hudHeart_full.png"))
        elif life == 2:
            for l in life_table[:-1]:
                arcade.draw_texture_rectangle(l + self.view_left, 570 + self.view_bottom,
                                              SCREEN_WIDTH / 20, SCREEN_HEIGHT / 15,
                                              arcade.load_texture("images/HUD/hudHeart_full.png"))
            arcade.draw_texture_rectangle(life_table[2] + self.view_left, 570 + self.view_bottom,
                                          SCREEN_WIDTH / 20, SCREEN_HEIGHT / 15,
                                          arcade.load_texture("images/HUD/hudHeart_empty.png"))
        elif life == 1:
            arcade.draw_texture_rectangle(life_table[0] + self.view_left, 570 + self.view_bottom,
                                          SCREEN_WIDTH / 20, SCREEN_HEIGHT / 15,
                                          arcade.load_texture("images/HUD/hudHeart_full.png"))
            for l in life_table[1:]:
                arcade.draw_texture_rectangle(l + self.view_left, 570 + self.view_bottom,
                                              SCREEN_WIDTH / 20, SCREEN_HEIGHT / 15,
                                              arcade.load_texture("images/HUD/hudHeart_empty.png"))

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # self.back = arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
        #                                                 arcade.load_texture(f"png_ground/BG/BG.png"))
        self.background.draw()
        self.wall_list.draw()
        self.pins.draw()
        self.goal.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.foreground.draw()
        score_text = f"Score: {self.score}"
        level_text = f"Level: {self.level}"
        arcade.draw_text(level_text, start_x=10 + self.view_left, start_y=570 + self.view_bottom,
                         color=arcade.csscolor.DARK_ORANGE, font_size=20)
        arcade.draw_text(score_text, start_x=10 + self.view_left,
                         start_y=540 + self.view_bottom, color=arcade.csscolor.GOLD, font_size=20)
        self.draw_life_counter()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.P:
            pause = PauseView(self)
            self.window.show_view(pause)
        elif key == arcade.key.Q:
            sys.exit()

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

        if self.player_sprite.center_y < -100:
            self.life_check()

        self.scroll_viewport()
        self.player_sprite.update_animation(delta_time)
        self.wall_list.update()

        for wall in self.wall_list:
            if wall.boundary_right and wall.right > wall.boundary_right and wall.change_x > 0:
                wall.change_x *= -1
            elif wall.boundary_left and wall.left < wall.boundary_left and wall.change_x < 0:
                wall.change_x *= -1
            elif wall.boundary_top and wall.top > wall.boundary_top and wall.change_y > 0:
                wall.change_y *= -1
            elif wall.boundary_bottom and wall.bottom < wall.boundary_bottom and wall.change_y < 0:
                wall.change_y *= -1

        collected_coins = arcade.check_for_collision_with_list(
            sprite=self.player_sprite, sprite_list=self.coin_list
        )

        for coin in collected_coins:
            # Add the coin score to our score
            self.score += 1
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()

        goals_hit = arcade.check_for_collision_with_list(
            sprite=self.player_sprite, sprite_list=self.goal
        )

        if goals_hit:
            bravo = Congrats(self)
            self.window.show_view(bravo)
            arcade.play_sound(self.finish_level_sound)

        if arcade.check_for_collision_with_list(self.player_sprite, self.pins):
            self.life_check()

    def return_to_start(self):
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.view_left = 0
        self.view_bottom = 0

    def life_check(self):
        if self.life >= 2:
            self.life -= 1
            self.draw_life_counter()
            arcade.play_sound(self.game_over_sound)
            self.return_to_start()
        elif self.life == 1:
            self.window.show_view((GameOver(self)))
            arcade.play_sound(self.game_over_sound)


def main():
    " "" Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameMenu()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()

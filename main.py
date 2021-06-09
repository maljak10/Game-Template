"""
    Adventure Jungle
    Simple Platformer Game
"""
import arcade
import time

# Constants
SCREEN_WIDTH = 800
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
RIGHT_VIEWPORT_MARGIN = 300
TOP_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 150

BUTTONS = {
    'big_left': [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
                 SCREEN_WIDTH / 10, SCREEN_HEIGHT / 9, "arcade.close_window()"],
    'big_right': [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
                  SCREEN_WIDTH / 1.1, SCREEN_HEIGHT / 9, "self.window.show_view(LevelSelect())"],
    'author': [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
               SCREEN_WIDTH / 15, SCREEN_HEIGHT / 1.05, "self.window.show_view(Author())"],
    'instruction': [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
                    SCREEN_WIDTH / 1.07, SCREEN_HEIGHT / 1.05, "self.window.show_view(Instructions())"],
    'scores': [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
               SCREEN_WIDTH / 1.2, SCREEN_HEIGHT / 1.05, "self.window.show_view(ScoreTable())"],
    'first_level': [arcade.load_texture("images/HUD/hud1.png"),
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.64],
    'second_level': [arcade.load_texture("images/HUD/hud2.png"),
                     SCREEN_WIDTH / 1.2, SCREEN_HEIGHT / 1.5],
    'escape_level': [arcade.load_texture("images/HUD/hudX.png"),
                     SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2.5],
    'menu': [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
             SCREEN_WIDTH / 10, SCREEN_HEIGHT / 9, "self.window.show_view(GameMenu())"]
}


class GameMenu(arcade.View):
    def __init__(self):
        super().__init__()

        # sounds
        self.menu_select = arcade.load_sound("sounds/menu_selection_click.wav")


    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("png_ground/BG/BG.png"))
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("images/game_menu.png"))
        arcade.draw_text("ADVENTURE JUNGLE", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3,
                         arcade.color.ORANGE_PEEL, font_size=40, anchor_x="center")
        self.draw_control_buttons()

    def draw_control_buttons(self):
        arcade.draw_scaled_texture_rectangle(BUTTONS['big_left'][1], BUTTONS['big_left'][2],
                                             BUTTONS['big_left'][0], scale=1.4)
        arcade.draw_scaled_texture_rectangle(BUTTONS['big_right'][1], BUTTONS['big_right'][2],
                                             BUTTONS['big_right'][0], scale=1.4)
        arcade.draw_text("EXIT", SCREEN_WIDTH / 10, SCREEN_HEIGHT / 10,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("SELECT LEVEL", SCREEN_WIDTH / 1.1, SCREEN_HEIGHT / 10,
                         arcade.color.BLACK, font_size=17, anchor_x="center")

        arcade.draw_scaled_texture_rectangle(BUTTONS['author'][1], BUTTONS['author'][2],
                                             BUTTONS['author'][0], scale=0.7)
        arcade.draw_scaled_texture_rectangle(BUTTONS['instruction'][1], BUTTONS['instruction'][2],
                                             BUTTONS['instruction'][0], scale=0.7)
        arcade.draw_scaled_texture_rectangle(BUTTONS['scores'][1], BUTTONS['scores'][2],
                                             BUTTONS['scores'][0], scale=0.7)
        arcade.draw_text("?", BUTTONS['instruction'][1], BUTTONS['instruction'][2] - 15,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Scores", BUTTONS['scores'][1], BUTTONS['scores'][2] - 5,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("A", BUTTONS['author'][1], BUTTONS['author'][2] - 15,
                         arcade.color.BLACK, font_size=25, anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        button_list = [BUTTONS['big_left'], BUTTONS['big_right'],
                       BUTTONS['instruction'], BUTTONS['scores'], BUTTONS['author']]
        self.eval_button(x, y, button_list)
        arcade.play_sound(self.menu_select)

    def eval_button(self, x, y, button_list):
        for i in button_list:
            texture = i[0]
            w = i[1]
            h = i[2]
            if w - texture.width // 2 <= x <= w + texture.width // 2:
                if h - texture.height // 2 <= y <= h + texture.height // 2:
                    eval(i[3])


class LevelSelect(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_select = arcade.load_sound("sounds/menu_selection_click.wav")

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("png_ground/BG/BG.png"))
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("images/level_select.png"))
        arcade.draw_text("SELECT THE LEVEL", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

        arcade.draw_scaled_texture_rectangle(BUTTONS['first_level'][1], BUTTONS['first_level'][2],
                                             BUTTONS['first_level'][0], scale=0.7)
        arcade.draw_scaled_texture_rectangle(BUTTONS['second_level'][1], BUTTONS['second_level'][2],
                                             BUTTONS['second_level'][0], scale=0.7)
        arcade.draw_scaled_texture_rectangle(BUTTONS['escape_level'][1], BUTTONS['escape_level'][2],
                                             BUTTONS['escape_level'][0], scale=0.7)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.play_sound(self.menu_select)
        button_list = [BUTTONS['first_level'], BUTTONS['second_level'], BUTTONS['escape_level']]
        for i in button_list:
            texture = i[0]
            w = i[1]
            h = i[2]
            if w - texture.width // 2 <= x <= w + texture.width // 2:
                if h - texture.height // 2 <= y <= h + texture.height // 2:
                    if i == BUTTONS['first_level']:
                        game_view = MyGame()
                        game_view.setup()
                        self.window.show_view(game_view)
                    elif i == BUTTONS['second_level']:
                        game_view = MyGame()
                        game_view.level = 2
                        game_view.setup()
                        self.window.show_view(game_view)
                    elif i == BUTTONS['escape_level']:
                        self.window.show_view(GameMenu())


class Instructions(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_select = arcade.load_sound("sounds/menu_selection_click.wav")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("png_ground/BG/BG.png"))
        arcade.draw_text("INSTRUCTION", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2, arcade.color.BLACK, font_size=50,
                         anchor_x="center")

        arcade.draw_text("Collect coins and find the exit!", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 1.5, arcade.color.ORANGE_PEEL, font_size=50,
                         anchor_x="center")
        arcade.draw_text("Use arrow keys to run and space bar for jump.\n\n"
                         "Press P to pause the game",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.3, arcade.color.BLACK, font_size=30, anchor_x="center")

        draw_menu_button()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.play_sound(self.menu_select)
        button_list = [BUTTONS['menu']]
        GameMenu().eval_button(x, y, button_list)


def draw_menu_button():
    arcade.draw_scaled_texture_rectangle(BUTTONS['menu'][1], BUTTONS['menu'][2],
                                         BUTTONS['menu'][0], scale=1.4)
    arcade.draw_text("MENU",
                     SCREEN_WIDTH / 15.5, SCREEN_HEIGHT / 9.5, arcade.color.BLACK, font_size=20, align="right")


class Author(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_select = arcade.load_sound("sounds/menu_selection_click.wav")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("png_ground/BG/BG.png"))
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("images/author.png"))
        arcade.draw_text("ABOUT AUTHOR", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2, arcade.color.ORANGE_PEEL, font_size=50,
                         anchor_x="center")
        arcade.draw_text("Math student \n"
                         "who was used to play \n platform games a lot.\n\n"
                         "Enjoy the game!",
                         SCREEN_WIDTH / 3.1, SCREEN_HEIGHT / 2.4, arcade.color.LIGHT_CYAN, font_size=30,
                         anchor_x="center")
        draw_menu_button()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.play_sound(self.menu_select)
        button_list = [BUTTONS['menu']]
        GameMenu().eval_button(x, y, button_list)


class ScoreTable(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_select = arcade.load_sound("sounds/menu_selection_click.wav")

    def show_table(self):
        arcade.draw_text("LATEST SCORE", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        t = open('scores.txt', 'r')
        table = t.readlines()
        for i in table:
            arcade.draw_text(i, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 1.5,
                             arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,
                                            arcade.load_texture("png_ground/BG/BG.png"))
        self.show_table()
        draw_menu_button()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.play_sound(self.menu_select)
        button_list = [BUTTONS['menu']]
        GameMenu().eval_button(x, y, button_list)


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.fill_color = arcade.make_transparent_color(arcade.color.WHITE, transparency=80)

    def on_draw(self):
        self.game_view.on_draw()
        arcade.draw_lrtb_rectangle_filled(
            left=self.game_view.view_left,
            right=self.game_view.view_left + SCREEN_WIDTH,
            top=self.game_view.view_bottom + SCREEN_HEIGHT,
            bottom=self.game_view.view_bottom,
            color=self.fill_color,
        )
        arcade.draw_text("PAUSED", self.game_view.view_left + 100, self.game_view.view_bottom + 400,
                         arcade.color.RED_ORANGE, font_size=40, align="center")
        arcade.draw_text("PRESS P TO RESUME", self.game_view.view_left + 100, self.game_view.view_bottom + 300,
                         arcade.color.YELLOW_ROSE, font_size=20, align="right")
        self.draw_menu_gameplay()

    def draw_menu_gameplay(self):
        arcade.draw_scaled_texture_rectangle(self.game_view.view_left + 80, self.game_view.view_bottom + 67,
                                             arcade.load_texture("images/HUD/hudJewel_yellow.png"), scale=1.4)
        arcade.draw_text("MENU", self.game_view.view_left + 50, self.game_view.view_bottom + 60,
                         arcade.color.BLACK, font_size=20, align="center")

    def eval_menu_gameplay(self, x, y):
        button_list = [arcade.load_texture("images/HUD/hudJewel_yellow.png"),
                       SCREEN_WIDTH / 10, SCREEN_HEIGHT / 9,
                       "self.window.show_view(GameMenu())"]
        texture = button_list[0]
        if button_list[1] - texture.width // 2 <= x <= button_list[1] + texture.width // 2:
            if button_list[2] - texture.height // 2 <= y <= button_list[2] + texture.height // 2:
                eval(button_list[3])
                arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.eval_menu_gameplay(x, y)
        if self.game_view.music:
            self.game_view.music.stop(self.game_view.current_player)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.P:
            self.window.show_view(self.game_view)


class GameOver(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.fill_color = arcade.make_transparent_color(arcade.color.WHITE, transparency=90)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            bottom_left_x=self.game_view.view_left,
            bottom_left_y=self.game_view.view_bottom,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=arcade.load_texture("images/JWDLx5AZBtI.jpg"),
            alpha=200)
        arcade.draw_scaled_texture_rectangle(self.game_view.view_left + 400, self.game_view.view_bottom + 150,
                                             arcade.load_texture("images/Tiles/lockRed.png"), scale=1.4)
        arcade.draw_text("GAME OVER", self.game_view.view_left + 400, self.game_view.view_bottom + 400,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("PRESS ENTER TO REPLAY", self.game_view.view_left + 400, self.game_view.view_bottom + 300,
                         arcade.color.ORANGE_PEEL, font_size=30, anchor_x="center")
        PauseView(self.game_view).draw_menu_gameplay()
        self.game_view.update_score()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)
        PauseView(self.game_view).eval_menu_gameplay(x, y)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            self.game_view.player_sprite.change_x = 0
            self.game_view.player_sprite.change_y = 0
            self.game_view.return_to_start()
            self.game_view.life = 3
            self.game_view.score = 0
            self.game_view.setup()
            self.window.show_view(self.game_view)
            arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)


class Congrats(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.fill_color = arcade.make_transparent_color(arcade.color.WHITE, transparency=90)

    def on_draw(self):
        """ Draw the congratulations"""
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            bottom_left_x=self.game_view.view_left,
            bottom_left_y=self.game_view.view_bottom,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=arcade.load_texture("images/congrats.png"))
        arcade.draw_text("CONGRATULATION", self.game_view.view_left + 100, self.game_view.view_bottom + 500,
                         arcade.color.YELLOW_ROSE, font_size=50, align="center")
        self.level_status_draw()
        PauseView(self.game_view).draw_menu_gameplay()
        self.game_view.update_score()

    def level_status_draw(self):
        if self.game_view.level == 2:
            arcade.draw_text("GAME FINISHED", self.game_view.view_left + 100,
                             self.game_view.view_bottom + 450,
                             arcade.color.YELLOW_ROSE, font_size=30, align="right")
        else:
            arcade.draw_text("TO NEXT LEVEL PRESS ENTER", self.game_view.view_left + 100,
                             self.game_view.view_bottom + 450,
                             arcade.color.YELLOW_ROSE, font_size=30, align="right")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        arcade.set_viewport(left=0, right=SCREEN_WIDTH, bottom=0, top=SCREEN_HEIGHT)
        PauseView(self.game_view).eval_menu_gameplay(x, y)

    def on_key_press(self, key, _modifiers):
        if self.game_view.level != 2:
            if key == arcade.key.ENTER:
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
        self.game_over_sound = arcade.load_sound("sounds/error.wav")
        self.game_creature = arcade.load_sound("sounds/game_creature.wav")
        self.current_player = None
        self.music = None

    def play_song(self):
        # stop currently playing
        if self.music:
            self.music.stop(self.current_player)

        # play next song
        self.music = arcade.Sound("sounds/childish_theme.WAV", streaming=True)
        self.current_player = self.music.play(volume=0.1, loop=True)
        time.sleep(0.03)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Reset the viewport
        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        self.player_sprite = self.create_player_sprite()
        arcade.play_sound(self.game_creature)
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
        player = arcade.AnimatedWalkingSprite()

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
            if self.music:
                self.music.stop(self.current_player)
                arcade.play_sound(self.finish_level_sound)

        if arcade.check_for_collision_with_list(self.player_sprite, self.pins):
            self.life_check()

    def return_to_start(self):
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.view_left = 0
        self.view_bottom = 0
        self.play_song()

    def life_check(self):
        if self.life >= 2:
            self.life -= 1
            self.draw_life_counter()
            arcade.play_sound(self.lost_life_sound)
            self.return_to_start()
        elif self.life == 1:
            self.window.show_view((GameOver(self)))
            if self.music:
                self.music.stop(self.current_player)
                arcade.play_sound(self.game_over_sound)


    def update_score(self):
        f = open('scores.txt', 'w')
        f.write("Level: " + str(self.level) + " score: " + str(self.score))
        f.close()


def main():
    " "" Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameMenu()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()

"""
    Jungle Adventure
    Simple Platformer Game
"""
from views import *
import arcade


def main():
    " "" Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameMenu()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()

# Removed for refactoring: import sys

import pygame

from settings import Settings
from ship import Ship

# Added during refactoring:
import game_functions as gf

def run_game():
	# Initialize game, settings and screen object.
	pygame.init()
	infrompy_settings = Settings()
	screen = pygame.display.set_mode((infrompy_settings.screen_width, infrompy_settings.screen_height))
	pygame.display.set_caption("Invaders from Python")

	# Create a ship.
	ship = Ship(screen)

	# Start the main loop for the game.
	while  True:
		gf.check_events()
		gf.update_screen(infrompy_settings, screen, ship)

run_game()
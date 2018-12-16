# 06/11/2018
# Tony Staunton
# www.tstaunton.com

import sys
import pygame

from lecture_004_settings import Settings
from lecture_005 import Ship
import lecture_006_game_functions as gf

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	infrompy_settings = Settings()
	screen = pygame.display.set_mode((infrompy_settings.screen_width, infrompy_settings.screen_height))
	pygame.display.set_caption("Invaders from Python")

	# Create the Ship
	ship = Ship(screen)

	# Start the main loop for the game.
	while  True:
		gf.check_events()
		gf.update_screen(infrompy_settings, screen,ship)

run_game()

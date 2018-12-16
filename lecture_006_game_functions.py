# 06/11/2018
# Tony Staunton
# www.tstaunton.com

import sys
import pygame

# Code added in lecture_016
def check_keydown_events(event, infrompy_settings, screen, ship, bullets):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# Create a new bulet and add it to the bullets group.
		new_bullet = Bullet(infrompy_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""Respond to keyup release."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ship):
	"""Respond to key presses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
			# Lecture_010
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			# Lecture_010
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False


# Refactoring Lecture 007
def update_screen(infrompy_settings, screen, ship):
	"""Update the images on the screen and flip to the new screen."""

	# Redraw the screen during each pass through the loop.
	screen.fill(infrompy_settings.bg_color)
	ship.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, infrompy_settings, screen):
		"""Initialize our ship and set its starting position."""
		super(Ship, self).__init__()
		self.screen = screen
		self.infrompy_settings = infrompy_settings

		# Load the ship image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the center of the ship
		self.center = float(self.rect.centerx)

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.infrompy_settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.center -= self.infrompy_settings.ship_speed

		# Update rect object from self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx


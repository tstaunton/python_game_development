class Settings():
	"""A class to store our games settings."""

	def __init__(self):
		"""Initialize our games settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (135,206,250)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60

		# Alien settings
		self.fleet_drop_speed = 30

		# How quickly the game speeds up
		self.speedup_scale = 1.2
		# How quickly the alien point values increases
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Iniatialize settings that change during the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 8
		self.alien_speed_factor = 2

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 100

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

		
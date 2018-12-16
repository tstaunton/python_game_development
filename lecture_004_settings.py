class Settings():
	"""A class to store our games settings."""

	def __init__(self):
		"""Initialize our game and screen settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (135,206,250)

		# Ship Settings from Lecture_011
		self.ship_speed = 1.5

		# Lecture_013: Bullet Section
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60

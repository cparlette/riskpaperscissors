from constants import *
import pygame
from Location import Location

class Risk():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.img = pygame.transform.scale(
			pygame.image.load('2000px-Risk_board.svg.png').convert(),
			(1000,692)
		)
		self.locations = []
		self.locations.append(Location(self,"1",75,108,"Alaska",13,13))

	def process_keydown(self, key):
		pass

	def draw(self):
		self.surface.fill(SHADOW)
		self.surface.blit(self.img,(0,0))
		for location in self.locations:
			location.draw()
		self.screen.blit(self.surface, (0, 0))

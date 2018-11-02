from constants import *
import pygame

class Risk():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.img = pygame.transform.scale(
			pygame.image.load('2000px-Risk_board.svg.png').convert(),
			(1000,692)
		)

	def process_keydown(self, key):
		pass

	def draw(self):
		self.surface.fill(SHADOW)
		self.surface.blit(self.img,(0,0))
		self.screen.blit(self.surface, (0, 0))

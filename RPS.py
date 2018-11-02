from constants import *
import pygame

class RPS():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))

	def draw(self):
		self.surface.fill(GREEN)
		self.screen.blit(self.surface, (0, 0))
	
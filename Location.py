from constants import *
import pygame

class Location():
	def __init__(self, risk_game, location_id, center_x, center_y, name, neighbors):
		self.location_id = location_id
		self.armies = 0
		self.bg_color = WHITE
		self.center_x = center_x
		self.center_y = center_y
		self.name = name
		self.neighbors = neighbors
		self.width = 30
		self.height = 30
		self.risk_game = risk_game
		self.text_color = BLACK
		self.font_size = int(self.height * 3 / 4)
		self.font = pygame.font.SysFont("tahoma", self.font_size)
		self.surface = pygame.Surface((self.width, self.height))
		self.draw()

	def insert_text(self):
		text_render = self.font.render(str(self.armies), 1, self.text_color)
		text_render_size = self.font.size(str(self.armies))
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(
			text_render, 
			(self.surface.get_width() / 2 - x_offset, self.surface.get_height() / 2 - y_offset)
		)

	def is_hovered(self, mx, my):
		if (mx > self.center_x - self.width / 2 and mx < self.center_x + self.width / 2):
			if (my > self.center_y - self.height / 2 and my < self.center_y + self.height / 2):
				return True
		else:
			return False

	def draw(self):
		self.surface.fill(self.bg_color)
		self.insert_text()
		self.risk_game.surface.blit(
			self.surface, 
			(self.center_x - self.width / 2, self.center_y - self.height / 2)
		)
 
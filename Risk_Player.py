from constants import *
import pygame

class Risk_Player():
	def __init__(self, risk_game, player_id, name, color, center_x, center_y):
		self.total_armies = 0
		self.total_locations = 0
		self.player_id = player_id
		self.name = name
		self.color = color
		self.controlled_locations = []
		self.risk_game = risk_game
		self.center_x = center_x
		self.center_y = center_y
		self.width = 300
		self.height = 158
		self.text_color = BLACK
		self.font_size = int(self.height * 1 / 4)
		self.font = pygame.font.SysFont("tahoma", self.font_size)
		self.surface = pygame.Surface((self.width, self.height))
		self.draw()

	def insert_text(self):
		# Print name
		text_render = self.font.render(self.name, 1, self.text_color)
		text_render_size = self.font.size(self.name)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(
			text_render, 
			(self.surface.get_width() / 2 - x_offset, self.surface.get_height() / 4 - y_offset)
		)

		# Print total armies
		text = "Total armies = " + str(self.total_armies)
		text_render = self.font.render(text, 1, self.text_color)
		text_render_size = self.font.size(text)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(
			text_render, 
			(self.surface.get_width() / 2 - x_offset, self.surface.get_height() / 2 - y_offset)
		)

		# Print total locations
		text = "Total territories = " + str(self.total_locations)
		text_render = self.font.render(text, 1, self.text_color)
		text_render_size = self.font.size(text)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(
			text_render, 
			(self.surface.get_width() / 2 - x_offset, self.surface.get_height() * 3 / 4 - y_offset)
		)

	def draw(self):
		self.surface.fill(self.color)
		self.insert_text()
		self.risk_game.surface.blit(
			self.surface, 
			(self.center_x - self.width / 2, self.center_y - self.height / 2)
		)

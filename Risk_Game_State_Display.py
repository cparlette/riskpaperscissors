from constants import *
import pygame

class Risk_Game_State_Display():
	def __init__(self, risk_game):
		self.risk_game = risk_game
		self.width = 400
		self.height = 158
		self.bg_color = WHITE
		self.text_color = BLACK
		self.center_x = 500
		self.center_y = 771
		self.font_size = int(self.height * 1 / 4)
		self.font = pygame.font.SysFont("tahoma", self.font_size)
		self.surface = pygame.Surface((self.width, self.height))
		self.draw()

	def insert_text(self):
		# Print current player
		text = "Current Player : " + str(self.risk_game.current_player)
		text_render = self.font.render(text, 1, self.text_color)
		text_render_size = self.font.size(text)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(
			text_render, 
			(self.surface.get_width() / 2 - x_offset, self.surface.get_height() / 4 - y_offset)
		)

		# Print current game phase
		text = self.risk_game.game_phase
		text_render = self.font.render(text, 1, self.text_color)
		text_render_size = self.font.size(text)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(
			text_render, 
			(self.surface.get_width() / 2 - x_offset, self.surface.get_height() / 2 - y_offset)
		)

		# Situational third line of text
		situational_text = None
		if self.risk_game.game_phase == "Place New Armies":
			situational_text = "Remaining armies: "+str(self.risk_game.placable_armies)
		elif self.risk_game.situational_text:
			situational_text = self.risk_game.situational_text
		if situational_text:
			text_render = self.font.render(situational_text, 1, self.text_color)
			text_render_size = self.font.size(situational_text)
			x_offset = text_render_size[0] / 2
			y_offset = text_render_size[1] / 2
			self.surface.blit(
				text_render, 
				(self.surface.get_width() / 2 - x_offset, self.surface.get_height() * 3 / 4 - y_offset)
			)

	def draw(self):
		self.surface.fill(self.bg_color)
		self.insert_text()
		self.risk_game.surface.blit(
			self.surface, 
			(self.center_x - self.width / 2, self.center_y - self.height / 2)
		)
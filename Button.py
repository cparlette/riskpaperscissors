from constants import *
import pygame

class Button():
	""" Base button object """
 
	def __init__(self, menu, action, width, height, bg_color, text, font_type, text_color, center_x, center_y):
		self.menu = menu
		self.action = action
		self.width = width
		self.height = height
		self.bg_color = bg_color
		self.text = text
		self.text_color = text_color
		# set the font size to 1/2 the button height
		self.font_size = int(height / 2)
		self.font = pygame.font.SysFont(font_type, self.font_size)
		self.center_x = center_x
		self.center_y = center_y
		self.surface = pygame.Surface((width, height))
		self.draw()
 
	def get_action(self):
		return self.action
 
	def insert_text(self):
		""" Insert text onto button surface """
		text_render = self.font.render(self.text, 1, self.text_color)
		text_render_size = self.font.size(self.text)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		self.surface.blit(text_render, (self.surface.get_width() / 2 - x_offset, self.surface.get_height() / 2 - y_offset))
 
	def is_hovered(self, mx, my):
		if (mx > self.center_x - self.width / 2 and mx < self.center_x + self.width / 2):
			if (my > self.center_y - self.height / 2 and my < self.center_y + self.height / 2):
				self.bg_color = GREEN
				return True
		self.bg_color = WHITE
		return False
 
	def draw(self):
		self.surface.fill(self.bg_color)
		self.insert_text()
		self.menu.surface.blit(self.surface, (self.center_x - self.width / 2, self.center_y - self.height / 2))
 
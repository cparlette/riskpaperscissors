from constants import *
import pygame

class Textbox():
	def __init__(self, menu, label, text, center_x, center_y):
		self.menu = menu
		self.label = label
		self.text = text
		self.center_x = center_x
		self.center_y = center_y
		self.label_color = WHITE
		self.text_bgcolor = SHADOW
		self.text_color = WHITE

		self.font_size = int(HEIGHT / 20)
		self.font = pygame.font.SysFont("tahoma", self.font_size)
		self.width = 750
		self.height = int(HEIGHT / 14)
		self.text_rect = pygame.Rect(self.width / 2, 0, self.width / 2, self.height)
		self.surface = pygame.Surface((self.width, self.height))
		self.draw()

	def draw_label(self):
		label_render = self.font.render(self.label, 1, self.label_color)
		label_render_size = self.font.size(self.label)
		#x_offset = label_render_size[0] / 2
		y_offset = label_render_size[1] / 2
		self.surface.blit(label_render, (0, self.surface.get_height() / 2 - y_offset))

	def draw_text(self):
		text_render = self.font.render(self.text, 1, self.text_color)
		text_render_size = self.font.size(self.text)
		x_offset = text_render_size[0] / 2
		y_offset = text_render_size[1] / 2
		pygame.draw.rect(self.surface, self.text_bgcolor, self.text_rect, 0)
		self.surface.blit(text_render, (self.center_x - x_offset, self.surface.get_height() / 2 - y_offset))

	def draw(self):
		self.surface.fill(GREEN)
		self.draw_label()
		self.draw_text()
		self.menu.surface.blit(self.surface, (self.center_x - self.width / 2, self.center_y - self.height / 2))
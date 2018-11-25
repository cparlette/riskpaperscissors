from constants import *
import pygame

# cursor stuff from https://github.com/Nearoo/pygame-text-input/blob/master/pygame_textinput.py

class Textbox():
	def __init__(self, menu, label, text, center_x, center_y, label_bgcolor):
		self.menu = menu
		self.label = label
		self.text = text
		self.center_x = center_x
		self.center_y = center_y

		self.label_color = WHITE
		self.label_bgcolor = label_bgcolor
		self.text_bgcolor = SHADOW
		self.text_color = BLACK

		self.font_size = int(HEIGHT / 20)
		self.font = pygame.font.SysFont("tahoma", self.font_size)
		self.width = 750
		self.height = int(HEIGHT / 14)
		self.label_rect = pygame.Rect(0, 0, self.width / 2, self.height)
		self.text_rect = pygame.Rect(self.width / 2, 0, self.width / 2, self.height)
		self.surface = pygame.Surface((self.width, self.height))

		# stuff from https://github.com/Nearoo/pygame-text-input/blob/master/pygame_textinput.py
		self.cursor_color = (0, 0, 1)
		self.cursor_surface = pygame.Surface((int(self.font_size/20+1), self.font_size))
		self.cursor_surface.fill(self.cursor_color)
		self.cursor_position = len(self.text)
		self.cursor_visible = False

		self.draw()

	def is_hovered(self, mx, my):
		if (mx > self.center_x - self.width / 2 and mx < self.center_x + self.width / 2):
			if (my > self.center_y - self.height / 2 and my < self.center_y + self.height / 2):
				return True
		return False

	def process_keydown(self, event):
		if event.key == pygame.K_BACKSPACE:
			self.text = self.text[:-1]
			self.cursor_position = max(self.cursor_position - 1, 0)
		else:
			self.text += event.unicode
			self.cursor_position += len(event.unicode)

	def draw_label(self):
		self.surface.fill(self.label_bgcolor, self.label_rect)
		label_render = self.font.render(self.label, 1, self.label_color)
		label_render_size = self.font.size(self.label)
		y_offset = label_render_size[1] / 2
		self.surface.blit(label_render, (5, self.surface.get_height() / 2 - y_offset))

	def draw_text(self):
		self.surface.fill(self.text_bgcolor, self.text_rect)
		text_render = self.font.render(self.text, 1, self.text_color)
		text_render_size = self.font.size(self.text)
		y_offset = text_render_size[1] / 2
		self.surface.blit(text_render, (self.surface.get_width() / 2 + 5, self.surface.get_height() / 2 - y_offset))

	def draw(self):
		self.draw_label()
		self.draw_text()
		if self.cursor_visible:
			cursor_x_pos = self.font.size(self.text[:self.cursor_position])[0]
			# Without this, the cursor is invisible when self.cursor_position > 0:
			if self.cursor_position > 0:
				cursor_x_pos -= self.cursor_surface.get_width()
			self.surface.blit(self.cursor_surface, (self.surface.get_width() / 2 + cursor_x_pos + 10, (self.height - self.cursor_surface.get_height()) / 2))
		self.menu.surface.blit(self.surface, (self.center_x - self.width / 2, self.center_y - self.height / 2))
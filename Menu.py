from Button import Button
from Textbox import Textbox
from constants import *
import pygame

class Menu():
	""" Base Menu Object """
 
	def __init__(self, screen, title, title_color, menu_font_type, bg_color):
		self.screen = screen
		self.title = title
		self.title_color = title_color
		self.font_type = menu_font_type
		self.bg_color = bg_color
		self.title_font_size = int(HEIGHT / 10)
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.buttons = []
		self.textboxes = []
		self.textbox_focus = None
 
	def add_button(self, action, width, height, bg_color, text, text_color, center_x, center_y):
		""" Add a button to the menu """
		new_button = Button(self, action, width, height, bg_color, text, self.font_type, text_color, center_x, center_y)
		self.buttons.append(new_button)

	def add_textbox(self, label, text, center_x, center_y, label_bgcolor):
		""" Add a button to the menu """
		new_textbox = Textbox(self, label, text, center_x, center_y, label_bgcolor)
		self.textboxes.append(new_textbox)
 
	def is_button_clicked(self, mouse_pos):
		for button in self.buttons:
			if button.is_hovered(mouse_pos[0], mouse_pos[1]):
				return button.get_action()
		action = "None"
		return action

	def is_textbox_clicked(self, mouse_pos):
		if not self.textbox_focus:
			for textbox in self.textboxes:
				if textbox.is_hovered(mouse_pos[0], mouse_pos[1]):
					self.textbox_focus = textbox
					textbox.cursor_visible = True
					return True 
		return False

	def process_keydown(self, event):
		if self.textbox_focus:
			if event.key == pygame.K_RETURN:
				self.textbox_focus = None
			else:
				self.textbox_focus.process_keydown(event)
 
	def draw(self):
		""" Draw the menu surface and then blit to screen """
		# Fill menu surface with background color
		self.surface.fill(self.bg_color)
		# Draw menu title
		font = pygame.font.SysFont(self.font_type, self.title_font_size)
		title = font.render(self.title, 1, self.title_color)
		render_size = font.size(self.title)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		title_center_x = WIDTH / 2 - x_offset
		title_center_y = HEIGHT / 8 - y_offset
		self.surface.blit(title, (title_center_x, title_center_y))
 
		# get mouse position
		mouse_pos = pygame.mouse.get_pos()
		# Draw all menu buttons
		for button in self.buttons:
			# Call is_hovered function to check for hover
			# which will change button color if true
			button.is_hovered(mouse_pos[0], mouse_pos[1])
			# Draw button
			button.draw()
		for textbox in self.textboxes:
			textbox.draw()
		# Blit menu surface to screen
		self.screen.blit(self.surface, (0, 0))

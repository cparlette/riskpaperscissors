from constants import *
import pygame

class Player():
	def __init__(self):
		self.choice = None
		self.wins = 0

class RPS():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.player_one = Player()
		self.player_two = Player()
		#font stuff
		self.font_type = "tahoma"
		self.font_size = int(HEIGHT / 10)

	def process_keydown(self, key):
		if key == pygame.K_a:
			self.player_one.choice = "rock"
		elif key == pygame.K_s:
			self.player_one.choice = "paper"
		elif key == pygame.K_d:
			self.player_one.choice = "scissors"
		elif key == pygame.K_j:
			self.player_two.choice = "rock"
		elif key == pygame.K_k:
			self.player_two.choice = "paper"
		elif key == pygame.K_l:
			self.player_two.choice = "scissors"

	def draw(self):
		self.surface.fill(GREEN)
		font = pygame.font.SysFont(self.font_type, self.font_size)
		# title
		title_text = "Let's Play RPS!"
		title = font.render(title_text, 1, BLACK)
		render_size = font.size(title_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		title_center_x = WIDTH / 2 - x_offset
		title_center_y = HEIGHT / 8 - y_offset
		self.surface.blit(title, (title_center_x, title_center_y))

		# player one info
		if self.player_one.choice:
			player_one_text = "P1 choice is "+self.player_one.choice
		else:
			player_one_text = "P1 choose!"
		text_one = font.render(player_one_text, 1, BLUE)
		render_size = font.size(player_one_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		player_one_center_x = WIDTH / 4 - x_offset
		player_one_center_y = HEIGHT / 2 - y_offset
		self.surface.blit(text_one, (player_one_center_x, player_one_center_y))

		# player two info
		if self.player_two.choice:
			player_two_text = "P2 choice is "+self.player_two.choice
		else:
			player_two_text = "P2 choose!"
		text_two = font.render(player_two_text, 1, RED)
		render_size = font.size(player_two_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		player_two_center_x = WIDTH * 3 / 4 - x_offset
		player_two_center_y = HEIGHT / 2 - y_offset
		self.surface.blit(text_two, (player_two_center_x, player_two_center_y))

		self.screen.blit(self.surface, (0, 0))
	
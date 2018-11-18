from constants import *
import pygame

class Player():
	def __init__(self, lives):
		self.choice = None
		self.lives = lives
		self.last_choice = None

class RPS():
	def __init__(self, screen, player_one_lives, player_two_lives):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.player_one = Player(player_one_lives)
		self.player_two = Player(player_two_lives)
		self.last_result = None
		#font stuff
		self.font_type = "tahoma"
		self.font_size = int(HEIGHT / 16)

	def showdown(self):
		if self.player_one.choice == "rock":
			if self.player_two.choice == "rock":
				self.last_result = "Tie - both chose rock"
			elif self.player_two.choice == "paper":
				self.last_result = "Player 2 wins - P over R"
				self.player_one.lives -= 1
			else:
				self.last_result = "Player 1 wins - R over S"
				self.player_two.lives -= 1
		elif self.player_one.choice == "paper":
			if self.player_two.choice == "rock":
				self.last_result = "Player 1 wins - P over R"
				self.player_two.lives -= 1
			elif self.player_two.choice == "paper":
				self.last_result = "Tie - both chose paper"
			else:
				self.last_result = "Player 2 wins - S over P"
				self.player_one.lives -= 1
		else:
			if self.player_two.choice == "rock":
				self.last_result = "Player 2 wins - R over S"
				self.player_one.lives -= 1
			elif self.player_two.choice == "paper":
				self.last_result = "Player 1 wins - S over P"
				self.player_two.lives -= 1
			else:
				self.last_result = "Tie - both chose scissors"
		self.player_one.last_choice = self.player_one.choice
		self.player_two.last_choice = self.player_two.choice
		self.player_one.choice = None
		self.player_two.choice = None


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
		#if both players have played, figure out the winner
		if self.player_one.choice and self.player_two.choice:
			self.showdown()

	def process_mouseclick(self, mouse_pos):
		# no mouse in RPS (yet)
		pass

	def draw_text(self, font, surface, text, font_color, center_x, center_y):
		rendered_text = font.render(text, 1, font_color)
		render_size = font.size(text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		text_center_x = center_x - x_offset
		text_center_y = center_y - y_offset
		surface.blit(rendered_text, (text_center_x, text_center_y))

	def draw(self):
		self.surface.fill(GREEN)
		font = pygame.font.SysFont(self.font_type, self.font_size)
		# title
		title_text = "Let's Play RPS!"
		self.draw_text(font, self.surface, title_text, BLACK, WIDTH / 2, HEIGHT / 8)

		# player one info
		if self.player_one.choice:
			player_one_text = "Player 1 has chosen!"
		else:
			player_one_text = "Player 1, choose!"
		self.draw_text(font, self.surface, player_one_text, BLUE, WIDTH / 4, HEIGHT * 4 / 16)

		player_one_lives_text = "Lives: "+str(self.player_one.lives)
		self.draw_text(font, self.surface, player_one_lives_text, BLUE, WIDTH / 4, HEIGHT * 6 / 16)

		if self.player_one.last_choice:
			one_last_choice_text = "Last: "+self.player_one.last_choice
			self.draw_text(font, self.surface, one_last_choice_text, BLUE, WIDTH / 4, HEIGHT * 8 / 16)

		one_rules_text_top = "A=Rock | S=Paper"
		self.draw_text(font, self.surface, one_rules_text_top, BLUE, WIDTH / 4, HEIGHT * 11 / 16)

		one_rules_text_bottom = "D=Scissors"
		self.draw_text(font, self.surface, one_rules_text_bottom, BLUE, WIDTH / 4, HEIGHT * 12 / 16)

		# player two info
		if self.player_two.choice:
			player_two_text = "Player 2 has chosen!"
		else:
			player_two_text = "Player 2, choose!"
		self.draw_text(font, self.surface, player_two_text, RED, WIDTH * 3 / 4, HEIGHT * 4 / 16)

		player_two_lives_text = "Lives: "+str(self.player_two.lives)
		self.draw_text(font, self.surface, player_two_lives_text, RED, WIDTH * 3 / 4, HEIGHT * 6 / 16)

		if self.player_two.last_choice:
			two_last_choice_text = "Last: "+self.player_two.last_choice
			self.draw_text(font, self.surface, two_last_choice_text, RED, WIDTH * 3 / 4, HEIGHT * 8 / 16)

		two_rules_text_top = "J=Rock | K=Paper"
		self.draw_text(font, self.surface, two_rules_text_top, RED, WIDTH * 3 / 4, HEIGHT * 11 / 16)

		two_rules_text_bottom = "L=Scissors"
		self.draw_text(font, self.surface, two_rules_text_bottom, RED, WIDTH * 3 / 4, HEIGHT * 12 / 16)

		#results
		if self.last_result:
			result_text = self.last_result
		else:
			result_text = "No games played yet"
		self.draw_text(font, self.surface, result_text, BLACK, WIDTH / 2, HEIGHT * 7 / 8)

		self.screen.blit(self.surface, (0, 0))
	
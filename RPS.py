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
		self.last_result = None
		#font stuff
		self.font_type = "tahoma"
		self.font_size = int(HEIGHT / 10)

	def showdown(self):
		if self.player_one.choice == "rock":
			if self.player_two.choice == "rock":
				self.last_result = "Tie - both chose rock"
			elif self.player_two.choice == "paper":
				self.last_result = "Player 2 wins - P over R"
				self.player_two.wins += 1
			else:
				self.last_result = "Player 1 wins - R over S"
				self.player_one.wins += 1
		elif self.player_one.choice == "paper":
			if self.player_two.choice == "rock":
				self.last_result = "Player 1 wins - P over R"
				self.player_one.wins += 1
			elif self.player_two.choice == "paper":
				self.last_result = "Tie - both chose paper"
			else:
				self.last_result = "Player 2 wins - S over P"
				self.player_two.wins += 1
		else:
			if self.player_two.choice == "rock":
				self.last_result = "Player 2 wins - R over S"
				self.player_two.wins += 1
			elif self.player_two.choice == "paper":
				self.last_result = "Player 1 wins - S over P"
				self.player_one.wins += 1
			else:
				self.last_result = "Tie - both chose scissors"
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
			player_one_text = "P1: "+self.player_one.choice
		else:
			player_one_text = "P1 choose!"
		text_one = font.render(player_one_text, 1, BLUE)
		render_size = font.size(player_one_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		player_one_center_x = WIDTH / 4 - x_offset
		player_one_center_y = HEIGHT / 2 - y_offset
		self.surface.blit(text_one, (player_one_center_x, player_one_center_y))

		player_one_wins_text = "Wins: "+str(self.player_one.wins)
		text_one_wins = font.render(player_one_wins_text, 1, BLUE)
		render_size = font.size(player_one_wins_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		player_one_wins_center_x = WIDTH / 4 - x_offset
		player_one_wins_center_y = HEIGHT * 5 / 8 - y_offset
		self.surface.blit(text_one_wins, (player_one_wins_center_x, player_one_wins_center_y))

		# player two info
		if self.player_two.choice:
			player_two_text = "P2: "+self.player_two.choice
		else:
			player_two_text = "P2 choose!"
		text_two = font.render(player_two_text, 1, RED)
		render_size = font.size(player_two_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		player_two_center_x = WIDTH * 3 / 4 - x_offset
		player_two_center_y = HEIGHT / 2 - y_offset
		self.surface.blit(text_two, (player_two_center_x, player_two_center_y))

		player_two_wins_text = "Wins: "+str(self.player_two.wins)
		text_two_wins = font.render(player_two_wins_text, 1, RED)
		render_size = font.size(player_two_wins_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		player_two_wins_center_x = WIDTH * 3 / 4 - x_offset
		player_two_wins_center_y = HEIGHT * 5 / 8 - y_offset
		self.surface.blit(text_two_wins, (player_two_wins_center_x, player_two_wins_center_y))

		#results
		if self.last_result:
			result_text = self.last_result
		else:
			result_text = "No games played yet"
		result = font.render(result_text, 1, BLACK)
		render_size = font.size(result_text)
		x_offset = render_size[0] / 2
		y_offset = render_size[1] / 2
		result_center_x = WIDTH / 2 - x_offset
		result_center_y = HEIGHT * 7 / 8 - y_offset
		self.surface.blit(result, (result_center_x, result_center_y))

		self.screen.blit(self.surface, (0, 0))
	
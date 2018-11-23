from constants import *
import pygame

class Player():
	def __init__(self, lives):
		self.choice = None
		self.lives = lives
		self.last_choice = None
		self.choice_image = None

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
		# Stuff for displaying intro
		self.show_intro = True 
		self.start_time = pygame.time.get_ticks()
		self.intro_image = pygame.image.load('assets/fighting-icon-11.jpg')
		# Store images at 250x250
		self.rock_image = pygame.transform.scale(pygame.image.load('assets/rock-icon-png-13.jpg'), (250, 250))
		self.paper_image = pygame.transform.scale(pygame.image.load('assets/paper-icon-9.jpg'), (250, 250))
		self.scissors_image = pygame.transform.scale(pygame.image.load('assets/scissor-icon-12.jpg'), (250, 250))
		self.blue_arrow_image = pygame.transform.scale(pygame.image.load('assets/blue-left-arrow-png-14.png'), (250, 250))
		self.red_arrow_image = pygame.transform.scale(pygame.image.load('assets/red-arrow-right-pointing-5.png'), (250, 250))
		self.equals_image = pygame.transform.scale(pygame.image.load('assets/equal-sign-icon-25.jpg'), (250, 250))

		# Showdown status
		self.showdown_happening = False
		self.showdown_start_time = None
		self.loser = None


	def showdown(self):
		if self.player_one.choice == "rock":
			self.player_one.choice_image = self.rock_image
			if self.player_two.choice == "rock":
				self.player_two.choice_image = self.rock_image
				self.last_result = "Tie - both chose rock"
			elif self.player_two.choice == "paper":
				self.player_two.choice_image = self.paper_image
				self.last_result = "Player 2 wins - P over R"
				self.loser = self.player_one
			else:
				self.player_two.choice_image = self.scissors_image
				self.last_result = "Player 1 wins - R over S"
				self.loser = self.player_two
		elif self.player_one.choice == "paper":
			self.player_one.choice_image = self.paper_image
			if self.player_two.choice == "rock":
				self.player_two.choice_image = self.rock_image
				self.last_result = "Player 1 wins - P over R"
				self.loser = self.player_two
			elif self.player_two.choice == "paper":
				self.player_two.choice_image = self.paper_image
				self.last_result = "Tie - both chose paper"
			else:
				self.player_two.choice_image = self.scissors_image
				self.last_result = "Player 2 wins - S over P"
				self.loser = self.player_one
		else:
			self.player_one.choice_image = self.scissors_image
			if self.player_two.choice == "rock":
				self.player_two.choice_image = self.rock_image
				self.last_result = "Player 2 wins - R over S"
				self.loser = self.player_one
			elif self.player_two.choice == "paper":
				self.player_two.choice_image = self.paper_image
				self.last_result = "Player 1 wins - S over P"
				self.loser = self.player_two
			else:
				self.player_two.choice_image = self.scissors_image
				self.last_result = "Tie - both chose scissors"
		self.showdown_happening = True
		self.showdown_start_time = pygame.time.get_ticks()
		

	def showdown_cleanup(self):
		self.player_one.last_choice = self.player_one.choice
		self.player_two.last_choice = self.player_two.choice
		self.player_one.choice = None
		self.player_two.choice = None
		self.showdown_happening = False
		self.showdown_start_time = None
		self.player_one.choice_image = None
		self.player_two.choice_image = None
		if self.loser:
			self.loser.lives -= 1
			self.loser = None


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
		self.surface.fill(SHADOW)
		if self.show_intro:
			# Display the fight intro
			self.surface.blit(self.intro_image,(244,290))
			intro_font = pygame.font.SysFont("tahoma", int(HEIGHT / 4))
			self.draw_text(intro_font, self.surface, "FIGHT", BLACK, WIDTH / 2, HEIGHT / 4)
			if pygame.time.get_ticks() - self.start_time > 1000:
				self.show_intro = False
		elif self.showdown_happening:
			self.surface.blit(self.player_one.choice_image, (125,290))
			self.surface.blit(self.player_two.choice_image, (625,290))
			if self.loser == self.player_one:
				self.surface.blit(self.red_arrow_image, (375, 290))
				winner_font = pygame.font.SysFont("tahoma", int(HEIGHT / 8))
				self.draw_text(winner_font, self.surface, "WINNER", RED, WIDTH * 3 / 4, HEIGHT * 3 / 4)
			elif self.loser == self.player_two:
				self.surface.blit(self.blue_arrow_image, (375, 290))
				winner_font = pygame.font.SysFont("tahoma", int(HEIGHT / 8))
				self.draw_text(winner_font, self.surface, "WINNER", BLUE, WIDTH / 4, HEIGHT * 3 / 4)
			else:
				self.surface.blit(self.equals_image, (375, 290))
				winner_font = pygame.font.SysFont("tahoma", int(HEIGHT / 8))
				self.draw_text(winner_font, self.surface, "TIE", BLACK, WIDTH / 2, HEIGHT * 3 / 4)
			if pygame.time.get_ticks() - self.showdown_start_time > 1000:
				self.showdown_cleanup()
		else:
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
	
from constants import *
import pygame
from Location import Location
from Risk_Player import Risk_Player
from Risk_Game_State_Display import Risk_Game_State_Display
import random
from RPS import RPS
from Button import Button


class Risk():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.img = pygame.transform.scale(
			pygame.image.load('2000px-Risk_board.svg.png'),
			(1000,692)
		)
		self.locations = {}
		# Locations below are in the format:
		# location_id, center_x, center_y, name, neighbors

		# North America
		self.locations[1] = Location(self,1,80,112,"Alaska",[2,3,32])
		self.locations[2] = Location(self,2,168,112,"NW Territory",[1,3,4,6])
		self.locations[3] = Location(self,3,158,161,"Alberta",[1,2,4,7])
		self.locations[4] = Location(self,4,222,160,"Ontario",[2,3,5,6,7,8])
		self.locations[5] = Location(self,5,294,165,"Quebec",[4,6,8])
		self.locations[6] = Location(self,6,345,71,"Greenland",[2,4,5,15])
		self.locations[7] = Location(self,7,161,233,"Western US",[3,4,8,9])
		self.locations[8] = Location(self,8,237,247,"Eastern US",[4,5,7,9])
		self.locations[9] = Location(self,9,170,321,"Central America",[7,8,10])
		# South America
		self.locations[10] = Location(self,10,237,378,"Venezuela",[9,11,12])
		self.locations[11] = Location(self,11,227,450,"Peru",[10,12,13])
		self.locations[12] = Location(self,12,315,437,"Brazil",[10,11,13,25])
		self.locations[13] = Location(self,13,260,554,"Argentina",[11,12])
		# Europe
		self.locations[14] = Location(self,14,405,213,"Great Britain",[15,16,17,20])
		self.locations[15] = Location(self,15,433,143,"Iceland",[6,14,17])
		self.locations[16] = Location(self,16,499,230,"Northern Europe",[14,17,18,19,20])
		self.locations[17] = Location(self,17,504,139,"Scandinavia",[14,15,16,19])
		self.locations[18] = Location(self,18,512,290,"Southern Europe",[16,19,20,23,25,33])
		self.locations[19] = Location(self,19,584,195,"Ukraine",[16,17,18,27,33,37])
		self.locations[20] = Location(self,20,429,319,"Western Europe",[14,16,18,25])
		# Africa
		self.locations[21] = Location(self,21,542,502,"Congo",[22,25,26])
		self.locations[22] = Location(self,22,585,451,"East Africa",[21,23,24,25,26,33])
		self.locations[23] = Location(self,23,542,389,"Egypt",[18,22,25,33])
		self.locations[24] = Location(self,24,639,593,"Madagascar",[22,26])
		self.locations[25] = Location(self,25,464,424,"North Africa",[12,18,20,21,22,23])
		self.locations[26] = Location(self,26,546,590,"South Africa",[21,22,24])
		# Asia
		self.locations[27] = Location(self,27,673,257,"Afghanistan",[19,28,29,33,37])
		self.locations[28] = Location(self,28,782,300,"China",[27,29,34,35,36,37])
		self.locations[29] = Location(self,29,724,350,"India",[27,28,33,35])
		self.locations[30] = Location(self,30,801,180,"Irkutsk",[32,34,36,38])
		self.locations[31] = Location(self,31,916,245,"Japan",[32,34])
		self.locations[32] = Location(self,32,892,104,"Kamchatka",[1,30,31,34,38])
		self.locations[33] = Location(self,33,611,347,"Middle East",[18,19,22,23,27,29])
		self.locations[34] = Location(self,34,814,240,"Mongolia",[28,30,31,32,36])
		self.locations[35] = Location(self,35,804,378,"Siam",[28,29,41])
		self.locations[36] = Location(self,36,735,119,"Siberia",[27,28,30,34,37,38])
		self.locations[37] = Location(self,37,685,165,"Ural",[19,27,28,36])
		self.locations[38] = Location(self,38,815,95,"Yakutsk",[30,32,36])
		# Australia
		self.locations[39] = Location(self,39,922,544,"Eastern Australia",[40,42])
		self.locations[40] = Location(self,40,855,589,"Western Australia",[39,41,42])
		self.locations[41] = Location(self,41,820,485,"Indonesia",[35,40,42])
		self.locations[42] = Location(self,42,910,462,"New Guinea",[39,40,41])

		# Set up players, 2 for now
		self.players = {}
		self.players[1] = Risk_Player(self, 1, "Player1", LIGHTBLUE, 150, 771)
		self.players[2] = Risk_Player(self, 2, "Player2", RED, 850, 771)
		self.current_player = 1
		self.game_phase = "Pick Starting Countries"
		self.attacker = None
		self.defender = None

		# Text that can be used in the bottom-middle display
		self.situational_text = None

		# Create the game state display
		self.game_state_display = Risk_Game_State_Display(self)

		# Blank RPS game that will get created on the fly during battle
		self.rps = None

		# End turn button
		self.end_turn_button = Button(self, "End Turn", 100, 50, WHITE, str("End Turn"), "tahoma", BLACK, 50, 667)

		# Placable armies that gets populated for each new turn
		self.placable_armies = 0


	def process_keydown(self, key):
		# When a key is pressed during Risk
		# Mostly just for testing purposes, maybe can do more with this
		if key == pygame.K_r:
			# Check the game phase , if during setup then randomize things
			if self.game_phase == "Pick Starting Countries" and self.players[1].total_locations == 0:
				# Rancomly pick starting countries for each player
				# First, make a shuffled list of locations
				locations_list = []
				for key, value in self.locations.items():
					locations_list.append(value)
				random.shuffle(locations_list)
				# Iterate the shuffled list and pick the next one for the current player
				for location in locations_list:
					self.locations[location.location_id].bg_color = self.players[self.current_player].color
					self.players[self.current_player].total_locations += 1
					self.players[self.current_player].controlled_locations.append(location.location_id)
					self.locations[location.location_id].owner = self.current_player
					self.locations[location.location_id].armies += 1
					self.players[self.current_player].total_armies += 1
					self.next_player()
				self.next_phase()
			elif self.game_phase == "Allocate All Armies":
				# Randomly allocate the rest of the armies for each player
				while(self.players[2].total_armies < 50):
					# Pick a random location from this player's list
					random_location = random.choice(self.players[self.current_player].controlled_locations)
					# Increment that location and the player's total armies
					self.locations[random_location].armies += 1
					self.players[self.current_player].total_armies += 1
					
					self.next_player()
				self.next_phase()
		elif self.rps:
			self.rps.process_keydown(key)
			# Check if the RPS game is over
			if self.current_player == 1:
				if self.rps.player_one.lives == 2:
					# Player two wins as defender
					self.attacker.armies = self.rps.player_one.lives
					self.defender.armies = self.rps.player_two.lives
					self.rps = None
					self.next_phase()
				elif self.rps.player_two.lives == 0:
					# Player one wins as attacker
					self.attacker.armies = 1
					self.defender.armies = self.rps.player_one.lives - 1
					self.defender.owner = self.current_player
					self.defender.bg_color = self.players[1].color
					self.players[1].total_locations += 1
					self.players[2].total_locations -= 1
					self.players[1].controlled_locations.append(self.defender.location_id)
					self.players[2].controlled_locations.remove(self.defender.location_id)
					self.rps = None
					self.next_phase()
			else:
				if self.rps.player_one.lives < 1:
					# Player two wins as attacker
					self.attacker.armies = 1
					self.defender.armies = self.rps.player_two.lives - 1
					self.defender.owner = self.current_player
					self.defender.bg_color = self.players[2].color
					self.players[2].total_locations += 1
					self.players[1].total_locations -= 1
					self.players[2].controlled_locations.append(self.defender.location_id)
					self.players[1].controlled_locations.remove(self.defender.location_id)
					self.rps = None
					self.next_phase()
				elif self.rps.player_two.lives == 2:
					# Player one wins as defender
					self.attacker.armies = self.rps.player_two.lives
					self.defender.armies = self.rps.player_one.lives
					self.rps = None
					self.next_phase()

	def next_player(self):
		if self.current_player == 1:
			self.current_player = 2
		else:
			self.current_player = 1

	def check_if_game_over(self):
		if self.players[1].total_locations == 0:
			return True
		elif self.players[2].total_locations == 0:
			return True
		else:
			return False

	def update_armies_count(self):
		for key, player in self.players.items():
			armies = 0
			for location in player.controlled_locations:
				armies += self.locations[location].armies
			player.total_armies = armies

	def next_phase(self):
		if self.game_phase == "Pick Starting Countries":
			self.game_phase = "Allocate All Armies"
		elif self.game_phase == "Allocate All Armies":
			self.game_phase = "Choose Attacker"
		elif self.game_phase == "Choose Attacker":
			self.game_phase = "Choose Defender"
		elif self.game_phase == "Choose Defender":
			self.game_phase = "RPS"
		elif self.game_phase == "RPS" and self.rps == None:
			if self.check_if_game_over():
				self.game_phase = "Victory!"
			else:
				self.update_armies_count()
				self.game_phase = "Choose Attacker"
		elif self.game_phase == "Place New Armies":
			self.game_phase = "Choose Attacker"

		# Always clean out the situational text when changing phases
		self.situational_text = None

	def new_turn(self):
		self.next_player()
		self.placable_armies = 5
		self.game_phase = "Place New Armies"

	def process_mouseclick(self, mouse_pos):
		# mouse was clicked, do something

		# Logic during different phases
		if self.game_phase == "Pick Starting Countries":
			for key, location in self.locations.items():
				if location.is_hovered(mouse_pos[0], mouse_pos[1]):
					if location.owner == None:
						location.bg_color = self.players[self.current_player].color
						self.players[self.current_player].total_locations += 1
						self.players[self.current_player].controlled_locations.append(location.location_id)
						location.owner = self.current_player
						location.armies += 1
						self.players[self.current_player].total_armies += 1
						self.next_player()
			if len(self.players[1].controlled_locations) + len(self.players[2].controlled_locations) == 42:
				# All countries taken, start next phase
				self.next_phase()
		elif self.game_phase == "Allocate All Armies":
			for key, location in self.locations.items():
				if location.is_hovered(mouse_pos[0], mouse_pos[1]):
					if location.owner == self.current_player:
						location.armies += 1
						self.players[self.current_player].total_armies += 1
						self.next_player()
					else:
						self.situational_text = "Not your territory!"
			if self.players[2].total_armies == 50:
				self.next_phase()
		elif self.game_phase == "Choose Attacker":
			for key, location in self.locations.items():
				if location.is_hovered(mouse_pos[0], mouse_pos[1]):
					if location.owner == self.current_player:
						self.attacker = location
						self.next_phase()
					else:
						self.situational_text = "Not your territory!"
			if self.end_turn_button.is_hovered(mouse_pos[0], mouse_pos[1]):
				self.new_turn()
		elif self.game_phase == "Choose Defender":
			for key, location in self.locations.items():
				if location.is_hovered(mouse_pos[0], mouse_pos[1]):
					if location.owner != self.current_player:
						if location.location_id in self.attacker.neighbors:
							self.defender = location
							self.next_phase()
							if self.current_player == 1:
								self.rps = RPS(self.screen, self.attacker.armies, self.defender.armies)
							else:
								self.rps = RPS(self.screen, self.defender.armies, self.attacker.armies)
						else:
							self.situational_text = "Not a connected territory"
					else:
						self.situational_text = "Can't attack yourself!"
		elif self.game_phase == "RPS":
			# Time to play RPS to see who wins
			pass
		elif self.game_phase == "Place New Armies":
			for key, location in self.locations.items():
				if location.is_hovered(mouse_pos[0], mouse_pos[1]):
					if location.owner == self.current_player:
						location.armies += 1
						self.players[self.current_player].total_armies += 1
						self.placable_armies -= 1
			if self.placable_armies == 0:
				self.next_phase()




	def draw(self):
		if self.rps:
			self.rps.draw()
		else:
			# Fill in background color
			self.surface.fill(SHADOW)
			# Draw risk map
			self.surface.blit(self.img,(0,0))
			# Draw each location square
			for key, location in self.locations.items():
				location.draw()
			# Draw player stats
			for key, player in self.players.items():
				player.draw()
			# Draw current game state
			self.game_state_display.draw()
			# Draw end turn button
			mouse_pos = pygame.mouse.get_pos()
			self.end_turn_button.is_hovered(mouse_pos[0], mouse_pos[1])
			self.end_turn_button.draw()
			
			self.screen.blit(self.surface, (0, 0))

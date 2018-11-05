from constants import *
import pygame
from Location import Location

class Risk():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.img = pygame.transform.scale(
			pygame.image.load('2000px-Risk_board.svg.png').convert(),
			(1000,692)
		)
		self.locations = []
		# Locations below are in the format:
		# location_id, center_x, center_y, name, neighbors
		
		# North America
		self.locations.append(Location(self,1,80,112,"Alaska",[2,3,32]))
		self.locations.append(Location(self,2,168,112,"NW Territory",[1,3,4,6]))
		self.locations.append(Location(self,3,158,161,"Alberta",[1,2,4,7]))
		self.locations.append(Location(self,4,222,160,"Ontario",[2,3,5,6,7,8]))
		self.locations.append(Location(self,5,294,165,"Quebec",[4,6,8]))
		self.locations.append(Location(self,6,345,71,"Greenland",[2,4,5,15]))
		self.locations.append(Location(self,7,161,233,"Western US",[3,4,8,9]))
		self.locations.append(Location(self,8,237,247,"Eastern US",[4,5,7,9]))
		self.locations.append(Location(self,9,170,321,"Central America",[7,8,10]))
		# South America
		self.locations.append(Location(self,10,237,378,"Venezuela",[9,11,12]))
		self.locations.append(Location(self,11,227,450,"Peru",[10,12,13]))
		self.locations.append(Location(self,12,315,437,"Brazil",[10,11,13,25]))
		self.locations.append(Location(self,13,260,554,"Argentina",[11,12]))
		# Europe
		self.locations.append(Location(self,14,405,213,"Great Britain",[15,16,17,20]))
		self.locations.append(Location(self,15,433,143,"Iceland",[6,14,17]))
		self.locations.append(Location(self,16,499,230,"Northern Europe",[14,17,18,19,20]))
		self.locations.append(Location(self,17,504,139,"Scandinavia",[14,15,16,19]))
		self.locations.append(Location(self,18,512,290,"Southern Europe",[16,19,20,23,25,33]))
		self.locations.append(Location(self,19,584,195,"Ukraine",[16,17,18,27,33,37]))
		self.locations.append(Location(self,20,429,319,"Western Europe",[14,16,18,25]))
		# Africa
		self.locations.append(Location(self,21,542,502,"Congo",[22,25,26]))
		self.locations.append(Location(self,22,585,451,"East Africa",[21,23,24,25,26,33]))
		self.locations.append(Location(self,23,542,389,"Egypt",[18,22,25,33]))
		self.locations.append(Location(self,24,639,593,"Madagascar",[22,26]))
		self.locations.append(Location(self,25,464,424,"North Africa",[12,18,20,21,22,23]))
		self.locations.append(Location(self,26,546,590,"South Africa",[21,22,24]))
		# Asia
		self.locations.append(Location(self,27,673,257,"Afghanistan",[19,28,29,33,37]))
		self.locations.append(Location(self,28,782,300,"China",[27,29,34,35,36,37]))
		self.locations.append(Location(self,29,724,350,"India",[27,28,33,35]))
		self.locations.append(Location(self,30,801,180,"Irkutsk",[32,34,36,38]))
		self.locations.append(Location(self,31,916,245,"Japan",[32,34]))
		self.locations.append(Location(self,32,892,104,"Kamchatka",[1,30,31,34,38]))
		self.locations.append(Location(self,33,611,347,"Middle East",[18,19,22,23,27,29]))
		self.locations.append(Location(self,34,814,240,"Mongolia",[28,30,31,32,36]))
		self.locations.append(Location(self,35,804,378,"Siam",[28,29,41]))
		self.locations.append(Location(self,36,735,119,"Siberia",[27,28,30,34,37,38]))
		self.locations.append(Location(self,37,685,165,"Ural",[19,27,28,36]))
		self.locations.append(Location(self,38,815,95,"Yakutsk",[30,32,36]))
		# Australia
		self.locations.append(Location(self,39,922,544,"Eastern Australia",[40,42]))
		self.locations.append(Location(self,40,855,589,"Western Australia",[39,41,42]))
		self.locations.append(Location(self,41,820,485,"Indonesia",[35,40,42]))
		self.locations.append(Location(self,42,910,462,"New Guinea",[39,40,41]))

	def process_keydown(self, key):
		# Not sure how keyboard will interact yet, so just do nothing for now
		pass

	def process_mouseclick(self, mouse_pos):
		# mouse was clicked, do something
		for location in self.locations:
			if location.is_hovered(mouse_pos[0], mouse_pos[1]):
				location.armies += 1
				location.bg_color = BLUE

	def draw(self):
		self.surface.fill(SHADOW)
		self.surface.blit(self.img,(0,0))
		for location in self.locations:
			location.draw()
		self.screen.blit(self.surface, (0, 0))

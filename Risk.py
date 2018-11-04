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
		# North America
		self.locations.append(Location(self,1,80,112,"Alaska"))
		self.locations.append(Location(self,2,168,112,"NW Territory"))
		self.locations.append(Location(self,3,158,161,"Alberta"))
		self.locations.append(Location(self,4,222,160,"Ontario"))
		self.locations.append(Location(self,5,294,165,"Quebec"))
		self.locations.append(Location(self,6,345,71,"Greenland"))
		self.locations.append(Location(self,7,161,233,"Western US"))
		self.locations.append(Location(self,8,237,247,"Eastern US"))
		self.locations.append(Location(self,9,170,321,"Central America"))
		# South America
		self.locations.append(Location(self,10,237,378,"Venezuela"))
		self.locations.append(Location(self,11,227,450,"Peru"))
		self.locations.append(Location(self,12,315,437,"Brazil"))
		self.locations.append(Location(self,13,260,554,"Argentina"))
		# Europe
		self.locations.append(Location(self,14,405,213,"Great Britain"))
		self.locations.append(Location(self,15,433,143,"Iceland"))
		self.locations.append(Location(self,16,499,230,"Northern Europe"))
		self.locations.append(Location(self,17,504,139,"Scandinavia"))
		self.locations.append(Location(self,18,512,290,"Southern Europe"))
		self.locations.append(Location(self,19,584,195,"Ukraine"))
		self.locations.append(Location(self,20,429,319,"Western Europe"))
		# Africa
		self.locations.append(Location(self,21,542,502,"Congo"))
		self.locations.append(Location(self,22,585,451,"East Africa"))
		self.locations.append(Location(self,23,542,389,"Egypt"))
		self.locations.append(Location(self,24,639,593,"Madagascar"))
		self.locations.append(Location(self,25,464,424,"North Africa"))
		self.locations.append(Location(self,26,546,590,"South Africa"))
		# Asia
		self.locations.append(Location(self,27,673,257,"Afghanistan"))
		self.locations.append(Location(self,28,782,300,"China"))
		self.locations.append(Location(self,29,724,350,"India"))
		self.locations.append(Location(self,30,801,180,"Irkutsk"))
		self.locations.append(Location(self,31,916,245,"Japan"))
		self.locations.append(Location(self,32,892,104,"Kamchatka"))
		self.locations.append(Location(self,33,611,347,"Middle East"))
		self.locations.append(Location(self,34,814,240,"Mongolia"))
		self.locations.append(Location(self,35,804,378,"Siam"))
		self.locations.append(Location(self,36,735,119,"Siberia"))
		self.locations.append(Location(self,37,685,165,"Ural"))
		self.locations.append(Location(self,38,815,95,"Yakutsk"))
		# Australia
		self.locations.append(Location(self,39,922,544,"Eastern Australia"))
		self.locations.append(Location(self,40,855,589,"Western Australia"))
		self.locations.append(Location(self,41,820,485,"Indonesia"))
		self.locations.append(Location(self,42,910,462,"New Guinea"))

	def process_keydown(self, key):
		pass

	def draw(self):
		self.surface.fill(SHADOW)
		self.surface.blit(self.img,(0,0))
		for location in self.locations:
			location.draw()
		self.screen.blit(self.surface, (0, 0))

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
		self.locations.append(Location(self,80,112,"Alaska"))
		self.locations.append(Location(self,168,112,"NW Territory"))
		self.locations.append(Location(self,158,161,"Alberta"))
		self.locations.append(Location(self,222,160,"Ontario"))
		self.locations.append(Location(self,294,165,"Quebec"))
		self.locations.append(Location(self,345,71,"Greenland"))
		self.locations.append(Location(self,161,233,"Western US"))
		self.locations.append(Location(self,237,247,"Eastern US"))
		self.locations.append(Location(self,170,321,"Central America"))
		# South America
		self.locations.append(Location(self,237,378,"Venezuela"))
		self.locations.append(Location(self,227,450,"Peru"))
		self.locations.append(Location(self,315,437,"Brazil"))
		self.locations.append(Location(self,260,554,"Argentina"))
		# Europe
		self.locations.append(Location(self,405,213,"Great Britain"))
		self.locations.append(Location(self,433,143,"Iceland"))
		self.locations.append(Location(self,499,230,"Northern Europe"))
		self.locations.append(Location(self,504,139,"Scandinavia"))
		self.locations.append(Location(self,512,290,"Southern Europe"))
		self.locations.append(Location(self,584,195,"Ukraine"))
		self.locations.append(Location(self,429,319,"Western Europe"))
		# Africa
		self.locations.append(Location(self,542,502,"Congo"))
		self.locations.append(Location(self,585,451,"East Africa"))
		self.locations.append(Location(self,542,389,"Egypt"))
		self.locations.append(Location(self,639,593,"Madagascar"))
		self.locations.append(Location(self,464,424,"North Africa"))
		self.locations.append(Location(self,546,590,"South Africa"))
		# Asia
		self.locations.append(Location(self,673,257,"Afghanistan"))
		self.locations.append(Location(self,782,300,"China"))
		self.locations.append(Location(self,724,350,"India"))
		self.locations.append(Location(self,801,180,"Irkutsk"))
		self.locations.append(Location(self,916,245,"Japan"))
		self.locations.append(Location(self,892,104,"Kamchatka"))
		self.locations.append(Location(self,611,347,"Middle East"))
		self.locations.append(Location(self,814,240,"Mongolia"))
		self.locations.append(Location(self,804,378,"Siam"))
		self.locations.append(Location(self,735,119,"Siberia"))
		self.locations.append(Location(self,685,165,"Ural"))
		self.locations.append(Location(self,815,95,"Yakutsk"))
		# Australia
		self.locations.append(Location(self,922,544,"Eastern Australia"))
		self.locations.append(Location(self,855,589,"Western Australia"))
		self.locations.append(Location(self,820,485,"Indonesia"))
		self.locations.append(Location(self,910,462,"New Guinea"))

	def process_keydown(self, key):
		pass

	def draw(self):
		self.surface.fill(SHADOW)
		self.surface.blit(self.img,(0,0))
		for location in self.locations:
			location.draw()
		self.screen.blit(self.surface, (0, 0))

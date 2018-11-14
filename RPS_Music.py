import pygame

class RPS_Music():
	def play(self):
		pygame.mixer.music.load('assets/Holst-Mars-Public-Domain.ogg')
		pygame.mixer.music.queue('assets/Tchaikovsky-1812_overture-Public-Domain.ogg')
		pygame.mixer.music.queue('assets/Wagner-Tristan_und_Isolde-Public-Domain.ogg')
		pygame.mixer.music.play(-1)
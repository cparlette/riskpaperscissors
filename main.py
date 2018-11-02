import pygame
from Menu import Menu
from Button import Button
from constants import *
from Risk import Risk
from RPS import RPS


def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Risk Paper Scissors")
	done = False
	clock = pygame.time.Clock()

	### Menu Creation ###
	main_menu = Menu(screen, "Risk Paper Scissors!", WHITE, "tahoma", BLACK)

	main_menu.add_button("Risk", 200, 100, WHITE, str("Risk"), BLACK, WIDTH / 2, (2 * HEIGHT / 5))
	main_menu.add_button("RPS", 200, 100, WHITE, str("RPS"), BLACK, WIDTH / 2, (3 * HEIGHT / 5))
	main_menu.add_button("Quit", 200, 100, WHITE, str("Quit"), BLACK, WIDTH / 2, (4 * HEIGHT / 5))
 
	### Game Init ###
	risk = Risk()
	rps = RPS(screen)
	game = None

	# Assign starting menu (set to None for no starting menu)
	menu = main_menu
 
	### Main Game Loop ###
	while not done:
		# Update mouse location
		mouse_pos = pygame.mouse.get_pos()
 
		### Event Loop  ###
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # window is closed
				done = True
 
			elif menu:
				if event.type == pygame.KEYDOWN:
					# press esc key to return to main menu
					if event.key == pygame.K_ESCAPE:
						if menu == main_menu:
							done = True
						else:
							menu = main_menu
				elif event.type == pygame.MOUSEBUTTONUP and menu:
					action = menu.is_button_clicked(mouse_pos)
					if action == "Quit":
						done = True
					elif action == "Risk":
						menu = None
						game = risk
					elif action == "RPS":
						menu = None
						game = rps
					elif action == "Main Menu":
						menu = main_menu
			else:
				# we're in a game
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						# go back to the main menu
						game = None
						menu = main_menu
					else:
						# pass the key to the game
						game.process_keydown(event.key)
				else:
					# mouse input
					# maybe add processing here, for now just keyboard
					pass
 
		### Draw screen ###
		screen.fill(WHITE)  # clear screen
 
		# check if there is currently a menu selected
		if menu:
			menu.draw()
		else:
			game.draw()
 
		# display the screen
		pygame.display.flip()
 
		# delay in miliseconds until next frame
		clock.tick(24)
 

if __name__ == "__main__":
	pygame.init()
	main()
	pygame.quit()

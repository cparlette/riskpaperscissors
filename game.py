import pygame
from Menu import Menu
from Button import Button
from constants import *


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
 
	settings_menu = Menu(screen, "Settings", WHITE, "tahoma", BLACK)
 
	settings_menu.add_button("Main Menu", 300, 100, WHITE, str("Main Menu"), BLACK, WIDTH / 2, HEIGHT / 2)
 
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
 
			elif event.type == pygame.KEYDOWN:
				# press esc key to return to main menu
				if event.key == pygame.K_ESCAPE:
					if menu == main_menu:
						menu = None
					else:
						menu = main_menu
			elif event.type == pygame.MOUSEBUTTONUP and menu:
				action = menu.is_button_clicked(mouse_pos)
				if action == "Quit":
					done = True
				elif action == "Game":
					menu = None
				elif action == "Settings":
					menu = settings_menu
				elif action == "Main Menu":
					menu = main_menu
 
		if not menu:
			#---- game update code ----#
			pass
 
		### Draw  Game ###
		screen.fill(WHITE)  # clear screen
 
		# check if there is currently a menu selected
		if menu:
			menu.draw()
		else:
			#---- game draw code ----#
			pass
 
		# display the screen
		pygame.display.flip()
 
		# delay in miliseconds until next frame
		clock.tick(24)
 

if __name__ == "__main__":
	pygame.init()
	main()
	pygame.quit()

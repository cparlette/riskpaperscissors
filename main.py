import pygame
from Menu import Menu
from constants import *
from Risk import Risk
from RPS import RPS
from RPS_Music import RPS_Music

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Risk Paper Scissors")
	done = False
	clock = pygame.time.Clock()

	music = RPS_Music()
	music.play()

	# Config settings
	player1_name = "Player1"
	player2_name = "Player2"

	### Menu Creation ###
	main_menu = Menu(screen, "Risk Paper Scissors!", WHITE, "tahoma", BLACK)
	main_menu.add_button("Risk", 200, 100, WHITE, str("Risk"), BLACK, WIDTH / 2, (HEIGHT * 2 / 6))
	main_menu.add_button("Settings", 200, 100, WHITE, str("Settings"), BLACK, WIDTH / 2, (HEIGHT * 3 / 6))
	main_menu.add_button("Help", 200, 100, WHITE, str("Help"), BLACK, WIDTH / 2, (HEIGHT * 4 / 6))
	main_menu.add_button("Quit", 200, 100, WHITE, str("Quit"), BLACK, WIDTH / 2, (HEIGHT * 5 / 6))
 
	settings_menu = Menu(screen, "Settings", WHITE, "tahoma", BLACK)
	settings_menu.add_textbox("Player 1 Name", player1_name, WIDTH / 2, HEIGHT * 2 / 6, BLUE)
	settings_menu.add_textbox("Player 2 Name", player2_name, WIDTH / 2, HEIGHT * 3 / 6, RED)
	settings_menu.add_button("Main Menu", 200, 100, WHITE, str("Main Menu"), BLACK, WIDTH / 2, HEIGHT * 5 / 6)

	help_menu = Menu(screen, "Help", WHITE, "tahoma", BLACK)
	help_menu.add_button("Main Menu", 200, 100, WHITE, str("Main Menu"), BLACK, WIDTH / 2, HEIGHT / 2)

	### Game Init ###
	#risk = Risk(screen)
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
					elif menu == settings_menu:
						menu.process_keydown(event)
				elif event.type == pygame.MOUSEBUTTONUP and menu:
					action = menu.is_button_clicked(mouse_pos)
					textbox_clicked = menu.is_textbox_clicked(mouse_pos)
					if action == "Quit":
						done = True
					elif action == "Risk":
						player1_name = settings_menu.textboxes[0].text
						player2_name = settings_menu.textboxes[1].text
						menu = None
						game = Risk(screen, player1_name, player2_name)
					elif action == "Settings":
						menu = settings_menu
					elif action == "Help":
						menu = help_menu
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
				elif event.type == pygame.MOUSEBUTTONUP:
					# pass mouse position into the game
					game.process_mouseclick(mouse_pos)
				else:
					# anything but a keyboard press or mouse click
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

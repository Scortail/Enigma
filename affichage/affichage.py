import pygame
from menu import menu

pygame.init()

# Variables globals
Width = 1600
Height = 900
Screen = pygame.display.set_mode((Width, Height))
rect_size = (300,150)


# Create fonts
Bold = pygame.font.SysFont("FreeMono", 25, bold=True)
Title_font = pygame.font.SysFont("FreeMono", 35, bold=True)


main = menu()

# Main loop
play = True
in_menu = True
while play:


    Screen.fill("#333333") 
    if in_menu == True:
        menu.draw(main,Screen,Width, Height, rect_size, Bold,Title_font)

    # Update screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Store mouse coordinate as a tuple (x, y)
            mouse = pygame.mouse.get_pos()

            if (Width-rect_size[0])/2 <= mouse[0] <= (Width+rect_size[0])/2:
                if 200 <= mouse[1] <= 350:
                    print("Cesar")
                    in_menu = False

                elif 400 <= mouse[1] <= 550:
                    print("Vigenere")
                    in_menu = False

                elif 600 <= mouse[1] <= 750:
                    print("Enigma")
                    in_menu = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                in_menu = True
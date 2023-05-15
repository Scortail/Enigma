import pygame
from menu import menu
from affichageCesar import Cesar
import cesar

pygame.init()

# Variables globals
Width = 1600
Height = 900
Screen = pygame.display.set_mode((Width, Height))
menu_rect_size = (300,150)
cesar_rect_size = (50,50)
alphabet = cesar.alphabet


# Create fonts
Bold = pygame.font.SysFont("FreeMono", 25, bold=True)
Title_font = pygame.font.SysFont("FreeMono", 35, bold=True)


main = menu()
cesar_afficher = Cesar()

# Main loop
play = True
in_menu = True
while play:


    Screen.fill("#333333") 
    if in_menu == True:
        main.draw(Screen,Width, Height, menu_rect_size, Bold,Title_font)

    # Update screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
    mouse = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONUP:
        if (Width-menu_rect_size[0])/2 <= mouse[0] <= (Width+menu_rect_size[0])/2:

            # Chiffrer Cesar
            if 200 <= mouse[1] <= 275:
                in_menu = False
                chiffrer_cesar = True
                choix = False
                input = ""
                output = ""
                decalage = ""
                while chiffrer_cesar:
                    Screen.fill("#333333")
                    # On demande le decalage
                    while not choix:
                        Screen.fill("#333333")

                        text = "Quelle est le decalage?"
                        text = Bold.render(text, True, "grey")
                        text_box = text.get_rect()
                        text_box.center = (Width // 2, Height // 1/4) 
                        Screen.blit(text, text_box)

                        text = Bold.render(decalage, True, "light blue")
                        text_box = text.get_rect()
                        text_box.center = (Width // 2, Height // 1/4+50) 
                        Screen.blit(text, text_box)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                choix = True
                                chiffrer_cesar = False
                                in_menu = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_DELETE:
                                    if decalage != "":
                                        decalage = decalage[:-1]
                                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                                    decalage += event.unicode

                                elif event.key == pygame.K_RETURN and decalage!="":
                                    choix = True
                        pygame.display.flip()
                    decalage = int(decalage)


                    # On affiche cesar
                    Screen.fill("#333333")                                
                    cesar_afficher.draw(Screen,Width, Height, cesar_rect_size, Bold,Title_font, decalage)
                    if len(input) > 0:
                        print(input,"ok")
                        if coordonnees1:
                            pygame.draw.line(Screen, "red", coordonnees1, coordonnees2, width=5)

                    # text input
                    text = Bold.render(input, True, "white")
                    text_box = text.get_rect(center= (Width/2, 50))
                    Screen.blit(text, text_box)

                    # text output
                    text = Bold.render(output, True, "grey")
                    text_box = text.get_rect(center= (Width/2, 100))
                    Screen.blit(text, text_box)

                    pygame.display.flip()

                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                chiffrer_cesar = False
                                in_menu = True

                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_DELETE:
                                    if input != "":
                                        input = input[:-1]  
                                        output = output[:-1]                                     
                                else:
                                    key = event.unicode
                                    if key in alphabet.lower() or key in alphabet.upper():
                                        input = input + key
                                        output = output + cesar.chiffrer(key, decalage)
                                        for i in range(len(alphabet)):
                                            if key == alphabet[i].lower() or key == alphabet[i].upper():
                                                coordonnees1 = (125 + cesar_rect_size[0] * (i+1),300)
                                                coordonnees2 = (125 + cesar_rect_size[0] * (i+1),500)


            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    chiffrer_cesar = False
                    in_menu = True

    #         # Dechiffrer Cesar
    #         elif 275 <= mouse[1] <= 350:
    #             cesar.afficherCesar(Screen,Width, Height, cesar_rect_size, Bold,Title_font)

    #         elif 400 <= mouse[1] <= 550:
    #             print("Vigenere")
    #             in_menu = False

    #         elif 600 <= mouse[1] <= 750:
    #             print("Enigma")
    #             in_menu = False

    # elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_z:
    #         in_menu = True
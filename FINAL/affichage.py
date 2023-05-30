import pygame
from menu import menu
from affichageCesar import Cesar
import cesar
import vigenere
import enigma
from affichageVigenere import Vigenere
from affichageEnigma import Enigma

pygame.init()

# Variables globals
Width = 1600
Height = 900
Screen = pygame.display.set_mode((Width, Height))
menu_rect_size = (300,150)
cesar_rect_size = (50,50)
alphabet = cesar.alphabet


# Paramètre de Enigma
Rotor1 = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "D"]
Rotor2 = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"]
Rotor3 = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"]

pos_rotor1 = "A"
pos_rotor2 = "A"
pos_rotor3 = "A"

ReflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"
ReflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

cablage = []


# Create fonts
Bold = pygame.font.SysFont("FreeMono", 25, bold=True)
Title_font = pygame.font.SysFont("FreeMono", 35, bold=True)


main = menu()
cesar_afficher = Cesar()
vigenere_afficher = Vigenere()
enigma_afficher = Enigma()

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
                                elif event.key == pygame.K_RETURN and decalage!="":
                                    choix = True
                                else:
                                    key = event.unicode 
                                    if key in ["1","2","3","4","5","6","7","8","9"]:
                                        decalage += key

                        pygame.display.flip()
                    decalage = int(decalage)

                    # On affiche cesar
                    Screen.fill("#333333")                                
                    cesar_afficher.draw(Screen,Width, Height, cesar_rect_size, Bold,Title_font)
                    if len(input) > 0 and input != " ":
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
                                        if len(input)>0:
                                            for i in range(len(alphabet)):
                                                if alphabet[i] == input[-1]:
                                                    coordonnees1 = (125 + cesar_rect_size[0] * (i+1),300)
                                                    coordonnees2 = (125 + cesar_rect_size[0] * ((i+1+decalage)%len(alphabet)),500)                                   
                                else:
                                    key = event.unicode
                                    if key == " ":
                                        input += " "
                                        output += " "
                                    elif key in alphabet.lower() or key in alphabet.upper():
                                        input = input + key
                                        output = output + cesar.chiffrer(key, decalage)
                                        for i in range(len(alphabet)):
                                            if key == alphabet[i].lower() or key == alphabet[i].upper():
                                                coordonnees1 = (125 + cesar_rect_size[0] * (i+1),300)
                                                coordonnees2 = (125 + cesar_rect_size[0] * ((i+1+decalage)%len(alphabet)),500)

            # Dechiffrer Cesar
            elif 275 <= mouse[1] <= 350:
                in_menu = False
                decrypter_cesar = True
                input = ""
                output = ""
                while decrypter_cesar:
                    Screen.fill("#333333")

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
                            decrypter_cesar = False
                            in_menu = True

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DELETE:
                                    if input != "":
                                        input = input[:-1]  
                                        output = output[:-1]
                            
                            if event.key == pygame.K_RETURN:
                                output = cesar.decrypter(input)

                            else:
                                key = event.unicode
                                if key == " ":
                                    input += " "
                                elif key in alphabet.lower() or key in alphabet.upper():
                                    input = input + key

            # Chiffrer Vigenère
            elif 400 <= mouse[1] <= 475:
                in_menu = False
                chiffrer_vigenere = True
                choix = False
                input = ""
                output = ""
                cle = ""
                while chiffrer_vigenere:
                    Screen.fill("#333333")
                    # On demande la cle
                    while not choix:
                        Screen.fill("#333333")

                        text = "Quelle est la cle?"
                        text = Bold.render(text, True, "grey")
                        text_box = text.get_rect()
                        text_box.center = (Width // 2, Height // 1/4) 
                        Screen.blit(text, text_box)

                        text = Bold.render(cle, True, "light blue")
                        text_box = text.get_rect()
                        text_box.center = (Width // 2, Height // 1/4+50) 
                        Screen.blit(text, text_box)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                choix = True
                                chiffrer_vigenere = False
                                in_menu = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_DELETE:
                                    if cle != "":
                                        cle = cle[:-1]
                                elif event.key == pygame.K_RETURN and cle!="":
                                    choix = True
                                else:
                                    key = event.unicode 
                                    if key in alphabet:
                                        cle += key

                        pygame.display.flip()

                    # On affiche vigenere
                    Screen.fill("#333333")                                
                    vigenere_afficher.draw(Screen,Width, Height, cesar_rect_size, Bold,Title_font)
                    if len(input) > 0 and input != " ":
                        if coordonnees1:
                            pygame.draw.line(Screen, "red", coordonnees1, coordonnees2, width=5)
                            pygame.draw.line(Screen, "red", coordonnees3, coordonnees4, width=5)

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
                                chiffrer_vigenere = False
                                in_menu = True

                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_DELETE:
                                    if input != "":
                                        input = input[:-1]  
                                        output = output[:-1]
                                        if len(input)>0:
                                            for i in range(len(alphabet)):
                                                if alphabet[i] == input[-1]:
                                                    coordonnees1 = (125 + cesar_rect_size[0] * (i+1),300)
                                                    coordonnees2 = (125 + cesar_rect_size[0] * ((i+1+decalage)%len(alphabet)),500)                                   
                                else:
                                    key = event.unicode
                                    if key == " ":
                                        input += " "
                                        output += " "
                                    elif key in alphabet.lower() or key in alphabet.upper():
                                        lettre_cle = cle[len(input)%len(cle)]
                                        input = input + key
                                        output = output + vigenere.chiffrer(key, lettre_cle)
                                        for i in range(len(alphabet)):
                                            if key == alphabet[i].lower() or key == alphabet[i].upper():
                                                coordonnees1 = (125 + cesar_rect_size[0] * (i+1),300)
                                            if lettre_cle == alphabet[i].lower() or lettre_cle == alphabet[i].upper():
                                                coordonnees2 = (125 + cesar_rect_size[0] * (i+1),500)
                                                coordonnees3 = (125 + cesar_rect_size[0] * (i+1),550)
                                            if output[-1] == alphabet[i].lower() or output[-1] == alphabet[i].upper():
                                                coordonnees4 = (125 + cesar_rect_size[0] * (i+1),750)
                                        
            # Decrypter Vigenere
            elif 475 <= mouse[1] <= 550:
                in_menu = False
                decrypter_vigenere = True
                input = ""
                output = ""
                while decrypter_vigenere:
                    Screen.fill("#333333")

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
                            decrypter_vigenere = False
                            in_menu = True

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DELETE:
                                    if input != "":
                                        input = input[:-1]  
                                        output = output[:-1]
                            
                            if event.key == pygame.K_RETURN:
                                output = vigenere.decrypter(input)

                            else:
                                key = event.unicode
                                if key == " ":
                                    input += " "
                                elif key in alphabet.lower() or key in alphabet.upper():
                                    input = input + key   

            # Chiffrer Enigma
            elif 600 <= mouse[1] <= 750:

                # On initialise nos rotors
                rotor1 = enigma.pos_init_rotor(Rotor1, pos_rotor1)
                alphabet_rotor1 = enigma.pos_init_rotor(enigma.alphabet, pos_rotor1)
                rotor2 = enigma.pos_init_rotor(Rotor2, pos_rotor2)
                alphabet_rotor2 = enigma.pos_init_rotor(enigma.alphabet, pos_rotor2)
                rotor3 = enigma.pos_init_rotor(Rotor3, pos_rotor3)
                alphabet_rotor3 = enigma.pos_init_rotor(enigma.alphabet, pos_rotor3)
                rotors = [rotor1, rotor2, rotor3]
                alphabets = [alphabet_rotor1, alphabet_rotor2, alphabet_rotor3]
                
                in_menu = False
                chiffrer_enigma = True
                input = ""
                output = ""
                path = []
                while chiffrer_enigma :
                    # On affiche enigma
                    Screen.fill("#333333")

                    enigma_afficher.draw(Screen, Bold, cablage, rotors, alphabets, ReflectorA, path)

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
                                chiffrer_enigma = False
                                in_menu = True

                            elif event.type == pygame.KEYDOWN:                    
                                key = event.unicode
                                if key == " ":
                                    input += " "
                                    output += " "
                                elif key in alphabet.lower() or key in alphabet.upper():
                                    input = input + key.upper()
                                    lettre_chiffrer, rotors,  alphabets, path = enigma.chiffrer(key.upper(), rotors, alphabets, cablage, ReflectorA)
                                    output += lettre_chiffrer
                                            



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
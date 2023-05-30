import enigma
import pygame

class Enigma:

    def draw(self, screen, font1, plugboard, rotors, alphabets, reflector, path):

        # Keyboard

        # Rectangle
        rectangle = pygame.Rect(1262.5, 200, 137.5, 600)
        pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

        # Lettre
        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font1.render(letter, True, "grey")
            text_box = letter.get_rect(center= (1262.5+137.5/2, 200+(i+1)*600/27))
            screen.blit(letter, text_box)

        # Plugboard

        # Rectangle
        rectangle = pygame.Rect(1050, 200, 137.5, 600)
        pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

        # Lettre
        for i in range(26):

            # Coter gauche
            if plugboard:
                for pair in plugboard:
                    if pair[0] == enigma.alphabet[i]:
                        letter = pair[1]
            else :
                letter = enigma.alphabet[i]
            letter = font1.render(letter, True, "grey")
            text_box = letter.get_rect(center= (1050+137.5/4, 200+(i+1)*600/27))
            screen.blit(letter, text_box)

            # Coter droit
            letter = enigma.alphabet[i]
            letter = font1.render(letter, True, "grey")
            text_box = letter.get_rect(center= (1050+137.5*3/4, 200+(i+1)*600/27))
            screen.blit(letter, text_box)

        # Rotor

        for i in range(3):
            # Rectangle
            rectangle = pygame.Rect(412.5 + i*212.5, 200, 137.5, 600)
            pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

            # Lettre
            for j in range(26):

                # Coter gauche
                letter = alphabets[i][j]
                letter = font1.render(letter, True, "grey")
                text_box = letter.get_rect(center= ((412.5 + i*212.5)+137.5/4, 200+(j+1)*600/27))
                screen.blit(letter, text_box)

                # Coter droit
                letter = rotors[i][0][j]
                letter = font1.render(letter, True, "grey")
                text_box = letter.get_rect(center= ((412.5 + i*212.5)+137.5*3/4, 200+(j+1)*600/27))
                screen.blit(letter, text_box)


        # Reflector

        # Rectangle
        rectangle = pygame.Rect(200, 200, 137.5, 600)
        pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

        # Lettre
        for i in range(26):

            # Coter gauche
            letter = enigma.alphabet[i]
            letter = font1.render(letter, True, "grey")
            text_box = letter.get_rect(center= (200+137.5/4, 200+(i+1)*600/27))

            screen.blit(letter, text_box)

            # Coter droit
            letter = reflector[i]
            letter = font1.render(letter, True, "grey")
            text_box = letter.get_rect(center= (200+137.5*3/4, 200+(i+1)*600/27))
            screen.blit(letter, text_box)

        # Afficher le nom des composants
        names = ["Reflector", "Rotor 1", "Rotor 2", "Rotor 3", "Plugboard", "Key/Lamp"]
        y = 150
        for i in range(6):
            x = 268.75 + i*212.5
            title = font1.render(names[i], True, "White")
            text_box = title.get_rect(center = (x, y))
            screen.blit(title, text_box)

        # coordonné du passage(path)
        y = [200+(signal+1)*600/27 for signal in path]
        x = [1400-137.5/2] #keyboard
        for i in [4,3,2,1,0]: # forward
            x.append(200+i*(137.5+75)+137.5*3/4)
            x.append(200+i*(137.5+75)+137.5*1/4)
        x.append(200+137.5*3/4) # reflector
        for i in [1,2,3,4]: # backward
            x.append(200+i*(137.5+75)+137.5*1/4)
            x.append(200+i*(137.5+75)+137.5*3/4)
        x.append(1600-200-137.5/2) # lampboard


        # Afficher le passage
        if len(path) > 0:
            for i in range(1,21):
                if i < 10:
                    color = "green"
                elif i < 12:
                    color = "orange"
                else:
                    color = "red"
                start = (x[i-1], y[i-1])
                end = (x[i],y[i])
                pygame.draw.line(screen, color, start, end, width=5)


import cesar
import pygame

class Cesar:

    def draw(self, screen, width, height, rect_size, font1, font2, decalage):
        

        alphabet = cesar.alphabet



        # Alphabet display

        for i in range(len(alphabet)):
            rectangle = pygame.Rect(100 + rect_size[0] * (i+1), 250, rect_size[0], rect_size[1])
            pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

            lettre = alphabet[i]
            lettre = font1.render(lettre, True, "grey")
            text_box = lettre.get_rect()
            text_box.center = rectangle.center

            screen.blit(lettre, text_box)


        for i in range(len(alphabet)):
            rectangle = pygame.Rect(100 + rect_size[0] * (i+1), 500, rect_size[0], rect_size[1])
            pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

            lettre = alphabet[(i+decalage)%len(alphabet)]
            lettre = font1.render(lettre, True, "grey")
            text_box = lettre.get_rect()
            text_box.center = rectangle.center
            screen.blit(lettre, text_box)

        
        # # Name display
        # rectangle = pygame.Rect((width-rect_size[0])/2, height-100, rect_size[0], rect_size[1])
        # pygame.draw.rect(screen, "#333333", rectangle, width=2, border_radius=15)

        # Name = font1.render(Name, True, "black")
        # text_box = Name.get_rect(center= (width/2,rectangle.top + rect_size[1]/2))

        # screen.blit(Name, text_box)

    def afficherCesar(self, screen, width, height, rect_size, font1, font2) :
        chiffrer = True
        while chiffrer:
            screen.fill("#333333")
            decalage = ""

            text = "Quelle est le decalage?"
            text = font1.render(text, True, "grey")
            text_box = text.get_rect()
            text_box.center = (width // 2, height // 2) 
            screen.blit(text, text_box)

            # On verifie le decalage
            while not isinstance(decalage, int):
                try:
                    decalage = int(input())
                    break
                except ValueError:
                    textError = "Le décalage doit être un nombre entier. Veuillez réessayer."
                    text = font1.render(text, True, "red")
                    text_box = text.get_rect()
                    text_box.center = (width // 2, height // 4) 
                    screen.blit(text, text_box)
                 
            
            # # self.draw(self, screen, width, height, rect_size, font1, font2)
            # screen.flip()
            # for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             chiffrer = False

            # # text input
            # text = font1.render(Input, True, "white")
            # text_box = text.get_rect(center= (width/2, Margins["top"]/2))
            # screen.blit(text, text_box)

            # # text output
            # text = Bold.render(Output, True, "grey")
            # text_box = text.get_rect(center= (width/2, Margins["top"]/2 +20))
            # screen.blit(text, text_box)
            # Cesar.draw(self, screen, width, height, rect_size, font1, font2)

            

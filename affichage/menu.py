import pygame

class menu:
    def draw(self, screen, width, height, rect_size, font1, font2):
        
        Title = "Projet Enigma"
        Options = ["César", "Vigenère", "Enigma"]
        Name = "BEAURAIN Tom, AUDIE Cedric, DUBUC-TABOUT Amaury"


        # Title display
        rectangle = pygame.Rect((width-rect_size[0])/2, 50, rect_size[0], rect_size[1])
        pygame.draw.rect(screen, "#333333", rectangle, width=2, border_radius=15)

        Title = font2.render(Title, True, "white")
        text_box = Title.get_rect(center= (width/2, rectangle.top + rect_size[1]/2))

        screen.blit(Title, text_box)


        # Options display
        for i in range(1,4):

            rectangle = pygame.Rect((width-rect_size[0])/2, 200*i, rect_size[0], rect_size[1])
            pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

            text = Options[i-1]

            text = font1.render(text, True, "grey")
            text_box = text.get_rect(center= (width/2,275+((i-1)*200)))

            screen.blit(text, text_box)

        
        # Name display
        rectangle = pygame.Rect((width-rect_size[0])/2, height-100, rect_size[0], rect_size[1])
        pygame.draw.rect(screen, "#333333", rectangle, width=2, border_radius=15)

        Name = font1.render(Name, True, "black")
        text_box = Name.get_rect(center= (width/2,rectangle.top + rect_size[1]/2))

        screen.blit(Name, text_box)


        

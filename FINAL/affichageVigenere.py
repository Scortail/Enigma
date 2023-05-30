import cesar
import pygame

class Vigenere:

    def draw(self, screen, width, height, rect_size, font1, font2):
        

        alphabet = cesar.alphabet

        # Alphabet display
        for i in range(1,4):
            for j in range(len(alphabet)):
                rectangle = pygame.Rect(100 + rect_size[0] * (j+1), i*250, rect_size[0], rect_size[1])
                pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)
                lettre = alphabet[j]
                lettre = font1.render(lettre, True, "grey")
                text_box = lettre.get_rect()
                text_box.center = rectangle.center
                screen.blit(lettre, text_box)

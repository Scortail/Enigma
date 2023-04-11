import pygame

class Reflector:

    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal):
        """Cette fonction renvoie la nouvelle position du signal


    Parameter
    ---------
    signal : int
                position d'arriver du signal

    Returns
    -------
    signal : int
        nouvelle position du signal
        

    """
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def draw(self, screen, x, y, w, h, font):

        # Rectangle
        rectangle = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

        # Lettre
        for i in range(26):

            # Coter gauche
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center= (x+w/4, y+(i+1)*h/27))

            screen.blit(letter, text_box)

            # Coter droit
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center= (x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)
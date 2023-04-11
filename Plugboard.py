import pygame

class Plugboard:

    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.right.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]
        
    def forward(self, signal):
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
    
    def backward(self, signal):
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
        
        letter = self.left[signal]
        signal = self.right.find(letter)
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
import pygame

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Rotor:

    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def show(self):
        """Cette fonction affiche la configuration actuelle du rotor


    Parameter
    ---------
    None

    Returns
    -------
    None
        
    """
        
        print(self.left)
        print(self.right)
        print("")

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
    
    def rotate(self, n = 1, forward = True):
        """Cette fonction permet de faire tourner un rotor n fois


    Parameter
    ---------
    n : int
                nombre de decalage

    Returns
    -------
    None
        

    """
        
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]

            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]
                

    def rotate_to_letter(self, letter):
        n = alphabet.find(letter)
        self.rotate(n)

    def set_ring(self, n):

        # Tourne le rotor en arriere
        self.rotate(n-1, forward=False)

        # Ajuster le notch en fonction du wiring
        n_notch = alphabet.find(self.notch)
        self.notch = alphabet[(n_notch - n+1) %26]
        

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

            # Surligner les lettres
            if i ==0:
                pygame.draw.rect(screen, "orange", text_box, border_radius= 5)

            # Surligner le notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, "white", text_box, border_radius= 5)

            screen.blit(letter, text_box)

            # Coter droit
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center= (x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)
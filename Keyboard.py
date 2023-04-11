import pygame

class Keyboard:

    def forward(self, letter):
        """Cette fonction renvoie la position de la lettre


    Parameter
    ---------
    letter : string
                lettre entrez par l'utilisateur

    Returns
    -------
    signal : int
        position de la lettre

    Examples
    --------

    >>> forward("D")
    3

    >>> forward("G")
    6

    >>> forward("A")
    0

    """
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
    
    def draw(self, screen, x, y, w, h, font):

        # Rectangle
        rectangle = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", rectangle, width=2, border_radius=15)

        # Lettre
        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center= (x+w/2, y+(i+1)*h/27))
            screen.blit(letter, text_box)
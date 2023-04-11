import pygame

from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector
from Enigma import Enigma
from draw import draw


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulation")

# Create fonts
Bold = pygame.font.SysFont("FreeMono", 25, bold=True)


# Variable global
Width = 1600
Height = 900
Screen = pygame.display.set_mode((Width, Height))
Margins = {"top": 200, "bottom":100, "left":200, "right":200}
Gap = 75


Input = ""
Output = ""
Path = []

# Configuration historique des rotors et reflecteurs de enigma 
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Clavier et le Plugboard
KB = Keyboard()
PB = Plugboard(["AB","GD"])

# Machine enigma
enigma = Enigma(B,I,II,III,PB,KB)

# Set les positions des rotors
enigma.set_rings((3,3,3))

# set message cle
enigma.set_key("MCK")


# Chiffre un message
# message = "TESTENIGMAYOYOYO"
# message_chiffre = ""
# for letter in message:
#     message_chiffre += enigma.chiffrer(letter)
# print(message_chiffre)


play = True
while play:

    # Background colour
    Screen.fill("#333333")

    # text input
    text = Bold.render(Input, True, "white")
    text_box = text.get_rect(center= (Width/2, Margins["top"]/2))
    Screen.blit(text, text_box)

    # text output
    text = Bold.render(Output, True, "grey")
    text_box = text.get_rect(center= (Width/2, Margins["top"]/2 +20))
    Screen.blit(text, text_box)

    # Afficher la machine enigma
    draw(enigma, Path, Screen, Width, Height, Margins, Gap, Bold)


    # Update screen
    pygame.display.flip()

    # Suivre les input de l'utilisateur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key == pygame.K_SPACE:
                Input += " "
                Output += " "
            else:
                key = event.unicode
                if key in alphabet.lower():
                    letter = key.upper()
                    Input = Input + letter
                    Path, chiffrer = enigma.chiffrer(letter)
                    Output = Output + chiffrer
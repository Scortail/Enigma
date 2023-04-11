import pygame

def draw(enigma, path, screen, width,height, margins, gap, font):

    # largeur et hauteur des composants
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # coordonné du passage(path)
    y = [margins["top"]+(signal+1)*h/27 for signal in path]
    x = [width-margins["right"]-w/2] #keyboard
    for i in [4,3,2,1,0]: # forward
        x.append(margins["left"]+i*(w+gap)+w*3/4)
        x.append(margins["left"]+i*(w+gap)+w*1/4)
    x.append(margins["left"]+w*3/4) # reflector
    for i in [1,2,3,4]: # backward
        x.append(margins["left"]+i*(w+gap)+w*1/4)
        x.append(margins["left"]+i*(w+gap)+w*3/4)
    x.append(width-margins["right"]-w/2) # lampboard


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


    # coordonnées de base
    x = margins["left"]
    y = margins["top"]

    # enigma components
    for component in [enigma.refle, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap
    
    # Afficher le nom des composants
    names = ["Reflector", "Rotor 1", "Rotor 2", "Rotor 3", "Plugboard", "Key/Lamp"]
    y = margins["top"]*3/4
    for i in range(6):
        x = margins["left"] + w/2 + i*(w+gap)
        title = font.render(names[i], True, "White")
        text_box = title.get_rect(center = (x, y))
        screen.blit(title, text_box)


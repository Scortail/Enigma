import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import string

alphabet = string.ascii_lowercase

def chiffrer(chaine : str, decalage : int) -> str:
    """Cette fonction renvoie la chaine chiffrer en fonction du décalage

    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    decalage : int
                nombre de décalage sur l'alphabet
    
    Returns
    -------
    string
        chaine chiffrer

    Examples
    --------
    >>> chiffrer("hello world", 3)
    'khoor zruog'
    >>> chiffrer("zebre", 3)
    'cheuh'
    >>> chiffrer("bonjour", 3)
    'erqmrxu'
    """
    res = ''
    for i in range(len(chaine)):
        if chaine[i].lower() in alphabet:
            for j in range(len(alphabet)):
                    if alphabet[j] == chaine[i]:
                        total = j + decalage
                        total = total % len(alphabet)
                        res += alphabet[total]
                    elif alphabet[j] == chaine[i].lower():
                        total = j + decalage
                        total = total % len(alphabet)
                        res += alphabet[total].upper()
        else :
            res += chaine[i]
    return res


def dechiffrer_cesar(chaine : str, decalage : int) -> str:
    """Cette fonction renvoie la chaine déchiffrer en fonction du décalage

    Parameter
    ---------
    chaine : string
                chaine à déchiffrer
    decalage : int
                nombre de décalage sur l'alphabet
    
    Returns
    -------
    string
        chaine déchiffrer

    Examples
    --------
    >>> dechiffrer_cesar("khoor zruog", 3)
    'hello world'
    >>> dechiffrer_cesar("cheuh", 3)
    'zebre'
    >>> dechiffrer_cesar("erqmrxu", 3)
    'bonjour'
    """
    res = ""
    for i in range(len(chaine)):
        if chaine[i].lower() in alphabet:
            for j in range(len(alphabet)):
                    if alphabet[j] == chaine[i]:
                        total = j - decalage
                        total = total % len(alphabet)
                        res += alphabet[total]
                    elif alphabet[j] == chaine[i].lower():
                        total = j - decalage
                        total = total % len(alphabet)
                        res += alphabet[total].upper()
        else :
            res += chaine[i]
    return res


def frequence_apparitions(chaine):
    """Cette fonction renvoie une liste contenant la fréquence d'apparitions dans la chaine par ordre alphabetique

    Parameter
    ---------
    chaine : string
                chaine à décrypter
                
    Returns
    -------
    list
        liste de nombre

    Examples
    --------
    >>> frequence_apparitions('mh shxa wh yrlu')
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
    """
    apparitions = [0] * 26
    chaine = chaine.lower() 
    for i in range(len(chaine)):
        if chaine[i] not in alphabet: 
            continue
        else:
            apparitions[alphabet.index(chaine[i])] = apparitions[alphabet.index(chaine[i])] + 1 
    return apparitions


def cherche_decalage(chaine):
    """Cette fonction renvoie le decalage effectuer sur la chaine

    Parameter
    ---------
    chaine : string
                chaine à décrypter
                
    Returns
    -------
    int
        decalage

    Examples
    --------
    >>> cherche_decalage('mh shxa wh yrlu')
    3
    """
    francais = [942, 102, 264, 339, 1587, 95, 104, 77, 841, 89, 0, 534, 324, 715, 514, 286, 106, 646, 790, 726, 624, 215, 0, 30, 24, 32]
    liste = [0] * 26 
    for i in range(len(francais)):
        for j in range(26):
            frequences = frequence_apparitions(dechiffrer_cesar(chaine, j))
            liste[i] += frequences[i] * francais[j]
    return liste.index(max(liste)) 


def diagramme_baton(chaine):
    """Cette fonction renvoie la fréquence d'apparitions des lettre sous forme de diagramme

    Parameter
    ---------
    chaine : string
                chaine à décrypter

    Returns
    -------
    None
    """
    categories = []
    valeur = []
    liste = frequence_apparitions(chaine)   
    for i in range(len(liste)):  
        categories += alphabet[i]   
        valeur.append(liste[i])  
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained') 
    ax.set_title("Fréquence des lettres dans la chaine de caractères")
    ax.set_xlabel('Lettres')
    ax.set_ylabel("Nombres d'apparitions")
    plt.bar(categories, valeur) ; plt.show()


def decrypter(chaine):
    """Cette fonction renvoie la chaine déchiffrer sans connaitre le décalage

    Parameter
    ---------
    chaine : string
                chaine à décrypter

    Returns
    -------
    string
        chaine décrypter

    Examples
    --------
    >>> decrypter('mh shxa wh yrlu')
    'je peux te voir'
    """
    decalage = cherche_decalage(chaine)
    return dechiffrer_cesar(chaine, decalage)


# chaine = "uizqmIumtqm aqvabittm idmk ai umzm icxzma lm ai lmuq awmcz ti zmqvm Uizqm I kmbbm mxwycm tm owcdmzvmumvb jzmaqtqmv zmncam mv mnnmb lm zmkwvviqbzm tmvnivb kwuum umujzm i xizb mvbqmzm lm ti niuqttm quxmzqitm Vq mttm vq ai umzm tquxmzibzqkm lwciqzqmzm vm zmkwqdmvb lwvk ickcvm xmvaqwv lm ti xizb lm tMbib jzmaqtqmv Kmab amctmumvb idmk ti nqv lm ti zmomvkm jzmaqtqmvvm mb tmizzqdmm ic xwcdwqz lc lmuq"

print(chiffrer("a", 3))
# print(a)
# b = dechiffrer_cesar(chaine, 8)
# print(b)
# c = frequence_apparitions('Mh shxa wh yrlu!')
# print(c)
# e = decrypter("HHHH vdoxw!:;,atroepuydbzvwbxnvbsfqgdhfjkmpsalut")
# print(cherche_decalage('Mh shxa wh yrlu!'))
# print(e)
# diagramme_baton("HHHH vdoxw!:;,atroepuydbzvwbxnvbsfqgdhfjkmpsalut")

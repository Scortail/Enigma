import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from cesar import cherche_decalage,frequence_apparitions
import string

alphabet = string.ascii_lowercase

def chiffrer(chaine, cle):
    """Cette fonction renvoie la chaine chiffrer en fonction de la cle

    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    cle : str
                cle à appliquer sur la chaine
    
    Returns
    -------
    string
        chaine chiffrer

    Examples
    --------
    >>> chiffrer("hello world", lol)
    'sswwc hzfwo'
    """
    res = ''
    j = 0   # j va servir à ajouter + 1 que lorsqu'il n'y a pas d'espace
    for i in range(len(chaine)):   # Parcours lettre par lettre de la chaine a chiffrer
        if chaine[i] == ' ':   # Si il y a un espace mettre un espace  
            res += ' '
        else:
            total = alphabet.index(cle[j % len(cle)]) + alphabet.index(chaine[i])   # total = l'indice dans l'alphabet du caractere de la cle qui correspond à j % longueur de cle + l'indice dans l'alphabet du caractere de la chaine qui correspond à i
            total = total % len(alphabet)   # On fait un modulo sur le total au cas où le total > longueur de alphabet
            res += alphabet[total]   # On ajoute la lettre qui correspond
            j += 1   # on ajoute 1 à j
    return res


def dechiffrer(chaine, cle):
    """Cette fonction renvoie la chaine dechiffrer en fonction de la cle

    Parameter
    ---------
    chaine : string
                chaine à dechiffrer
    cle : str
                cle à appliquer sur la chaine
    
    Returns
    -------
    string
        chaine dechiffrer

    Examples
    --------
    >>> dechiffrer("sswwc hzfwo", lol)
    'hello world'
    """
    res = ''
    j = 0   # j va servir à ajouter + 1 que lorsqu'il n'y a pas d'espace
    for i in range(len(chaine)):   # Parcours lettre par lettre de la chaine a déchiffrer
        if chaine[i] == ' ':   # Si il y a un espace mettre un espace  
            res += ' '
        else:
            total = alphabet.index(chaine[i]) - alphabet.index(cle[j % len(cle)])   # total = l'indice dans l'alphabet du caractere de la chaine qui correspond à i - l'indice dans l'alphabet du caractere de la cle qui correspond à j % longueur de cle
            total = total % len(alphabet)   # On fait un modulo sur le total au cas où le total > longueur de alphabet
            res += alphabet[total]   # On ajoute la lettre qui correspond
            j += 1   # on ajoute 1 à j
    return res


def indice_coincidence(chaine):
    """Cette fonction renvoie l'indice de coincidence de la chaine

    Parameter
    ---------
    chaine : string
                chaine à décrypter
    
    Returns
    -------
    float
        indice de coincidence

    Examples
    --------
    >>> indice_coincidence()
    0.05176029020150553
    """
    apparitions = frequence_apparitions(chaine)   # On récupère les fréquences d'apparitions 
    somme = sum(n * (n - 1) for n in apparitions)   # On fait la somme de n * (n - 1) pour n de apparitions
    total_caractere = sum(apparitions)   # On recupère la somme des apparitions 
    return somme / (total_caractere * (total_caractere - 1))   # On retourne la somme divisé par (total_caractere * total_caractere - 1)


def liste_indice_coincidence(chaine, n):   # n = longueur de cle maximum
    """Cette fonction renvoie une liste contenant n indice de coincidence de la chaine

    Parameter
    ---------
    chaine : string
                chaine à décrypter
    
    n : int
                longueur cle maximum
    Returns
    -------
    list
        liste d'indice de coincidence

    Examples
    --------
    >>> liste_indice_coincidence(chaine, 2)
    [0.05176029020150553, 0, 0695399754379876]
    """
    res = [0]   # On créer une liste contenant de base 0
    for i in range(1, n + 1):   # Pour tout i allant de 1 à n + 1
        res.append(sum(indice_coincidence(chaine[j::i]) for j in range(i)) / i)   # On append la somme des indices de coincidence de la chaine à partir de j et de pas i pour tout j allant jusqu'à i le tout divisé par i
    return res


def affiche_graphe(chaine):
    """Cette fonction renvoie l'indice de coincidence pour chaque longueur de cle sous forme de graphe

    Parameter
    ---------
    chaine : string
                chaine à décrypter

    Returns
    -------
    None
    """
    liste = liste_indice_coincidence(chaine, 27)   # On creer une variable qui récupère le résultat de la fonction frequence_lettre()
    fig, ax = plt.subplots()   # Cf matplotlib doc
    ax.set_title("Indice de coincidence")   # On lui donne un titre
    ax.set_xlabel('Longueur de la cle')   # On donne un nom à l'axe des abscisse
    ax.set_ylabel("Indice de coincidence")   # On donne un nom à l'axe des ordonné
    ax.plot([i for i in range(len(liste))], liste)   # On créer une liste de 0 à 27 pour les abcsisses et on donne la liste pour les ordonnées
    plt.axis([0, 27, 0.05, 0.1])  # On dit que les abcsisses vont de 0 à 27 et les ordonnées de de 0.05 à 0.1
    plt.show()   # On affiche le graphique


def longueur_cle(chaine, seuil = 0.068, nmax = 27):   # nmax + 27 car le mot le plus long en français est : intergouvernementalisations
    """Cette fonction renvoie la longueur de la cle

    Parameter
    ---------
    chaine : string
                chaine à décrypter
    
    seuil : float
                seuil définis à l'avance

    nmax : int
                nmax définis à l'avance

    Returns
    -------
    int
        longueur de la cle

    Examples
    --------
    >>> longueur_cle(chaine, seuil = 0.068, nmax = 27)
    3
    """
    liste = liste_indice_coincidence(chaine, nmax)   # On créer une liste qui récupère la fonction liste_indice_coincidence(chaine, nmax)
    for i in range(len(liste)):   # On parcours la longueur de la liste
        if liste[i] > seuil:   # Si l'élément de la liste est supérieur au seuil
            return i   # On retourne i
        

def cherche_cle_vigenere(chaine, n):
    """Cette fonction renvoie la cle 

    Parameter
    ---------
    chaine : string
                chaine à décrypter
    
    n : int
                longueur de la cle

    Returns
    -------
    string
        cle

    Examples
    --------
    >>> cherche_cle_vigenere(chaine, 3)
    POE
    """
    liste = []
    res = ""
    chaine = chaine.replace(' ', '')   # On enlève les espace de la chaine
    for i in range(n):   # Pour i allant jusqu'à n
        liste.append(cherche_decalage(chaine[i::n]))   # On ajoute à la liste le résultat de la foncction cherche_decalage(chaine[i::n]) en commençant à i et de pas n
        res += chr(ord('a') + liste[i])   # On ajoute à res la valeur de ord('a') + liste[i] le tout qu'on transforme en lettre suivant l'ASCII
    return res


def decrypter(chaine):
    """Cette fonction renvoie la chaine décrypter 

    Parameter
    ---------
    chaine : string
                chaine à décrypter

    Returns
    -------
    string
        chaine décrypté

    Examples
    --------
    >>> decrypter("jppnz aqcpf")
    hello world
    """
    cle = cherche_cle_vigenere(chaine, longueur_cle(chaine))   # On récupère la cle de la chaine à décrypter
    return dechiffrer(chaine, cle)   # On retourne la fonction dechiffrer(chaine, cle)


chaine1 = 'eneffetlamemeconfigurationdefigurinesdansantesapparueadeuxreprisesetquejavaisdejarecopieesetrouvaitsurlaporte'
chaine2 = 'xgxyyxmetfxfxvhgybznktmbhgwxybznkbgxlwtgltgmxltiitknxtwxnqkxikblxlxmjnxctotblwxctkxvhibxxlxmkhnotbmlnketihkmx'
chaine3 = 'sorhzirowpqxjspthicgsbaisorhhsjgptggpghtqvxhygswtqvthiaotgsqxsvteytgxxcrpjmssvrswizeaorviisigwwjufirovaswefmcqmeswsswdzyiwscdeghmripxsvtaichujorswphokxhhtggwwjufihzihdpjgwxataswssttbhtbxsiktbmtrirvefiixrmdaithttiztbxthvtasswjxswtbktbigopxzrnotpghpixgsqdmiceytrihgensvhigrswhwztaichicgiswvxuipbxhimkorizihdvdpeqwpxhihhsjhihzihzecuytgujwzdiwhcriqscbytgnjgujogteytjsjgensdifsjjiaofdbrtaexghpbwasgwwjufifimccyhcgritthsjhiswjuwgjzxtogthivovssxpwxgswdzytdegzehwkcoxjfiasvtpyhgygzibcxzwhsbihhtdgwxppteytrecgppzecuytorvzexgihorhqiihirwvrcrhhecqiyoygomhqsbaicqibswtgwpwweovasweokccpthpttvpbexggdaqtsxpbxaswaorviihrecgptgujspaswjbtxfeishtgqtfwtgtpurdzihoygomiryastaiwcoxjfiazibsrisrusvbsvjbwtqvthhtqiihicoxjfibomhrecgptqehogiiiaxiefihiqpwujsptqvndxduvpaqtsxpwxpbkaomh'
# a = chiffrer("hello world", "lol")
# print(a)
# # b = dechiffrer("jppnz aqcpf", "cle")
# # print(b)
# # c = frequence_apparitions(chaine)
# # print(c)
# # d = indice_coincidence(chaine)
# # print(d)
# e = indice_coincidence(chaine3)
# print(e)
# print(liste_indice_coincidence('quvs n pb fvn asvs favwjrbnf tpueqhsj tbug jvt oagm b pnrgms dhn pescnn fm eue dhr daaoa wj tlrnroifaax uoht aeruvt qyo sbuuejt soh hvn fohlbig nhp bsfohzjr wufuvah bbyu ln fnwdiaagmpn qu pvj vnia wprgie hv pnrpsvrf rnwtueaax eu zog xsoc shfjt grbt doafveot grbt dozmhr oosfems ah svkoisinru qhua kpuyog uvua bbcbu duhr dhns fm bmvnpm ti sia wj avgh uvoa y isjt nufwjtbt fe kuftvjjcntvso', 27))
# affiche_graphe(chaine3)
# print(longueur_cle(chaine3))
# print(frequence_apparitions(chaine3))
# print(cherche_cle_cesar(chaine3))
# print(cherche_cle_vigenere('quvs n pb fvn asvs favwjrbnf tpueqhsj tbug jvt oagm b pnrgms dhn pescnn fm eue dhr daaoa wj tlrnroifaax uoht aeruvt qyo sbuuejt soh hvn fohlbig nhp bsfohzjr wufuvah bbyu ln fnwdiaagmpn qu pvj vnia wprgie hv pnrpsvrf rnwtueaax eu zog xsoc shfjt grbt doafveot grbt dozmhr oosfems ah svkoisinru qhua kpuyog uvua bbcbu duhr dhns fm bmvnpm ti sia wj avgh uvoa y isjt nufwjtbt fe kuftvjjcntvso', 6))
# print(decrypter('quvs n pb fvn asvs favwjrbnf tpueqhsj tbug jvt oagm b pnrgms dhn pescnn fm eue dhr daaoa wj tlrnroifaax uoht aeruvt qyo sbuuejt soh hvn fohlbig nhp bsfohzjr wufuvah bbyu ln fnwdiaagmpn qu pvj vnia wprgie hv pnrpsvrf rnwtueaax eu zog xsoc shfjt grbt doafveot grbt dozmhr oosfems ah svkoisinru qhua kpuyog uvua bbcbu duhr dhns fm bmvnpm ti sia wj avgh uvoa y isjt nufwjtbt fe kuftvjjcntvso'))
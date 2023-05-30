alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




def decalage_rotor(rotor, pos=1):
    """
    Cette fonction décale le rotor à gauche ou à droite en fonction de la position passée en paramètre.

    Parameters
    ----------
    rotor : str
        La chaîne de caractères représentant le rotor.
    pos : int, optional
        La position de décalage. Par défaut 1.

    Returns
    -------
    str
        La chaîne de caractères du rotor décalé.
    """
    rotor = rotor[pos:] + rotor[:pos]  # on prend tous les éléments jusqu'à pos et on les met à la fin
    return rotor


def pos_init_rotor(rotor, lettre):
    """
    Décale le rotor en fonction de la lettre initiale.

    Parameters
    ----------
    rotor : str
        La chaîne de caractères représentant le rotor.
    lettre : str
        La lettre initiale pour le rotor.

    Returns
    -------
    str
        La chaîne de caractères du rotor décalé.
    """
    lettre_index = alphabet.index(lettre)
    rotor = decalage_rotor(rotor, lettre_index)
    return rotor


def lettre_apres_cablage(indice, cablage):
    """
    Renvoie la lettre obtenue après le passage par le cablage.

    Parameters
    ----------
    lettre : str
        La lettre en entrée.

    Returns
    -------
    str
        La lettre obtenue après le passage par le cablage.
    """
    if cablage:
        for pair in cablage:
            if pair[0] == indice:
                return alphabet.index(pair[1])
    return indice


def lettre_apres_rotor(rotor, indice, alphabet_rotor):
    """
    Renvoie la lettre obtenue après le passage par le rotor.

    Parameters
    ----------
    rotor : str
        La configuration du rotor.
    indice : int
        L'indice de la lettre en entrée.

    Returns
    -------
    int
        L'indice de la lettre obtenue après le passage par le rotor.
    """
    lettre = rotor[indice]
    res_indice_lettre_rotor = alphabet_rotor.index(lettre)
    return  res_indice_lettre_rotor


def lettre_apres_rotor_inverse(rotor, indice, alphabet_rotor):
    """
    Renvoie la lettre obtenue après le passage par le rotor inverse.

    Parameters
    ----------
    rotor : str
        La configuration du rotor.
    indice : int
        L'indice de la lettre en entrée.

    Returns
    -------
    int
        L'indice de la lettre obtenue après le passage par le rotor inverse.
    """
    lettre_rotor = alphabet_rotor[indice]
    indice_lettre_alphabet = rotor.index(lettre_rotor)
    return  indice_lettre_alphabet


def lettre_apres_reflecteur(reflecteur, indice):
    """
    Renvoie la lettre obtenue après le passage par le reflecteur.

    Parameters
    ----------
    reflecteur : str
        La configuration du reflecteur.
    indice : int
        L'indice de la lettre en entrée.

    Returns
    -------
    int
        L'indice de la lettre obtenue après le passage par le reflecteur.
    """
    lettre = alphabet[indice]
    indice_lettre_apres_reflecteur = alphabet.index(alphabet[reflecteur.index(lettre)])
    return indice_lettre_apres_reflecteur


def chiffrer(lettre, rotors, alphabets, cablage, reflecteur):
    """
    Chiffre une lettre en utilisant les rotors, le reflecteur et le cablage.

    Parameters
    ----------
    lettre : str
        La lettre à chiffrer.

    Returns
    -------
    str
        La lettre chiffrée.
    """
    lettre1 = rotors[0][1]
    lettre2 = rotors[1][1]
    lettre3 = rotors[2][1]
    rotor1 = rotors[0][0]
    rotor2 = rotors[1][0]
    rotor3 = rotors[2][0]

    path = [alphabet.index(lettre), alphabet.index(lettre)]

    if lettre == " ":
        mot_chiffre += " "
    else:
        rotor3 = decalage_rotor(rotor3)
        alphabets[2] = decalage_rotor(alphabets[2])
        if rotor3[0] == lettre3:
            rotor2 = decalage_rotor(rotor2)
            alphabets[1] = decalage_rotor(alphabets[1])

            if rotor2[0] == lettre2:
                rotor1 = decalage_rotor(rotor1)
                alphabets[0] = decalage_rotor(alphabets[0])

        res = alphabet.index(lettre)
        res = lettre_apres_cablage(res, cablage)
        path.append(res)
        path.append(res)
        res = lettre_apres_rotor(rotor3, res, alphabets[2])
        path.append(res)
        path.append(res)
        res = lettre_apres_rotor(rotor2, res, alphabets[1])
        path.append(res)
        path.append(res)
        res = lettre_apres_rotor(rotor1, res, alphabets[0])
        path.append(res)
        path.append(res)
        res = lettre_apres_reflecteur(reflecteur, res)
        path.append(res)
        path.append(res)
        path.append(res)
        res = lettre_apres_rotor_inverse(rotor1, res, alphabets[0])
        path.append(res)
        path.append(res)
        res = lettre_apres_rotor_inverse(rotor2, res, alphabets[1])
        path.append(res)
        path.append(res)
        res = lettre_apres_rotor_inverse(rotor3, res, alphabets[2])
        path.append(res)
        path.append(res)
        res = lettre_apres_cablage(alphabet[res], cablage)
        path.append(alphabet.index(res))
        path.append(alphabet.index(res))
        rotors[0][0] = rotor1
        rotors[1][0] = rotor2
        rotors[2][0] = rotor3
    return res, rotors, alphabets, path






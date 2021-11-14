import sys, os
import numpy as np

def init_pions(nb_cases, nb_couleurs):
    """
    Cette fonction permet à la machine de générer de manière 
    aléatoire la combinaison à déterminer par le joueur.
    ------------------------------------------------
    PARAMÈTRES :
        Entrée :
            nb_cases : longueur de la combinaison (entier)
            nb_couleurs : nombre de couleurs disponibles (entier)
        
        Sortie : 
            result : matrice contenant la combinaison aléatoire
    """

    result = np.random.uniform(low = 0, high = nb_couleurs, size = nb_cases) 
    result = np.round(result)
    return result

def jouer(nb_cases, nb_couleurs):
    """
    Cette fonction permet au joueur de choisir la combinaison qu'il
    pense être juste.
    ------------------------------------------------
    PARAMÈTRES :
        Entrée :
            nb_cases : longueur de la combinaison (entier)
            nb_couleurs : nombre de couleurs disponibles (entier)
        
        Sortie : 
            result : matrice contenant la combinaison du joueur
    """

    choix = []
    for i in range(nb_cases):
        c = int(input("Entrer un chiffre inferieur ou egal a {}\n".format(nb_couleurs)))
        choix.append(c)
    return np.array(choix).reshape((-1))

def verification(liste_ordi, liste_jouer):
    r1 = liste_ordi == liste_jouer
    r2 = liste_jouer != liste_ordi
    inter_liste = liste_ordi[r2]
    result = []
    for i in range(len(r1)):
        if r1[i] :
            result.append("Blanc")
        else :
            elmt = liste_jouer[i]
            repeat = np.where(inter_liste == elmt)[0]
            
            if len(repeat) == 0:
                result.append("Vide")
            else:
                result.append("Noire")
                inter_liste = np.delete(inter_liste, repeat[0])
    return result

def fin(win):
    if win:
        print("Victoire !")
    else:
        print("Perdu !")

def partie():
    nb_cases = 5
    nb_col = 8
    nb_tours = 6
    win = False
    tour = 0
    liste_ordinateur = init_pions(nb_cases, nb_col)

    while tour < nb_tours and not win:
        liste_j = jouer(nb_cases, nb_col)
        print(liste_j)
        result = verification(liste_ordinateur, liste_j)
        print(result)
        win = result == ["Blanc", "Blanc", "Blanc", "Blanc", "Blanc"]
        tour =+ 1
    
    return win

print(partie())


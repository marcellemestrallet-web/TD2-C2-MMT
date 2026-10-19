#! /usr/bin/env python3

"""Chiffrement d'un texte à l'aide d'un algorithme de chiffrement mono-alphabétique """

import random
import sys

def alphabet_latin(): 
    """DONE: Renvoyer les caractères alphabétiques présents dans les données de référence. """
    return "abcdefghijklmnopqrstuvwxyzßàáâãäåæçèéêëìíîïðñòóôöøùúüýþąćĉčďęěĝğĥıĵłńňœřśŝşšťŭůźżž"
    
def generer_cle(): 
    """TODO: Renvoyer les caractères alphabétiques présents dans les données de référence dans un ordre aléatoire. """
    return "abcdefghijklmnopqrstuvwxyzßàáâãäåæçèéêëìíîïðñòóôöøùúüýþąćĉčďęěĝğĥıĵłńňœřśŝşšťŭůźżž"

def chiffrer(texte,cle):
    """TODO: Chiffrer un texte en appliquant les substitutions correspondant à la clé passée en paramètre. """
    pass

def dechiffrer(texte,cle):
    """TODO: Déchiffrer un texte en appliquant les substitutions correspondant à la clé passée en paramètre. """
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fichier_cle=sys.argv[1]
        with open(fichier_cle, "r", encoding="utf-8") as fichier:
            cle = fichier.read()
            #print(cle)
            chaine = sys.stdin.read()
            #print(chaine)
            print(dechiffrer(chaine,cle))
    else :         
        cle = generer_cle()
        #print(cle)
        message = chiffrer(sys.stdin.read(), cle) 
        print(message) 
        with open("cle_substitution.txt", "w", encoding="utf-8") as fichier:
            fichier.write(cle+"\n")
    

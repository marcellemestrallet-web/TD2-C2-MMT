#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. """

import sys
import os

def debug(s):
    """Affiche un message en mode DEBUG, sans saut de ligne"""
    if "DEBUG" in os.environ:
        print(s, end="")

def arguments():
    """Affiche les arguments de la ligne de commande."""
    if len(sys.argv) == 1:
        sys.stderr.write("Aucun argument fourni.\n")
        sys.exit(1)
    i=0
    for indice in range(len(sys.argv)):
        debug("Argument " + str(indice)+ ": ")
        print(sys.argv[indice])

def arguments_idiomatique():
    """Affiche les arguments de la ligne de commande, en utilisant la fonction enumerate"""
    if len(sys.argv) == 1:
        sys.stderr.write("Aucun argument fourni.\n")
        sys.exit(1)
    for i, val in enumerate(sys.argv):
        debug("Argument " + str(i) + ": ")
        print(val)


if __name__ == "__main__":
    arguments()         

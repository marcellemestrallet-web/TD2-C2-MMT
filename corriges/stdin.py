#! /usr/bin/env python3
"""Ce programme permet de compter le nombre de caractères saisi par l'utilisateur dans son entrée standard et de l'afficher. 
- Ce programme demandera à l'utilisateur de saisir une chaine uniquement s'il est invoqué en mode interactif.  
- Ce programme ne devra afficher sur la sortie standard *que* le nombre de caractères saisi. 
- Une fois le programme ci-dessous mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import sys

def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur à l'aide d'un message si le flux d'entrée n'est pas redirigé"""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()

def comptage_avec_parcours():
    """Compte les caractères saisis dans l'entrée standard à l'aide d'un for c in s."""
    count=0
    for caractere in lire_stdin():
        count+=1
    return count

def comptage():
    """Compte les caractères saisis dans l'entrée standard à l'aide de len(s)."""
    return len(lire_stdin())

if __name__ == "__main__":
    print(comptage())

#! /usr/bin/env python3

"""Programme permettant de réaliser successivement les opérations de chiffrement puis déchiffrement du texte fourni sur son entrée standard, 
en utilisant le chiffrement de César, à l'aide de la commande shell tr et de la commande python subprocess."""

import subprocess
import sys

def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur à l'aide d'un message si le flux d'entrée n'est pas redirigé"""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()

def coder(s): 
    """Réalise un chiffrement de César à l'aide de la commande tr."""
    resultat = subprocess.run(
        ["tr", "a-zA-Z", "D-ZABCd-zabc"],
        input=s,
        capture_output=True,
        text=True
    )
    return resultat.stdout

def decoder(s): 
    """Réalise un déchiffrement de César à l'aide de la commande tr."""
    resultat = subprocess.run(
        ["tr", "D-ZABCd-zabc", "a-zA-Z"],
        input=s,
        capture_output=True,
        text=True
    )

    return resultat.stdout

def tuto():
    """Démonstration de l'utilisation de la commande subprocess."""
    resultat = subprocess.run(
        ["wc", "-c", "-w"],
        input="une chaine de 5 mots et 38 caractères",
        capture_output=True,
        text=True
    )
    print(resultat.stdout)
    print(resultat.stderr)
    print(resultat.returncode)


if __name__ == "__main__":
    # tuto()
    s = lire_stdin()
    print("Chaine à traiter : " + s)
    s1 = coder(s)
    print("Chiffrement : " + s1)
    s2 = decoder(s1)
    print("Déchiffrement : " + s2)
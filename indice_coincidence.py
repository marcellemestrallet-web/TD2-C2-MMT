#! /usr/bin/env python3

"""Calcul de l'indice de coincidence d'un texte."""

import sys
import os

from analyse_frequences import (
    lire_fichier, 
    lire_csv,
    structurer_reference_freqs,
    enrichir_reference_freqs, 
    compter_occurrences,
    normaliser_occurrences
)

ACCENTS = {
    "à": "a", "á": "a", "â": "a", "ã": "a",
    "ä": "a", "å": "a", "æ": "a", "ą": "a",
    "ç": "c", "ć": "c", "ĉ": "c", "č": "c",
    "ď": "d",
    "è": "e", "é": "e", "ê": "e", "ë": "e",
    "ę": "e", "ě": "e",
    "ĝ": "g", "ğ": "g",
    "ĥ": "h",
    "ì": "i", "í": "i", "î": "i", "ï": "i", "ı": "i",
    "ĵ": "j",
    "ł": "l",
    "ń": "n", "ñ": "n", "ň": "n",
    "ð": "d",
    "ò": "o", "ó": "o", "ô": "o", "õ": "o",
    "ö": "o", "ø": "o", "œ": "o",
    "ř": "r",
    "ś": "s", "ŝ": "s", "ş": "s", "š": "s",
    "ť": "t", "þ": "t",
    "ù": "u", "ú": "u", "û": "u", "ü": "u",
    "ŭ": "u", "ů": "u",
    "ý": "y", "ź": "z", "ż": "z", "ž": "z",
    "ß": "s"
}


def supprimer_accents(texte):
    """DONE: Supprime les accents du texte passé en paramètre et le renvoie. 
    Hypothèse : le texte doit être composé uniquement de minuscules. """
    texte_sans_accents = ""

    for lettre in texte:
        if lettre in ACCENTS:
            texte_sans_accents += ACCENTS[lettre]
        else:
            texte_sans_accents += lettre

    return texte_sans_accents

def calculer_ic(texte):
    """TODO: Renvoyer l'indice de coïncidence du texte passé en paramètre. """

if __name__ == "__main__":
    if len(sys.argv) <2 :
        sys.stderr.write("Pas assez d'arguments fournis.\n")
        sys.exit(1)
    else: 
        chemin = sys.argv[1]
    txt = lire_fichier(chemin)
    #print("texte chiffre : " + txt)
    print(calculer_ic(txt))


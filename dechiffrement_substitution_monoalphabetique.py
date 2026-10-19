#! /usr/bin/env python3

"""Réaliser les opérations suivantes : 
- Calculer la fréquence des caractères du texte chiffré ; 
- Trier les caractères du texte chiffré par ordre décroissant de fréquence ; 
- Pour chaque caractère présent dans le texte chiffré, proposer à l'utilisateur un caractère de substitution, 
en suivant l'ordre décroissant des fréquences de référence des caractères dans la langue considérée
- Afficher le message partiellement déchiffré correspondant ; 
- Permettre à l'utilisateur de valider ou de modifier les substitutions proposées au fur et à mesure.
"""

import sys
import os

from analyse_frequences import (
    lire_stdin, 
    lire_fichier, 
    lire_csv,
    structurer_reference_freqs,
    enrichir_reference_freqs, 
    compter_occurrences,
    normaliser_occurrences
)

def cle_tri(elt) : 
    return elt[1]

def trier_liste_freq(freq): 
    """DONE: Trie les caractères par ordre décroissant de fréquence. """
    freq.sort(key=cle_tri, reverse=True)

def afficher_freqs(ref,txt):
    """DONE: Affiche les fréquences des caractères du texte à déchiffrer, ainsi que les fréquences de référence, en les numérotant. """
    print("#\tRef\tFreq\t#\tTexte\tFreq")
    #for i in range (max(len(ref),len(txt))):
    for i in range (min(len(ref),len(txt))):
        if (i<len(ref)) : 
            print(f"{i}\t{ref[i][0]}\t{ref[i][1]:.4f}\t", end="")
        else : 
            print("\t\t\t", end="")
        if i<len(txt) : 
            print(f"{i}\t{txt[i][0]}\t{txt[i][1]:.4f}") 
        else : 
            print("")

def appliquer_substitutions(texte, substitutions_decidees, substitutions_proposees):
    """DONE: Applique les substitutions passées en paramètre pour renvoyer un texte partiellement déchiffré. """
    # les substitutions sont des dictionnaires 
    t = ""
    print("decidees: ",end="") 
    print(substitutions_decidees)

    print("proposees: ",end="") 
    print(substitutions_proposees)

    for c in texte: 
        if c in substitutions_decidees : 
            t += substitutions_decidees[c]  
        elif c in substitutions_proposees : 
            t += substitutions_proposees[c]
        elif c.isalpha() : 
            t += "?"
        else : 
            t += c
    return t


if __name__ == "__main__":
    if len(sys.argv) <3 :
        sys.stderr.write("Pas assez d'arguments fournis.\n")
        sys.exit(1)
    else: 
        chemin = sys.argv[1]
        langue = sys.argv[2]
    txt = lire_fichier(chemin)
    print("texte chiffre : " + txt)

    d,n = compter_occurrences(txt)
    normaliser_occurrences(d,n)
    freqs_txt = list(d.items()) 
    trier_liste_freq(freqs_txt)

    data = lire_csv("letter_frequency.csv")
    ref = structurer_reference_freqs(data)
    enrichir_reference_freqs(ref,"English", "extraits/aliceInWonderland_en")
    freqs_ref = list(ref[langue].items())
    trier_liste_freq(freqs_ref)
    
    afficher_freqs(freqs_ref, freqs_txt) 

    substitutions_decidees = {}
    substitution_proposee = {}

    while 1: 
        os.system("clear")
        # TODO: afficher les caractères dans l'ordre de leur fréquence, entre le texte à déchiffrer et le fréquences de référence
        # afficher le texte chiffré 
        # afficher le texte partiellement déchiffré en appliquant les substitutions décidées 
        # demander à l'utilisateur de saisir sa substitution 
        # afficher le texte partiellement déchiffré en appliquant les substitutions décidées et la substitution proposée
        # demander à l'utilisateur s'il souhaite valider sa substitution, et l'ajouter aux substitutions décidées le cas échéant
        

       

    




    

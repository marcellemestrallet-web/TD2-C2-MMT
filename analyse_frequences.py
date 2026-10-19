#! /usr/bin/env python3

"""fonctions pour l'analyse des fréquence des caractères d'un texte"""

import os
import sys
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def lire_fichier(fichier):
    pass
    
def lire_csv(path):
    with open("letter_frequency.csv", encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=";")
        data = list(lecteur)
        return data
    
def lire_stdin():
    pass
    
def structurer_reference_freqs(data):
    langues = data[0][1:]
    dics_freqs = [{} for l in langues]
    for l in range(1, len(data)):
        if not data[l]:
            continue
        lettre = data[l][0]
        for f in range(1, len(data[l])):
            valeur = data[l][f].strip("%*")
            freq = float(valeur) / 100
            dics_freqs[l - 1][lettre] = freq
    # Association des deux listes (langues et dics_freqs) pour former le dictionnaire final
    dictionnaire_final = {}
    for i in range(len(langues)):
        dictionnaire_final[langues[i]] = dics_freqs[i]
    return dictionnaire_final
    
def enrichir_reference_freqs(ref,langue, chemin):
    pass
    
def normaliser_occurrences(d, nb):
    pass

if __name__ == "__main__":
    pass


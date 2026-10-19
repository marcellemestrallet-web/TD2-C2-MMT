#! /usr/bin/env python3

"""Analyse un texte et identifie dans quelle langue il est écrit. """

import os
import sys
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def lire_fichier(fichier):
    """DONE: Ouvrir un fichier et renvoie son contenu. """
    try:
        with open(fichier,"r",encoding="utf-8") as flux:    
            texte = flux.read()
            return texte
    except: 
        sys.stderr.write("Impossible d'ouvrir le fichier " +  fichier + "\n")
        sys.exit(1)

### gestion des données de référence (cf. fichier letter_frequency.csv) #########################################

def lire_csv(path):
    """TODO: Renvoyer les données d'un fichier csv sous forme de listes de lignes. 
    Hypothèses : fichier structuré à l'aide du séparateur ";" / encodé en utf-8. """

    
def fixture_lire_csv(path): 
    """Fixture: renvoie un exemple de ce que devrait renvoyer la fonction lire_csv. """
    return [
        ['Letter', 'French', 'Spanish'],
        ['a', '7.636%', '11.525%'],
        ['b', '0.901%', '2.215%'],
        ['c', '3.260%', '4.019%'],
        ['d', '3.669%', '5.010%'],
        ['e', '14.715%', '12.181%'],
        ['f', '1.066%', '0.692%'],
        ['g', '0.866%', '1.768%'],
        ['h', '0.737%', '0.703%'],
        ['i', '7.529%', '6.247%'],
        ['j', '0.613%', '0.493%'],
        ['k', '0.049%', '0.011%'],
        ['l', '5.456%', '4.967%'],
        ['m', '2.968%', '3.157%'],
        ['n', '7.095%', '6.712%'],
        ['o', '5.796%', '8.683%'],
        ['p', '2.521%', '2.510%'],
        ['q', '1.362%', '0.877%'],
        ['r', '6.693%', '6.871%'],
        ['s', '7.948%', '7.977%'],
        ['t', '7.244%', '4.632%']
    ]


def fixture_structurer_reference_freqs(data):
    """Fixture: renvoie un exemple de ce que devrait renvoyer la fonction structurer_reference_freqs. """
    return {
        'French': {
            'a': 0.07636,
            'b': 0.00901,
            'c': 0.0326,
            'd': 0.03669,
            'e': 0.14715,
            'f': 0.01066,
            'g': 0.00866,
            'h': 0.00737,
            'i': 0.07529,
            'j': 0.00613,
            'k': 0.00049,
            'l': 0.05456,
            'm': 0.02968,
            'n': 0.07095,
            'o': 0.05796,
            'p': 0.02521,
            'q': 0.01362,
            'r': 0.06693,
            's': 0.07948,
            't': 0.07244
        },
        'Spanish': {
            'a': 0.11525,
            'b': 0.02215,
            'c': 0.04019,
            'd': 0.0501,
            'e': 0.12181,
            'f': 0.00692,
            'g': 0.01768,
            'h': 0.00703,
            'i': 0.06247,
            'j': 0.00493,
            'k': 0.00011,
            'l': 0.04967,
            'm': 0.03157,
            'n': 0.06712,
            'o': 0.08683,
            'p': 0.0251,
            'q': 0.00877,
            'r': 0.06871,
            's': 0.07977,
            't': 0.04632
        }
    }

def structurer_reference_freqs(data) : 
    """TODO: parcourir les langues dans la première ligne 
    pour chacune, construire un dictionnaire associant la lettre à sa fréquence dans la langue
    Renvoyer un dictionnaire contenant les dictionnaires produits. """
    langues = []    # liste des langues qui devront être présentes dans le dictionnaire : ["French", "Spanish", ...]
    freqs = []      # liste des dictionnaires de fréquences des caractères dans cette langue [ {'a': 0.07636, 'b': 0.00901, ...}, {'a': 0.11525,...}, ...] 
    ref = {}        # résultat attendu : { 'French': { 'a': 0.07636, ...}, 'Spanish': { 'a': 0.11525,, ...}, ... }
    return ref


def fixture_enrichir_reference_freqs(ref,langue, chemin):
    """Fixture: Ajoute la langue "English" dans les données de référence. 
    Les fréquences insérées sont celles de la langue Anglaise, calculées à partir de l'analyse du fichier "extraits/aliceInWonderland_en". """
    ref["English"] = ref["French"].copy()
    ref["English"]['a'] = 0.0797688704475096
    ref["English"]['b'] = 0.014214629560594518
    ref["English"]['c'] = 0.02453928067815291 
    ref["English"]['d'] = 0.04440248310290614
    ref["English"]['e'] = 0.12545990890967146 
    ref["English"]['f'] = 0.019287809780054135

def enrichir_reference_freqs(ref,langue, chemin): 
    """TODO: Ajouter les caractères d'une langue à partir de la lecture d'un texte. """
    # Il faut que tous les caractères apparaissent dans cette langue (comme dans les autres)
    # On part par exemple du français 
    # ref[langue] = ref["French"] # ATTENTION : ceci est une prise de référence !!! 
    ref[langue] = ref["French"].copy()

 
def fixture_compter_occurrences(texte) : 
    """Fixture: renvoie un exemple de ce que devrait renvoyer la fonction pour le texte du fichier "VoixAmbigue". """
    return {'e': 2, 'x': 3, 't': 4, 'r': 1, 'a': 2, 'i': 3, 's': 1, 'v': 1, 'o': 1, 'm': 1, 'b': 1, 'g': 1, 'u': 1}, 22

def compter_occurrences(texte): 
    """TODO: Parcourir les caractères alphabétiques d'un texte afin de produire un dictionnaire 
    contenant le *nombre d'occurrences* de chaque lettre dans le texte. 
    - Cette fonction ne devra pas distinguer la casse des caractères : 'a' ou 'A' représentent la même chose. 
    - Cette fonction devra renvoyer un tuple composé du dictionnaire d'occurrences généré et du nombre total de caractères alphabétiques trouvés. """
    occ = {}    # dictionnaire indiquant les occurences de chacun des caractères alphabétiques dans le texte 
    nb = 0      # nombre de caractères du texte alphabétiques du texte
    return occ, nb

### FIN gestion des données de référence  #######################################################################



### Analyse d'un fichier texte ##################################################################################

def fixture_normaliser_occurrences(d,n) : 
    """Fixture: normalise sur place le dictionnaire d'occurrences pour en faire un dictionnaire de frequences.
    Exemple des fréquences attendues pour le texte du fichier "VoixAmbigue". """
    d['e'] = 0.09090909090909091 
    d['x'] = 0.13636363636363635
    d['t'] = 0.18181818181818182
    d['r'] = 0.045454545454545456
    d['a'] = 0.09090909090909091 
    d['i'] = 0.13636363636363635
    d['s'] = 0.045454545454545456
    d['v'] = 0.045454545454545456 
    d['o'] = 0.045454545454545456
    d['m'] = 0.045454545454545456 
    d['b'] = 0.045454545454545456 
    d['g'] = 0.045454545454545456 
    d['u'] = 0.045454545454545456

def normaliser_occurrences(d, nb): 
    """TODO: Normaliser sur place un dictionnaire d'occurrences pour qu'il contienne les *fréquences* des caractères du fichier texte à analyser. """
    pass
    

def fixture_calculer_mse(reference_freqs,texte_freqs, chaine=None):
    """Fixture: renvoie un extrait des scores mse calculés pour le texte du fichier "tourDuMonde80Jours_fr". """ 
    return [
        ('French', 0.0013200181251706875), 
        ('German', 0.0017723910029813382), 
        ('Spanish', 0.0015256110322712792), 
        ('Portuguese', 0.0016165249955848889), 
        ('Esperanto', 0.0017237336571233504), 
        ('Italian', 0.0017827693881884389)
    ]

        
def calculer_mse(reference_freqs,texte_freqs, chaine=None): 
    """TODO: Calculer pour chaque langue des données de référence, *l'erreur quadratique moyenne* (score *MSE* : *Mean Square Error*) 
    entre les fréquences observées dans le texte et les fréquences de référence, pour les caractères listés dans le troisième argument. 
    - Si le troisième argument n'est pas fourni, tous les caractères présents dans les données de référence devront être utilisés.
    - Le résultat de cette fonction devra être fourni sous la forme d'une liste de tuples `(langue, score)`. """
    scores = []     # liste des scores MSE calculés pour chaque langue
    return scores    

def fixture_trier_mse(mse) : 
    """Fixture: renvoie un extrait de la liste triée des scores mse calculés pour le texte du fichier "tourDuMonde80Jours_fr". """ 
    mse[0] = ('French', 0.0013200181251706875)
    mse[1] = ('Spanish', 0.0015256110322712792)
    mse[2] = ('Portuguese', 0.0016165249955848889)
    mse[3] = ('Esperanto', 0.0017237336571233504)
    mse[4] =  ('German', 0.0017723910029813382)
    mse[5] = ('Italian', 0.0017827693881884389)

def cle_tri(elt) :
    """TODO: Renvoyer la clé de tri : le champ de chaque élément de la liste qui servira à classer. """
    pass

def trier_mse(mse): 
    """TODO: Classer sur place les langues selon le score obtenu par ordre croissant. """
    pass

def tracer_mse(mse, chemin, titre): 
    """DONE: Produire un diagramme portant le titre *titre* 
    dans le fichier *chemin* représentant les scores *mse* 
    à l'aide de la bibliothèque `pyplot`. """
    langues = [x[0] for x in mse]
    scores = [x[1] for x in mse]
    plt.figure()
    plt.barh(langues,scores)
    plt.ylabel("Langue")
    plt.xlabel("Score MSE")
    plt.title(titre)
    plt.tight_layout()
    plt.savefig(chemin)
    plt.close()

def analyse_lois() : 
    """TODO: Produire un diagramme de scores pour chacun des textes présents dans le répertoire `lois` de votre projet, 
    et vérifier si la langue associée à l'erreur la plus faible est bien celle du texte considéré. """
    pass

if __name__ == "__main__":
    data = fixture_lire_csv("letter_frequency.csv")
    print(data)
    
    ref = fixture_structurer_reference_freqs(data)
    print(ref)

    enrichir_reference_freqs(ref,"English", "extraits/aliceInWonderland_en")
    print(ref)

    d,n = fixture_compter_occurrences("extraits/voixAmbigue.txt")
    print(d,n)
    
    fixture_normaliser_occurrences(d,n)
    print(d)
    
    #mse = fixture_calculer_mse(ref,d,"abcdefghijklmnopqrstuvwxyz")
    mse = fixture_calculer_mse(ref,d)
    print(mse)
    
    fixture_trier_mse(mse)
    print(mse)

    tracer_mse(mse,"mse.png", "Language matching, MSE for " + "extraits/tourDuMonde80Jours_fr")
    
    analyse_lois()
    

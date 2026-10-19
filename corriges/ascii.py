#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques détaillées. 
- ***Cet exercice s'inspire largement d'un TP construit par Christian Vercauter, enseignant d'informatique à l'Ecole Centrale de Lille, aujoud'hui retraité.***
- Le programme doit afficher en plus des informations précédentes du programme comptage : 
    - Le nombre total de caractères alphabétiques rencontrés. 
    - Un tableau présentant le nombre d'occurrences de chaque caractère alphabétique, ainsi que sa fréquence (rapport entre le nombre d'occurrences d'un caractère alphabétique sur le nombre total de caractères alphabétiques).
- **Indications** : Créer et initialiser à zéro, une liste de 29 composantes entières, qui contiendra les occurrences des caractères alphabétiques mais également le nombre total de mots, lignes, caractères et caractères alphabétiques rencontrés. 
- Considérer les caractères accentués de manière spéficique à l'aide d'un `match/case`; 
- Tester votre programme sur les deux extraits du roman de Georges Perec (1936-1982) intitulé "La Disparition" paru en 1969. Que remarquez-vous en examinant les résultats ?
- Tester votre programme sur l'extrait d'un autre roman de Georges Perec, intitulé "Les Revenentes" paru en 1972. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **lipogramme** ?
- Tester votre programme sur le texte suivant : *"Portez ce vieux whisky au juge blond qui fume"*. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **pangramme** ? A quoi servent les pangrammes en informatique ?
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 

"""

import sys
import os

def debug(s):
    """Affiche un message en mode DEBUG, avec saut de ligne"""
    if "DEBUG" in os.environ:
        print(s)


def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur à l'aide d'un message si le flux d'entrée n'est pas redirigé"""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()

def lire_flux(flux):
    """Lit le flux passé en paramètre (stdin ou fichier)"""
    if flux is sys.stdin :
        return lire_stdin()
    else :
        return flux.read()

def get_flux_from_args(): 
    """Récupère un éventuel argument fichier et sélectionne le flux à utiliser"""
    if len(sys.argv) > 1: 
        try:
            flux = open(sys.argv[1],"r")
        except: 
            sys.stderr.write("Impossible d'ouvrir le fichier " +  sys.argv[1] + "\n")
            sys.exit(1)
    else: 
        debug("Pas d'argument : utilisation de stdin\n")
        flux = sys.stdin
    return flux


def lire():
    """Lit un fichier et affiche ses caractéristiques détaillées."""
    flux = get_flux_from_args()

    compteurs = [0 for i in range(30)]      # structure contenant les statistiques d'occurences de chaque lettre (cases 0-25)
    iNbCar=26                               # indice dans la structure où trouver le nombre de CARACTERES du texte
    iNbCarAlpha=27                          # indice dans la structure où trouver le nombre de CARACTERES ALPHABETIQUES du texte
    iNbMots=28                              # indice dans la structure où trouver le nombre de MOTS du texte 
    iNbLignes=29                            # indice dans la structure où trouver nombre de LIGNES du texte
    dansMot = False                         # le dernier caractère lu était-il autre chose qu'un séparateur ? 
    
    nextMot = ""        # mot en cours de lecture                          # debug


    # parcours du flux et comptage
    for c in lire_flux(flux):
        debug("Lu: ." + c + ". nbCar : " + str(compteurs[iNbCar]))

        compteurs[iNbCar] +=1               # nouveau caractère 

        # La détection d'un premier caractère entraîne l'existence d'une première ligne
        if compteurs[iNbCar]==1 :
            compteurs[iNbLignes] +=1

        match c:
            case '\n':
                compteurs[iNbLignes] +=1     # une fin de ligne termine une ligne
                if dansMot:                  # une fin de ligne termine un mot 
                    dansMot = False
                    compteurs[iNbMots] +=1
                    debug(f"Mot[{compteurs[iNbMots]}] = {nextMot}")        # debug
                    nextMot = ""                                           # debug    
                
            case ' ':                        # un espace termine un mot
                if dansMot: 
                    dansMot = False
                    compteurs[iNbMots] +=1
                    debug(f"Mot[{compteurs[iNbMots]}] = {nextMot}")        # debug
                    nextMot = ""                                           # debug

            case '\t':                       # une tabulation termine un mot
                if dansMot: 
                    dansMot = False
                    compteurs[iNbMots] +=1
                    debug(f"Mot[{compteurs[iNbMots]}] = {nextMot}")        # debug
                    nextMot = ""                                           # debug

            case _:                          # On est dans ou on entre dans un mot 
                if ord(c)>= ord("a") and ord(c)<= ord("z"): 
                    compteurs[ord(c) - ord("a")] += 1
                    compteurs[iNbCarAlpha] += 1
                elif ord(c)>= ord("A") and ord(c)<= ord("Z"):
                    compteurs[ord(c) - ord("A")] += 1
                    compteurs[iNbCarAlpha] += 1
                else:
                    match c:
                        case 'é': compteurs[ord("E") - ord("A")] += 1
                        case 'è': compteurs[ord("E") - ord("A")] += 1
                        case 'ê': compteurs[ord("E") - ord("A")] += 1
                        case 'à': compteurs[ord("A") - ord("A")] += 1
                        case 'ù': compteurs[ord("U") - ord("A")] += 1
                        case 'ï': compteurs[ord("I") - ord("A")] += 1   

                if dansMot:                                                # debug
                    nextMot += c                                           # debug
                else:                    
                    nextMot = c                                            # debug
                    dansMot = True
    
    # Si le fichier se termine alors qu'on était dans un mot, il faut le terminer
    if dansMot: 
        compteurs[iNbMots] +=1
        debug(f"Mot[{compteurs[iNbMots]}] = {nextMot}")                    # debug


    # affichage 
    print(f"nbCarAlpha:{compteurs[iNbCarAlpha]} nbCar:{compteurs[iNbCar]} nbMots:{compteurs[iNbMots]} nbLignes:{compteurs[iNbLignes]}")

    for i in range(26):
        print(f"{chr(ord('A')+i)} : {compteurs[i]:2} : {(100*compteurs[i])/compteurs[iNbCarAlpha]:5.2f} %")

    # fermeture du fichier 
    flux.close()

if __name__ == "__main__":
    lire()

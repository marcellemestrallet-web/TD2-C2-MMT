#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

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
    """Lit un fichier et affiche ses caractéristiques principales."""
    flux = get_flux_from_args()

    nbCar=0             # nombre de CARACTERES du texte
    nbMots=0            # nombre de MOTS du texte
    nbLignes=0          # nombre de LIGNES du texte
    dansMot = False     # le dernier caractère lu était-il autre chose qu'un séparateur ? 
    
    nextMot = ""        # mot en cours de lecture              # debug
 
    # parcours du flux et comptage
    for c in lire_flux(flux):
        debug("Lu: ." + c + ". nbCar : " + str(nbCar))
        
        nbCar +=1                           # nouveau caractère 

        # La détection d'un premier caractère entraîne l'existence d'une première ligne
        if nbCar==1 :
            nbLignes +=1

        match c:
            case '\n':
                nbLignes +=1                 # une fin de ligne termine une ligne
                if dansMot:                  # une fin de ligne termine un mot 
                    dansMot = False
                    nbMots +=1
                    debug(f"Mot[{nbMots}] = {nextMot}")        # debug
                    nextMot = ""                               # debug    
                
            case ' ':                        # un espace termine un mot
                if dansMot: 
                    dansMot = False
                    nbMots +=1
                    debug(f"Mot[{nbMots}] = {nextMot}")        # debug
                    nextMot = ""                               # debug

            case '\t':                       # une tabulation termine un mot
                if dansMot: 
                    dansMot = False
                    nbMots +=1
                    debug(f"Mot[{nbMots}] = {nextMot}")        # debug
                    nextMot = ""                               # debug

            case _:                          # On est dans ou on entre dans un mot 
                if dansMot:                                    # debug
                    nextMot += c                               # debug
                else:                    
                    nextMot = c                                # debug
                    dansMot = True
    
    # Si le fichier se termine (sans saut de ligne) alors qu'on était dans un mot, il faut le terminer
    if dansMot: 
        nbMots +=1
        debug(f"Mot[{nbMots}] = {nextMot}")

    # affichage 
    print(f"nbCar:{nbCar} nbMots:{nbMots} nbLignes:{nbLignes}")

    # fermeture du fichier 
    flux.close()

if __name__ == "__main__":
    lire()

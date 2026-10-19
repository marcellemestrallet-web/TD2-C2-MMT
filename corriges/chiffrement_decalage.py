#! /usr/bin/env python3

"""
Programme permettant de réaliser des opérations de chiffrement-déchiffrement par décalage
- Le texte à chiffrer ou déchiffrer sera fourni sur son l'entrée standard du programme.
- Lors de l'invocation du programme, l'utilisateur devra saisir lui-même le décalage à opérer, sous la forme d'un argument en ligne de commande. 
    - La classe `str` (dont héritent les chaînes de caractères dans un programme python) implémente la méthode `s.isnumeric` 
    pour tester si une chaîne `s` est constituée exclusivement de caractères numériques. 
    Malheureusement, cette méthode renvoie `False` lorsqu'elle est exécutée depuis la chaîne "-3"
    - Pour convertir une chaine de caractères numérique `s` en entier (on parle de *type casting*), on utilise la fonction `int(s)`. 
    Cette fonction lève une exception si la conversion est impossible. 
    - 📌  Le **type casting** est l'opération qui consiste à convertir une valeur d'un type vers un autre type compatible, 
    généralement en utilisant une opération ou une fonction de conversion.
- Si le programme est invoqué sans argument, il devra réaliser un chiffrement de César.
- Votre programme devra s'appuyer sur une fonction nommée `chiffrer` prenant deux arguments en paramètre : 
  - la chaîne à chiffrer. 
  - Le décalage (positif ou négatif) à opérer sur chacun des caractères alphabétiques de la chaine. 
- Les opérations de chiffrement-déchiffrement devront inverser la casse des caractères. 
Vous pourrez utiliser pour cela les *méthodes* `s.islower` et `s.isupper` de la classe `str`.  
- Votre programme devra traiter les caractères alphabétiques non accentués de manière générique en utilisant leurs codes ASCII.
- Votre programme devra traiter de manière spécifique les caractères accentués : il se contentera d'en changer la casse, sans réaliser de décalage.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 
"""

import sys
import os

# ACCENTS_MINUSCULES = ["à", "â", "ä","é", "è", "ê", "ë","î", "ï","ô", "ö","ù", "û", "ü","ÿ","ç"]
# ACCENTS_MAJUSCULES = ["À", "Â", "Ä","É", "È", "Ê", "Ë","Î", "Ï","Ô", "Ö","Ù", "Û", "Ü","Ÿ","Ç"]
# indice = ACCENTS_MINUSCULES.index("é")
# print(ACCENTS_MAJUSCULES[indice])

ACCENTS = ("àâäéèêëîïôöùûüÿç","ÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇ")   # utilisation d'un tuple de chaînes : accès en temps constant, test d'existence en O(n)
ACCENTS_MINUSCULES, ACCENTS_MAJUSCULES = ACCENTS    # unpacking 

# utilisation d'un dictionnaire : accès et tests en temps constant ! 
ACCENTS = {
    "à": "À", "À": "à",
    "â": "Â", "Â": "â",
    "ä": "Ä", "Ä": "ä",
    "é": "É", "É": "é",
    "è": "È", "È": "è",
    "ê": "Ê", "Ê": "ê",
    "ë": "Ë", "Ë": "ë",
    "î": "Î", "Î": "î",
    "ï": "Ï", "Ï": "ï",
    "ô": "Ô", "Ô": "ô",
    "ö": "Ö", "Ö": "ö",
    "ù": "Ù", "Ù": "ù",
    "û": "Û", "Û": "û",
    "ü": "Ü", "Ü": "ü",
    "ÿ": "Ÿ", "Ÿ": "ÿ",
    "ç": "Ç", "Ç": "ç"
}

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

def chiffrer_v1(s,dec): 
    """Réalise une chiffrement par décalage en appliquant le décalage passé en paramètre,
    À l'aide d'un tableau d'accents"""
    r = ""
    for c in s: 
        if c.islower() : 
            if c in ACCENTS_MINUSCULES: 
                indice = ACCENTS_MINUSCULES.index(c)
                r += ACCENTS_MAJUSCULES[indice]
            else : 
                r += chr(ord("A") + (ord(c) - ord("a") + dec + 26) % 26)  
        elif c.isupper() :
            if c in ACCENTS_MAJUSCULES: 
                indice = ACCENTS_MAJUSCULES.index(c)
                r += ACCENTS_MINUSCULES[indice]
            else : 
                r += chr(ord("a") + (ord(c) - ord("A") + dec + 26) % 26)  
        else:
            r += c
    return r 

def chiffrer(s,dec): 
    """Réalise une chiffrement par décalage en appliquant le décalage passé en paramètre,
    À l'aide d'un dictionnaire d'accents"""
    r = ""
    for c in s: 
        if c.islower() : 
            if c in ACCENTS:                 
                r += ACCENTS[c]
            else : 
                r += chr(ord("A") + (ord(c) - ord("a") + dec + 26) % 26)  
        elif c.isupper() :
            if c in ACCENTS: 
                r += ACCENTS[c]
            else : 
                r += chr(ord("a") + (ord(c) - ord("A") + dec + 26) % 26)  
        else:
            r += c
    return r 

def traiter_arguments():
    """Récupération du décalage fourni en arguments"""
    # if len(sys.argv) > 1 and sys.argv[1].isnumeric(): 
    #     decalage = int(sys.argv[1])
    try: 
        decalage = int(sys.argv[1])
    except: 
        sys.stderr.write("Décalage manquant ou mal formé : utilisation de la valeur +3\n")
        decalage = 3
    return decalage


if __name__ == "__main__":
    dec = traiter_arguments()
    s1 = lire_stdin()
    print(chiffrer(s1,dec), end="")
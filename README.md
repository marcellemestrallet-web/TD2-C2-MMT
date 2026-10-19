# APP 2026-2027 -- TD2

## Support de cours

[Support de cours au format Google docs](https://docs.google.com/presentation/d/1xtLq2CcGjzC1wiF6JUL4i_v9mX1e2wphQqo258a2Z4s/edit?usp=sharing)

## Consigne générale 

On rappelle les principes qui vous permettront de monter en compétences : 
- Interpellez l'enseignant pour toute question. 
- N'utiliser pas les IA en phase d'apprentissage pour comprendre/apprendre. Au contraire, cherchez à lire, comprendre et exploiter la [documentation officielle du language](https://docs.python.org/fr/3/contents.html).
- Si votre environnement est configuré pour afficher des suggestions lors de la frappe, désactivez-les !
- Pour désactiver les suggestions dans VSCode, un fichier de configuration est déjà intégré dans ce projet : `.vscode/settings.json`.
- Ponctuellement, vous pouvez utiliser Ctrl+Espace pour demander la complétion des noms de variables/fonctions/méthodes... 
- Ne pas fuir la difficulté : sans effort, pas d'ancrage !
- Tout le travail de développement réalisé en séance est susceptible de donner lieu à des questions lors du QCM de la séance suivante. Plus particulièrement, les termes précédés du symbole 📌 représentent des concepts que vous devez être capables de *définir* et de *développer*, sans aide.
- Le travail réalisé **en séance** est également évalué, sur la base des interactions que vous aurez eu avec l'enseignant pour faire valider vos développements. 
- Si le travail demandé dans le sujet n'a pas été terminé à l'issue de la séance, il doit être poursuivi en TEA. Le QCM de la séance suivante permet également de le vérifier. 


## Objectifs

À l'issue de ce TD, vous devez savoir :

- Récupérer des fichiers depuis un dépôt github à l'aide de la commande shell `wget`. 
- Lire un fichier `csv` pour en parcourir le contenu.  
- Produire un diagramme à l'aide de `pyplot`. 
- Vous répartir des tâches de développement en binôme en utilisant des *fixtures* 

À l'issue du TD1, vous deviez savoir :

- Utiliser le vocabulaire associé à l'exécution des programmes et à leurs entrées-sorties.
- Mettre en place les bonnes pratiques associées. 
- Saisir des caractères en entrée d'un programme en *mode interactif* depuis le shell.
- Utiliser le shell pour mettre en place des redirections. 
- Lire l'entrée standard d'un programme.
- Récupérer les arguments fournis en ligne de commande à un programme.
- Ouvrir un fichier pour le lire ou l'écrire.
- Utiliser la structure de contrôle match/case. 
- Exploiter les codes ASCII des caractères.
- Exécuter une commande shell depuis un programme python.
- Utiliser les types `str`, `list` et `dict` du langage python.
- Utiliser les *tuples* du langage python et le *sequence unpacking*.
- Produire du code robuste et modulaire.

## Exercice 1 : Appropriation de la base de code du TD1 

Les corrigés du TD1 sont situés dans le répertoire `corriges` de votre dépôt. 

1. Vérifiez de trois manières différentes la validité du programme `ascii.py` en utilisant le fichier `extraits/test_comptage` :  
- En fournissant le chemin du fichier comme argument du programme.
- En fournissant le contenu du fichier dans l'entrée standard du programme à l'aide d'une redirection d'entrée.
- En fournissant le contenu du fichier dans l'entrée standard du programme à l'aide d'une redirection de commandes. 
- En activant le *mode de débogage* intégré de deux manières (sans changer le code). 

2. Nous souhaitons décoder le message contenu dans le fichier `extraits/secret1`, qui a été chiffré à l'aide d'un code de César, en refactorisant le code du programme `cesar.py`. 
- 📌 La **refactorisation** est une opération qui consiste à modifier la structure interne d’un programme existant, sans en changer le comportement attendu, afin d’améliorer sa lisibilité, sa modularité, sa maintenabilité ou sa réutilisabilité. Elle peut notamment consister à découper un programme en plusieurs fonctions ou modules, à supprimer des répétitions ou à séparer des responsabilités
- Créer à partir de `cesar.py` les programmes `coder_cesar.py` et `decoder_cesar.py`.
- Décoder le message du fichier `extraits/secret1`.
- Quelle pionnière de l'histoire de l'informatique est évoquée dans ce message secret ? 

3. Nous souhaitons décoder le message contenu dans le fichier `extraits/secret2`, qui a été chiffré à l'aide d'un chiffrement par décalage, en utilisant les fonctions du programme `chiffrement_decalage.py`. Cette fois, le décalage utilisé est inconnu. 
- Développer un programme important les fonctions du fichier `chiffrement_decalage.py`
- Utiliser les fonctions de ce fichier pour développer un programme affichant tous les décalages possibles, l'un après l'autre, jusqu'à trouver le décalage employé pour coder ce fichier. 
- Ce programme lira le texte à déchiffrer depuis un fichier dont le chemin sera fourni comme argument du programme.  
- Après chaque proposition, l'utilisateur devra appuyer sur la touche `Entree` pour continuer.
- Combien de décalages au maximum doivent être testés ? 
- Quel décalage a été utilisé lors du chiffrement ? 
- Quel moment historique de l'histoire de l'humanité est évoqué dans ce message secret ? 

## Chiffrement par substitution monolaphabétique

Dans cet exercice, nous souhaitons étudier la généralisation du chiffrement par décalage, dans laquelle les transformations des lettres ne dépendent plus d'un décalage fixe : le *chiffrement par substitution mono-alphabétique*. 
- 📌 Le **chiffrement par substitution mono-alphabétique** est une technique de chiffrement qui consiste à substituer dans un message chacune des lettres de l'alphabet par une autre, selon une correspondance définie par une clé de substitution. 
- Pour l'alphabet latin, ceci permet de construire 26! ≈ 4 × 10<sup>26</sup> substitutions (soit de l'ordre de 2<sup>88</sup>), à savoir le nombre de permutations des 26 lettres.
- Cf. [Lien Wikipédia sur le chiffrement par substitution](https://fr.wikipedia.org/wiki/Chiffrement_par_substitution).

Le simple chiffrement par substitution est facile à casser par l'analyse des fréquences des lettres du texte chiffré, ce qui est l'objectif du programme que nous souhaitons réaliser dans ce TD : à partir d'un texte chiffré dont la clé est inconnue, nous chercherons à retrouver progressivement le texte original en utilisant l'analyse des fréquences d'apparition des lettres dans la langue du texte considéré.

## Exercice 2 : Fréquence d'apparition des lettres 

D'après la page [Wikipédia sur la fréquence d'apparition des lettres](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres), *"la fréquence d'apparition des lettres dans une langue est une donnée statistique utilisée en linguistique, en typographie et en cryptographie liée au fait que les utilisateurs de la langue écrite n'utilisent pas les lettres disponibles au hasard, mais selon l'ordonnancement de la langue, du langage et de la parole. Bien que l'alphabet ne soit pas hiérarchisé, les lettres écrites ne sont pas utilisées à la même fréquence, en français comme dans les autres langues."*

Ainsi, si l'on connaît la langue d'origine d'un texte ayant subi un chiffrement par substitution monoalphabétique, et que l'on connaît la fréquence d'apparition des lettres dans cette langue, il est possible de formuler des hypothèses sur le texte d'origine. 
- En effet, une substitution monoalphabétique ne modifie pas le nombre d'occurrences de chaque caractère du texte d'origine : elle modifie uniquement la lettre à laquelle ce nombre d'occurrences est associé. 
- Il suffit donc de recalculer la fréquence des caractères du texte chiffré pour pouvoir estimer à quels caractères d'origine ils correspondent dans la langue utilisée.  

Afin de vérifier que la fréquence d'apparition des lettres est suffisamment spécifique pour retrouver la langue d'origine d'un texte, Adrianus Kleemans a développé un script python en s'appuyant sur les fréquences indiquées sur la page Wikipédia précédente. 
- Il a partagé son travail sur le [dépôt Github letter-frequency](https://github.com/akleemans/letter-frequency). 
- Malheureusement, ce développeur a développé son programme en utilisant le language `Python2`. Or, le passage de `Python 2` à `Python 3` n'assure pas de *compatibilité ascendante* : un programme développé pour `Python 2` peut donc nécessiter des modifications pour fonctionner avec `Python 3`.
    - 📌 On parle de **compatibilité ascendante** lorsqu'une nouvelle version d'un langage, d'un logiciel ou d'un système reste compatible avec les programmes ou données conçus pour une version antérieure.
- Plutôt que récupérer tout son travail, nous allons juste repartir de son fichier `letter_frequency.csv` qui contient les fréquences d'apparition des lettres dans plusieurs langues utilisant l'alphabet latin, qui peut être téléchargé directement dans votre environnement de travail à l'aide de la commande `wget` : 

```bash
wget https://raw.githubusercontent.com/akleemans/letter-frequency/refs/heads/master/letter_frequency.csv
```

4. Dans la suite, vous travaillerez en binôme pour accélérer le développement du programme. 
- En attendant de disposer des fonctions qui doivent être réalisées par votre binôme, vous utiliserez les *fixtures* présentes dans le fichier ̀`kleemans.py`. 
    - 📌 En programmation, une **fixture** est une donnée ou un état préparé à l'avance pour réaliser un test.
- À l'issue de la mise au point de chaque fonction, vous mettrez en place des tests et partagerez votre code avec votre binôme. 
- À l'issue de la mise au point du grogramme complet, vous appelerez l'enseignant pour valider votre travail avant de passer à l'exercice suivant. 

### Lecture d'un fichier csv


Pour lire un fichier `csv` en python et extraire chacune de ses lignes sous forme de *liste de listes*, on peut utiliser le module `csv`. 

```python
import csv

with open("letter_frequency.csv", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier, delimiter=";")
    data = list(lecteur)
```

La forme précédente est recommandée par rapport à la syntaxe alternative ci-dessous. L'intérêt de `with` est que Python ferme automatiquement le fichier lorsqu'on sort du bloc, y compris si une erreur survient.

```python
import csv

fichier = open("letter_frequency.csv", encoding="utf-8")
lecteur = csv.reader(fichier, delimiter=";")
data = list(lecteur)
fichier.close()
```

Le paramètre `encoding="utf-8"` indique l'encodage des caractères utilisé pour ce fichier. Cette information peut être déterminée par la commande shell `file`. 

```bash
file letter_frequency.csv
```


- Développer une fonction nommée `read_csv(path)` permettant d'ouvrir un fichier `csv` et d'en récupérer les données. 
- Développer une fonction nommée `structurer_reference_freqs(data)` permettant de construire, à partir des données extraites précédemment, un dictionnaire associant chaque caractère à sa fréquence de référence dans cette langue, puis stocker l'ensemble de ces dictionnaires dans un dictionnaire dont les clés sont les noms des langues, en respectant la structure ci-dessous :

```python
{
    "French": {
        "a": 0.07636,
        "b": 0.00901,
        ...
    },
    "German": {
        "a": 0.06516,
        "b": 0.01886,
        ...
    },
    ...
}
```
- **Indications** : 
    - Lors du parcours des lignes du fichier csv, créer deux listes contenant respectivement les langues et les dictionnaire des fréquences de chaque lettre dans chaque langue. Une fois les deux listes obtenues, les associer pour construire le dictionnaire final. 
    - Stocker directement les fréquences sous forme de réels et non pas de chaînes de caractères en supprimant le caractère `%` associé à chaque valeur du fichier `csv`. Pour cela, utiliser l'expression `float(data[l][f].strip("%")) /100`.
    - Penser à prendre en compte les caractères `*` présents dans certaines valeurs du fichier `csv` après le symbole `%`.

### Comptage des occurences et calcul de l'écart quadratique moyen entre deux textes

- Développer une fonction nommée `compter_occurrences(texte)̀` permettant de parcourir les caractères alphabétiques d'un texte afin de produire un dictionnaire contenant le *nombre d'occurrences* de chaque lettre dans le texte. 
    - Cette fonction ne devra pas distinguer la casse des caractères : 'a' ou 'A' représentent la même chose. 
    - Cette fonction devra renvoyer un tuple composé du dictionnaire d'occurrences généré et du nombre total de caractères alphabétiques trouvés.

- Développer une fonction `normaliser(occurrences, total)` permettant de normaliser -- sur place -- un dictionnaire pour qu'il contienne les *fréquences* des caractères du fichier texte à analyser. 
- **Indication** : un dictionnaire est un type *mutable*, il n'est donc pas nécessaire que cette fonction renvoie un résultat : on modifie le dictionnaire *sur place*. 

- Développer une fonction `calculer_mse(reference_freqs,texte_freqs, chaine)` permettant de calculer pour chaque langue des données de référence, *l'erreur quadratique moyenne* (score *MSE* : *Mean Square Error*) entre les fréquences observées dans le texte et les fréquences de référence, pour les caractères listés dans le troisième argument. 
    - Si le troisième argument n'est pas fourni, tous les caractères présents dans les données de référence devront être utilisés.
    - Le résultat de cette fonction devra être fourni sous la forme d'une liste de tuples `(langue, score)`.  

$$
\mathrm{Score\ MSE} = \frac{1}{n}\sum_{i=1}^{n}
(\mathrm{fréquence\ observée}_i-\mathrm{fréquence\ de\ référence}_i)^2
$$

- Développer une fonction `trier_mse(mse)` permttant de la classer les langues selon le score obtenu à l'aide de la méthode `list.sort(key=foo,reverse=True)`. 
    - Cette méthode est *spécifique aux listes*. À l'issue du tri, la liste est directement *modifiée sur place*.
        - Ne pas confondre *tri sur place* et *tri en place* : le tri sur place indique que la liste de départ est modifiée. Le tri 📌  *en place* est un concept informatique qui indique que le tri une quantité de mémoire auxiliaire *indépendante de la taille de l'entrée*.
    - Elle prend comme argument `key` une *fonction d'un argument* renvoyant la 📌 **clé de tri** : la valeur utilisée pour déterminer l'ordre des éléments lors des comparaisons effectuées avec l'opérateur `<`.
    - L'argument `reverse=True` est optionnel, il permet de demander à trier par ordre décroissant. Sans argument cet argument, la liste est triée par ordre croissant.  
    - Il existe également une fonction native `sorted()` qui construit une *nouvelle liste* triée à partir d'un *itérable*.


- Développer une fonction `tracer_mse(mse,chemin)` permettant de produire un diagramme représentant les scores à l'aide de la bibliothèque `pyplot`, comme le propose Kleemans sur son dépôt. 

```python
import matplotlib
matplotlib.use("Agg")  # https://matplotlib.org/stable/users/explain/figure/backends.html
import matplotlib.pyplot as plt

plt.barh(langues,scores)
plt.ylabel("Langue")
plt.xlabel("Score MSE")
plt.title(titre)
plt.tight_layout()
plt.savefig(chemin)
```

- Produire un diagramme de scores pour chacun des textes présents dans le répertoire `lois` de votre projet, et vérifier si la langue associée à l'erreur la plus faible est bien celle du texte considéré. 
- Pour parcourir les fichiers d'un répertoire en python, on peut utiliser le code suivant. 

```python
import os

for nom in os.listdir("chemin/du/repertoire"):
    print(nom)
```

### Enrichissement du corpus de référence

- Vous constaterez qu'il manque les fréquences des caractères de la langue *anglaise*. Nous vous invitons à les retrouver en procédant à l'analyse du texte d'*Alice au Pays des Merveilles*, de *Lewiss Carroll*, présent dans le répertoire `extraits`.
    - Ce document est tiré du [projet Gutenberg](https://www.gutenberg.org/), une bibliothèque numérique qui propose gratuitement des livres électroniques, principalement des œuvres littéraires anciennes dont les droits d'auteur ont expiré aux États-Unis. Les livres peuvent être lus en ligne ou téléchargés dans différents formats, dont le texte brut, particulièrement adapté au traitement informatique.
    - Développer une fonction `enrichir_reference_freqs(ref,langue, chemin)` permettant d'ajouter aux données de référence les fréquences des caractères d'une nouvelle langue, par la lecture d'un fichier. 
- **Indication** : Pour ajouter une nouvelle langue dans le dictionnaire `ref`, disposant des mêmes caractères que ceux de la langue française par exemple, penser à effectuer une *copie* du dictionnaire français, plutôt qu'une prise de référence : 

```python
ref[langue] = ref["French"] # ceci n'est pas une copie : les deux clés désignent le même espace mémoire
ref[langue] = ref["French"].copy() # chaque clé permet d'accéder à des espaces mémoires différents
```


## Exercice 3 : Programme de chiffrement par substitution mono-alphabétique

5. Développer un programme réalisant un chiffrement par substitution mono-alphabétique des caractères d'un texte fourni sur son entrée standard. 
- Nous considérerons que les textes à chiffrer ne sont composés *que de caractères minuscules*. Les caractères majuscules éventuels seront convertis en minuscules avant chiffrement. 
- Ce programme produira le texte chiffré sur sa sortie standard et stockera la clé de substitution dans un fichier nommé `cle_substitution.txt`
- Si ce même programme est fourni avec un argument contenant le chemin d'un fichier, il devra procéder au *déchiffrement* du message fourni sur son entrée standard à l'aide de la clé fournie dans ce fichier. 
- **Indications** : Afin de faciliter la production de votre programme, vous pouvez utiliser la commmande shell suivante pour générer l'alphabet initial à mélanger à partir du fichier `csv` : 
    
```bash
cat letter_frequency.csv | tail -n +2 | cut -d';' -f1 | tr -d '\n'
# cela donne 'abcdefghijklmnopqrstuvwxyzßàáâãäåæçèéêëìíîïðñòóôöøùúüýþąćĉčďęěĝğĥıĵłńňœřśŝşšťŭůźżž'
```
- Afin de mélanger une liste python, vous pouvez utiliser le module `random` :  
```python
import random

alphabet_latin = 'abcdefghijklmnopqrstuvwxyzßàáâãäåæçèéêëìíîïðñòóôöøùúüýþąćĉčďęěĝğĥıĵłńňœřśŝşšťŭůźżž'
liste_alphabet_latin = list(alphabet_latin)
random.shuffle(liste_alphabet_latin)    # Attention : cette fonction mélange la liste elle-même et ne renvoie rien ! 
cle_substitution = "".join(liste_alphabet_latin)
```

## Exercice 4 : Programme de déchiffrement par analyse des fréquences

Dans cette section, nous souhaitons exploiter l'analyse des fréquences des caractères pour déchiffrer un message chiffré à l'aide d'un chiffrement par substitution mono-alphabétique, dont nous connaissons a priori la langue. 

Pour cela, nous allons réaliser les opérations suivantes : 
- Calculer la fréquence des caractères du texte chiffré. 
- Trier les caractères du texte chiffré par ordre décroissant de fréquence. 
- Afficher sous forme de tableau les caractères du texte chiffré et ceux de la langue de référence, chacun étant trié par ordre décroissant de fréquence. 
    - Numéroter les caractères de chaque liste afin de permettre à l'utilisateur de sélectionner facilement les caractères à substituer. 
- Demander à l'utilisateur de proposer une substitution. 
- Afficher le message partiellement déchiffré correspondant. 
- Permettre à l'utilisateur de valider ou non cette substitution. 
- Recommencer en réaffichant les caractères restant à substituer jusqu'à ce que le texte soit entièrement déchiffré ou que l'utilisateur décide de quitter le programme en sauvegardant son travail. 
- Lorsque l'utilisateur choisit de terminer son travail, le programme doit afficher les indices des caractères dans les substitutions mises en oeuvre, et calculer l'écart moyen de position des caractères lors des substitutions. 

L'utilisateur aura ainsi constamment sous les yeux le message partiellement déchiffré et pourra progressivement construire une substitution qui lui semble pertinente.


6. Développer un module nommé `analyse_frequences.py` à l'aide des fonctions du programme `kleemans.py`. Développer le programme de déchiffrement `dechiffrement_substitution_monoalphabetique.py` décrit ci-dessus en vous appuyant sur les fonctions de ce module.
- Le texte à déchiffrer devra être fourni dans un fichier dont le chemin sera fourni comme premier argument en ligne de commandes. 
- La langue du texte à déchiffrer sera fournie comme second argument en ligne de commandes. 

7. Déchiffrez le message contenu dans le fichier extraits/secret3, dont la langue d'origine est le français. 


## Exercice 5 : Programme de déchiffrement si la langue est inconnue : utilisation de l'indice de coincidence

Notre objectif dans cette section est de déchiffrer un message codé à l'aide d'un chiffrement par substitution mono-alphabétique *dont nous ne connaissons **pas** la langue*. Pour cela, nous procéderons en deux étapes : 
- Détection de la langue la plus probable ; 
- Utilisation de programme de déchiffrement précédent une fois la langue connue. 

Pour détecter la langue d'un texte, nous ne pouvons pas nous appuyer directement sur une comparaison des fréquences du texte à déchiffrer avec les fréquences de référence, puisque nous ne connaissons pas la langue du message. Nous allons donc utiliser un autre indicateur statistique : l'indice de coïncidence.
- 📌 L'indice de coïncidence est une mesure statistique qui permet d'estimer la probabilité que deux caractères choisis au hasard dans un texte soient identiques.
- D'après la [Page Wikipédia sur l'indice de coïncidence](https://fr.wikipedia.org/wiki/Indice_de_co%C3%AFncidence), cet indicateur est caractéristique de la langue utilisée, puisque la distribution des lettres diffère d'une langue à l'autre. 
- Il se calcule de la manière suivante, avec n le nombre de lettres total du message, $n_A$ le nombre de A, $n_B$ le nombre de B, etc. :

$$
\mathrm{IC} = \sum_{q=A}^{Z} \frac{n_q(n_q-1)}{n(n-1)}
$$

- Un chiffrement par substitution monoalphabétique conserve les nombres d'occurrences des caractères, même s'il remplace chaque lettre par une autre. L'indice de coïncidence du texte chiffré est donc identique à celui du texte original, il peut ainsi aider à identifier la langue d'un texte chiffré.

8. Développer un programme calculant l'indice de coincidence d'un texte dont le chemin est fourni comme argument, affichant la langue la plus probable du texte d'origine. 
- Nous considérerons comme précédemment que les textes à déchiffrer ne sont composés que de caractères minuscules.
- Les indices de coïncidence des principales langues peuvent être extraits du site de Wikipédia, recalculés à partir des fréquences de référence ou de fichiers extraits du site du [projet Gutenberg](https://www.gutenberg.org/). 


## Exercice 6 : Pour aller plus loin — Chiffre de Vigenère : chiffrement par substitution polyaphabétique

Le chiffre de Vigenère est un système de *chiffrement par substitution polyalphabétique* dans lequel une même lettre du message clair peut, suivant sa position dans celui-ci, être remplacée par des lettres différentes, contrairement à un système de chiffrement mono alphabétique comme le chiffre de César (qu'il utilise cependant comme composant). Cette méthode résiste ainsi à l'analyse de fréquences, ce qui est un avantage décisif sur les chiffrements mono alphabétiques. 
- Cf. [Lien Wikipédia sur le Chiffre de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re) :  
    - "*Si l'on connait le nombre de symboles que comporte la clé, il devient possible de procéder par analyse de fréquences sur chacun des sous-textes déterminés en sélectionnant des lettres du message clair à intervalle la longueur de la clef (autant de sous-textes que la longueur de la clef). C'est l'attaque bien connue sur les chiffrements mono-alphabétiques."*
    - *"Des techniques statistiques fondées sur l'indice de coïncidence, découvertes au XXe siècle, s'avèrent encore plus efficaces pour casser le chiffre."*

Si le coeur vous en dit, vous pouvez poursuire ce travail en développant un programme de déchiffrement utilisant l'analyse de fréquences, l'indice de coïncidence et des hypothèses sur la longueur de la clé... 


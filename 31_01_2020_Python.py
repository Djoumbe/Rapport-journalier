# • Entrée : Longue chaîne de caractère
# • Traitement :
# • Partage de la chaîne de caractère en une liste de mots
# • On crée une liste vide lignes
# • Pour tout mot dans la liste :
# • On ajoute un espace à mot
# • Si la longueur du dernier élément de la liste vide + la longueur du mot < 24 :
# • On ajoute le mot au dernier élément de la liste ligne (+= mot)
# •
# Si non :
# •
# •
# On ajoute le mot au dernier élément de la liste ligne (+= mot)
# Sortie : liste ligne


p = "Onze ans déjà que cela passe vite Vous vous étiez servis simplement de vos armes la mort n‘éblouit pas les yeux des partisans Vous viez vos portraits sur les murs de nos villes"

def ligne(p) :
    D = [""]
    s1 = p.split() 
    for i in s1 :
        i +=  " " 
        if len(D[-1]) + len(i) <= 24 :
            D[-1]+=i
        else :
            D.append(i)

    return(D)


print(ligne(p))

# 1. Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaîne s commençant par une majuscule.Pour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres (Les lettres majuscule ont un code allant de 65 à 90).

def hascap(s):
    zak = []
    ami = s.split()
    for i in ami :
         if ord(i[0]) in range (65,90) :
             zak.append(i)
    return print(zak)

D = "D"    
hascap(D)

#4. Proposer un programme qui renvoie la liste de tout les nombres 
# (y compris décimaux et négatifs) d’une chaîne de caractères. 
# A tester sur la chaîne : « Les 2 maquereaux valent 6.50 euros ».

import re
def izuku():
    pp = re.findall ("[\-]?[0-9]+[\.,,]*[0-9]*", "Les 3,0 maquereaux valent 6.50 euros")
    print(pp)
izuku()



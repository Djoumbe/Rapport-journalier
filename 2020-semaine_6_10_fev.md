# Sebastien Bories, Data Scientist pour la CMA - CGM

--------------------------------------------------------------


le SGBD peut gérer des verrous, par exemple si **deux utilisateurs veulent manipuler une BD en même temps, les écritures multiples et concurrentes.**
Il est possible de créer des contraintes personnalisés. On peut stocker des données dans une vue matérialisée.
L'index permet d'optimiser ses requêtes en inscrivant des mots clés pour les requêtes soient plus rapides.
Le trigger est un objet de de base de structure qui permet de créer une boucle.

**Les procédures stockées** peuvent créer des bases procédurales et permet d'utiliser des fonctions. 
Il est possible de créer des variables en faisant un code semblable à C et Python.
DB links est de lier des base de données distante et  plusieurs serveurs.

Language de 2ème génération : assembleur.
Prédicats = des conditions (égale, plus grand ou plus petit que)

**Manipulation des lois ensemblistes** : 
- Union
- Calcul de la différence
- Produit cartésien 

Agréger (trouver la somme, minimum, maximum, moyenne, ect...) des données.

La requête **SELECT** est une boucle. 
Projections conditionnées (CASE WHEN). Cela permet d'effectuer des conditions.
Le "Having" a la quasiment la même fonction que where sauf qu'il permet d'utilier des fonctions d'opérations (somme, minimum, maximum, moyenne).

Conseils :

Ecrire en colonnes principalement 

SQL COMMANDE AVANCEES :
Fenêtrage

Optimisation et plan d'éxecution

L'administrateur de BDD peut effectuer des statistiques et peut être recalculer.

On peut **programmer à l'avance** une requête en la mettant à jour, supprimer une donnée ou une colonne par exemple à tel heure ou tel minute.

Logiciels pour du SQL : PSql, OracleXe

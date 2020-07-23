# Evaluation semaine de cours Python : Share Code

## Partie 1 : enregistrer le langage de programmation utilisé
Model :
* Create .lang file function
* Read .lang file function

Template :
* Add select tag into form
* If condition to select the language used

Routes :
* Add language info to requests

## Partie 2 : Changez le procédé de stockage, plus de fichiers mais un SGBDR
Model :
* Création d'un nouveau model : model_sqlite.py
* Réécriture de toutes les fonctions pour fonctionner avec sqlite
    * createCode(code, langage) --> retourn l'id de la ligne crée
    * getCode(id) --> retourne la ligne associée à l'id
    * getAllCode() --> retourne toutes les lignes
    * updateCode(id, code, language) --> Met à jour la ligne associée à l'id

Route :
* Réécriture du traitement des données, desormais reçues depuis sqlite

template :
* Ajustement de l'interprétation des données reçu


## Partie 3 : enregistrez les infos sur les utilisateurs qui publient du code
A faire

## Partie 4 : colorisation de code
A faire

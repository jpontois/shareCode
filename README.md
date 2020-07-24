# Evaluation semaine de cours Python : Share Code
## Lancement
* pip3 install -r requirements.txt
* pip install Pygments
* export FLASK_ENV=development
* python3 app.py ou python3 -m flask run

## Gitflow mode projet :
* Un branch de développement appelée "Dev"
* Une branche par partie
* Une branch de mise en forme

## Partie 1 : enregistrer le langage de programmation utilisé
**Model :**
* Ajout de fonctions permettant de créer et lire un nouveau type de fichier
    * save_language_as_file (uid, language = 'py') --> Retourne l'uid
    * read_language_as_file (uid) --> Retourne le language associé à l'uid

**Template :**
* Ajout d'un menu déroulant dans la page d'édition permettant de selectionner le code
* Ajout d'une condition pour sélectionner le language lors de la génération de la page

**Routes :**
* Add language info to requests

## Partie 2 : Changez le procédé de stockage, plus de fichiers mais un SGBDR
**Model :**
* Création d'un nouveau model : model_sqlite.py
* Réécriture de toutes les fonctions pour fonctionner avec sqlite
    * createCode(code, langage) --> retourne l'id de la ligne crée
    * getCode(id) --> retourne la ligne associée à l'id
    * getAllCode() --> retourne toutes les lignes
    * updateCode(id, code, language) --> Met à jour la ligne associée à l'id

**Route :**
* Réécriture du traitement des données, désormais reçues depuis sqlite

**Template :**
* Ajustement de l'interprétation des données reçues

## Partie 3 : enregistrez les infos sur les utilisateurs qui publient du code
**Model :**
* Nouvelle table contenant les logs à chaque ajout ou modification d'un user : edition
* Ajout de functions d'interaction avec la table edition
    * createEdition(code_id, id, user_agent) --> Retourne l'id de la ligne crée
    * getEdition() --> Retourne la list des logs des users

**Route :**
* Ajout de la route admin
* Logs des actions des users via createEdition a chaque appel des routes "create" et "publish"

**template :**
* Ajout du template admin.html

## Partie 4 : colorisation de code
**Fichier**
* Ajout du fichier functions
* Fonction :
    * Colorize(code, langage) --> Retourne le code sous forme de html permettant de le mettre en forme via css dans la vue.

**Route :**
* Les données envoyées sont désormais sous forme de dictionnaire avec le html du code généré via la fonction colorize
* Routes affectées :
    * /view/<string:id>
    * /

**template :**
* Ajustement de l'interprétation des données reçues

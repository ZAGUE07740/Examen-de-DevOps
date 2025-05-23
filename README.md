# Examen-de-DevOps
Vous êtes développeur dans une entreprise qui souhaite moderniser son infrastructure et automatiser le déploiement de ses applications. Votre mission est de : ➢ Créer une application web, ➢ L'intégrer dans un pipeline CI/CD, ➢ Conteneuriser l'application avec Docker, 1➢ Publier l'image sur Docker Hub, ➢ Et automatiser le déploiement avec Jenkins. 

## Comment faire fonctionner votre code ?

### Installation du projet Django

Après avoir fait le pull ("git clone <url> ou git pull origin main") du projet, vous aurez reçu les fichiers suivants:

1. **appDevOps**: Il s'agit du projet Django (l'application)
2. **.gitignore**: Il contient les noms des fichiers stockés en local, mais qui ne doivent pas être pris en compte dans le git commit.
   - Vous remarquerez que j'y ai écrit "*virtual_env" (On précède d'une * le nom du fichier à ajouter)
   - virtual_env est mon environnement virtuel local
   - Il contient le bin\ et scripts\ de python et les packages (dans notre cas django)
3. **db.sqlite3**: Il s'agit de la base de données utilisée par notre projet django
4. **manage.py**: Le fichier manage.py dans Django est un script Python essentiel qui sert d'interface de ligne de commande pour interagir avec votre projet Django
5. **requirements.txt**: Il contient les versions des packages nécessaires pour faire fonctionner le projet

### Prérequis
- Python doit être installé sur votre machine
- Vérifiez si pip est installé, sinon installez-le

### Commandes à exécuter

1. Ouvrez l'invite de commande en tant qu'administrateur et exécutez les commandes suivantes :

```bash
cd <mon_du_projet- ici "Examen-de-DevOps">  # pour vous déplacer dans le répertoire PARENT du projet GIT

python -m venv <nom de votre environnement virtuel>  # création de l'environnement virtuel

.\<nom de votre environnement virtuel>\Scripts\activate  # activation de l'environnement virtuel
# Pour Linux/Mac OS: source <nom de votre environnement virtuel>/bin/activate

pip install -r requirements.txt  # installation des packages nécessaires (django etc.)
```

2. Vérifiez que Django fonctionne correctement :

```bash
python manage.py migrate  # Pour effectuer les migrations
python manage.py runserver  # Pour lancer le serveur
```

3. Ouvrez votre navigateur et accédez à l'URL indiquée (généralement 'http://127.0.0.1:8000/')

4. Pour fermer le serveur, utilisez CTRL+Break

5. N'oubliez pas d'inscrire le nom de votre environnement virtuel dans le fichier .gitignore (Mettre une * devant le nom)


### DOCKER
Pour exécuter l'application sans rien installer d'autre que Docker, suivez les étapes ci-dessous:
1. Assurez-vous d’avoir Docker Desktop installé et en cours d’exécution sur votre machine.

2. Depuis la racine du projet, exécutez les commandes suivantes dans votre terminal:
   * Construire l'image Docker:
      docker-compose build

   * Lancer les conteneurs (serveur Django + base de données si ajoutée):
      docker-compose up

3. Une fois les conteneurs lancés, ouvrez votre navigateur et accédez à: 
      http://localhost:8000 ou http://127.0.0.1:8000

4. Pour arrêter l'exécution:
      docker-compose down

-----------------------------------------------------------------------------------------------------------------------------------
Partie Base de données 

1. Dans le fichier settings.py , à la partie Database, il y'a les infos pour la connexion avec la base de données
2. Il s'agit d'une base de données PostgreSql .
3. La base de données stocke les villes qui seront affichées dans le fichier html
4. Donc on aura plus besoin d'ajouter les villes manuellement dans le fichier views.py ou dans le fichier html.
5. Il faudra creer un superuser avec la commande python manage.py createsuperuser
6. Aller sur http://127.0.0.1:8000/admin et mettre les infos de connexion du superuser pour se connecter 
7. Et vous pourrez ajouter ou supprimer les villes 
8. Les villes déja mises seront enregistrées dans un fichier City.json pour vous permettre de les recuperer 
9. Vous ferez python manage.py loaddata City.json pour importer les données 

Nb: N'oubliez pas d'installer les nouvelles bibliothèques ajoutées dans le requirements.txt
-----------------------------------------------------------------------------------------------------------------------------------
Partie Docker-compose et Jenkinsfile 

1. Le Docker-compose a été modifier de sorte à prendre en compte l'application mais aussi la base de données .

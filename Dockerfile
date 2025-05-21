# Utiliser une image Python officielle légère
FROM python:3.10-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les paquets Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier l’ensemble du projet dans le conteneur
COPY . .

# Exposer le port utilisé par Django
EXPOSE 8000

# Commande exécutée au démarrage du conteneur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

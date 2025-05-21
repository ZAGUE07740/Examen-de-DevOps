# Utilise une image Python officielle
FROM python:3.12

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ouvrir le port 8000
EXPOSE 8000

# Commande pour exécuter le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

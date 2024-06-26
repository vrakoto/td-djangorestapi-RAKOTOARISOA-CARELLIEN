# Installation

Clonez le dépôt du projet depuis GitHub :

    git clone https://github.com/vrakoto/td-djangorestapi-RAKOTOARISOA-CARELLIEN.git

Accédez au répertoire du projet :

    cd projet-recherche-chercheur

Créez un environnement virtuel Python :

    python3 -m venv venv

Activez l'environnement virtuel sur Windows :

    venv\Scripts\activate


Installez les dépendances du projet :

    pip install -r requirements.txt

# Configuration

Effectuez les migrations de la base de données :

    python manage.py migrate

Créez un superutilisateur pour s'authentifier à l'application :

    python manage.py createsuperuser

Lancez le serveur de développement :

    python manage.py runserver

L'application devrait maintenant être accessible à l'adresse http://localhost:8000.

Une page de login devrait s'afficher dans un premier temps, les identifiants de connexion correspondent au superutilisateur créé précédemment.

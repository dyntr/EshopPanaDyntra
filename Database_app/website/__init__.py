"""
Hlavní konfigurační modul Flask aplikace

Tento modul obsahuje funkce pro vytvoření a konfiguraci Flask aplikace, včetně registrace blueprintů a nastavení globálních proměnných pro šablony.

Funkce:
- create_app(): Vytváří a konfiguruje instanci Flask aplikace.
"""

from flask import Flask, session
from src.db_connect import DbConnection

def create_app():
    """
    Vytváří a konfiguruje instanci Flask aplikace.

    Návratová hodnota:
    - app: Flask aplikace
    """
    # Získání instance databázového připojení
    db_conn = DbConnection.get_instance()

    # Vytvoření instance Flask aplikace
    app = Flask(__name__)

    # Konfigurace aplikace
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs' # Nastavení tajného klíče pro zabezpečení session
    app.config['SESSION_TYPE'] = 'filesystem' # Nastavení typu session na filesystem

    # Importování blueprintů
    from .views import views
    from .auth import auth

    # Registrace blueprintů
    app.register_blueprint(views)
    app.register_blueprint(auth)

    @app.before_request
    def before_request():
        """
        Funkce, která se provádí před každým požadavkem.
        Pokud je uživatel přihlášen, nastaví jeho jméno jako globální proměnnou pro šablony.
        """
        if 'username' in session:
            app.jinja_env.globals['username'] = session['username']

    return app

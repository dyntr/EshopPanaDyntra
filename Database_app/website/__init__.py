from flask import Flask, session
from src.db_connect import DbConnection


def create_app():
    db_conn = DbConnection.get_instance()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SESSION_TYPE'] = 'filesystem'
    

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views)
    app.register_blueprint(auth)
    
    @app.before_request
    def before_request():
        if 'username' in session:
            app.jinja_env.globals['username'] = session['username']

    return app
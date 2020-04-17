from flask import Flask
import connexion
from config import get_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Create flask application instance
    connex_app = connexion.App(__name__, specification_dir='../openapi/')

    # Read specification.yml to configure the endpoints
    connex_app.add_api('specification.yml')

    app = connex_app.app
    env_config_obj = get_config()
    app.config.from_object(env_config_obj)

    db.init_app(app)
    with app.app_context():
           db.create_all()
    
    return app
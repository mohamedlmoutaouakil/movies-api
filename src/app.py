from flask import Flask
import connexion
from config import get_config, get_log_level
from flask_sqlalchemy import SQLAlchemy
import logging

# logging.basicConfig(level=get_log_level())

# Create handlers
c_handler = logging.StreamHandler()
# Create formatters and add them to handlers
c_formatter = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_formatter)

# Add handler to loggers of all modules
for logger in (
       logging.getLogger('app'),
       logging.getLogger('movies')
):
    logger.addHandler(c_handler)
    logger.setLevel(get_log_level())

# Get app logger
logger = logging.getLogger('app')

db = SQLAlchemy()

def create_app():
    # Create flask application instance
    connex_app = connexion.App(__name__, specification_dir='../openapi/')

    # Read specification.yml to configure the endpoints
    connex_app.add_api('specification.yml')
    logger.info('Created flask app using connexion.')

    app = connex_app.app
    env_config_obj = get_config()
    app.config.from_object(env_config_obj)

    db.init_app(app)
    with app.app_context():
           db.create_all()
    logger.info('Initialized and created the database.')

    return app
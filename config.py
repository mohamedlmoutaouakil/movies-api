from environs import Env
import os

env = Env()
env.read_env() # read .env file, if it exists

basedir = os.path.abspath(os.path.dirname(__file__))

def get_config():
    FLASK_ENV = env.str('FLASK_ENV', 'production')
    if FLASK_ENV == 'production':
        return 'config.ProdConfig'
    elif FLASK_ENV == 'testing':
        return 'config.TestConfig'
    elif FLASK_ENV == 'development':
        return 'config.DevConfig'


class Config(object):
    # Set configuration variables

    # General config
    DEBUG = False
    TESTING = False
    APP_ROOT = basedir

    # Database
    DB_NAME = env.str('DB_NAME', 'dev.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_ROOT, 'databases', DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    SQLALCHEMY_ECHO = env.bool('SQLALCHEMY_ECHO', False)

class ProdConfig(Config):
    ENV = "production"

class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True

class TestConfig(Config):
    ENV = "testing"
    TESTING = True
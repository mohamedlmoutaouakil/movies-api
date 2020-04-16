from environs import Env

env = Env()
env.read_env() # read .env file, if it exists

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

    DEBUG = False
    TESTING = False
    HOST = env.str('HOST', '127.0.0.1')
    PORT = env.int('PORT', 5000)

class ProdConfig(Config):
    ENV = "production"

class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True

class TestConfig(Config):
    ENV = "testing"
    TESTING = True
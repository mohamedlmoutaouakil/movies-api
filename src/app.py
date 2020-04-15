from flask import Flask
import connexion
import os

def create_app():
    # Create flask application instance
    app = connexion.App(__name__, specification_dir='../openapi/')

    # Read specification.yml to configure the endpoints
    app.add_api('specification.yml')

    return app.app
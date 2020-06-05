import pytest
from src.app import create_app, db
from config import get_config

@pytest.fixture(scope='function')
def setup_db():
    app = create_app()
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='function')
def test_client():
    app = create_app()
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
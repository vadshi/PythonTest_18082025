import pytest
import random
from app import create_app


@pytest.fixture(scope="session")
def app():
    """ Session-wide test 'app' fixture """
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql://user:password@host/dummy_db", # Dummy database URL
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(app_config=test_config)

    with app.app_context():
        yield app


@pytest.fixture
def test_client(app):
    """ Test client for the app """
    return app.test_client()


@pytest.fixture
def user_payload():
    suffix = random.randint(1, 100)
    return {
        "username": f"user_{suffix}",
        "email": f"user_{suffix}@mail.com",
    }
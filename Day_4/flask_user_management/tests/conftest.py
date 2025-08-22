import pytest
import random
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.exc import OperationalError as SQLAlchemyOperationalError
from app import create_app
from models import db


def pytest_addoption(parser):
    parser.addoption(
        "--dburl", # For Postgres use "postgresql://user:password@host/dbname"
        action="store",
        default="sqlite:///:memory:", # Default use SQLite in-memory database,
        help="Database URL use to tests",
    )

@pytest.fixture(scope="session")
def db_url(request):
    return request.config.getoption("--dburl")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    db_url = session.config.getoption("--dburl")
    try:
        # Attempt to create an engine and connect to the database
        engine = create_engine(
            db_url,
            poolclass=StaticPool,
        )
        connection = engine.connect()
        connection.close() # Clone the connection right after a successfull connect
        print("Using Database URL", db_url)
        print("Database connection successful ...")
    except SQLAlchemyOperationalError as e:
        print(f"Failed to connect to the database at {db_url}: {e}")
        pytest.exit(reason="Stopping tests because database connection could not be established")


@pytest.fixture(scope="session")
def app(db_url):
    """ Session-wide test 'app' fixture """
    test_config = {
        "SQLALCHEMY_DATABASE_URI": db_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(app_config=test_config)

    with app.app_context():
        db.create_all()
        yield app

        # Close the database session and drop all tables after the session
        db.session.remove()
        # db.drop_all()


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
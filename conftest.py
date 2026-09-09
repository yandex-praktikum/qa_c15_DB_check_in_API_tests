import pytest

from api.client import ApiClient
from db.client import DatabaseClient
from db.seed import create_database
from fixtures.db_fixtures import courier


def pytest_sessionstart(session):
    create_database()


@pytest.fixture
def api():
    return ApiClient()


@pytest.fixture
def db():
    return DatabaseClient()
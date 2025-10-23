import pytest

from test import create_client_from_env


@pytest.fixture
def client():
    yield create_client_from_env()

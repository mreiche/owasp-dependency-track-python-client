import pytest

from test import api


@pytest.fixture(scope="session")
def client():
    yield api.create_client_from_env()


@pytest.fixture(scope="session")
def client_v2():
    yield api.create_client_from_env("/api/v2")

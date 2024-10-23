import pytest

from test import api


@pytest.fixture
def client():
    yield api.create_client_from_env()

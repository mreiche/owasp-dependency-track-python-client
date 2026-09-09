import pytest

from owasp_dt import utils

@pytest.fixture(scope="session")
def client():
    yield utils.create_client_from_env()


@pytest.fixture(scope="session")
def client_v2():
    yield utils.create_client_from_env("/api/v2")

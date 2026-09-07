import pytest
from tinystream import Stream

import owasp_dt
from owasp_dt.api.user import create_managed_user, get_managed_users, delete_managed_user
from owasp_dt.models import ManagedUser

__test_user = ManagedUser(
    username="test-user",
    fullname="Test User Full Name",
    email="test-user@example.com",
    new_password="test-password",
    confirm_password="test-password",
)

def test_create_managed_user(client: owasp_dt.Client):
    resp = create_managed_user.sync_detailed(client=client, body=__test_user)
    assert resp.status_code in [201, 409]

@pytest.mark.depends(on=["test_create_managed_user"])
def test_created_managed_user(client: owasp_dt.Client):
    global __test_user
    users = get_managed_users.sync(client=client)
    opt_test_user = Stream(users).find(lambda user: user.username == "test-user")
    assert opt_test_user.present
    __test_user = opt_test_user.get()

@pytest.mark.depends(on=["test_created_managed_user"])
def test_delete_managed_user(client: owasp_dt.Client):
    resp = delete_managed_user.sync_detailed(client=client, body=__test_user)
    assert resp.status_code == 204

@pytest.mark.depends(on=["test_delete_managed_user"])
def test_deleted_managed_user(client: owasp_dt.Client):
    users = get_managed_users.sync(client=client)
    assert Stream(users).filter(lambda user: user.username == "test-user").count() == 0

# @pytest.fixture(scope="module", autouse=True)
# def cleanup_managed_user(request, client: owasp_dt.Client):
#     request.addfinalizer(
#         lambda: delete_managed_user.sync_detailed(client=client, body=__test_user)
#     )

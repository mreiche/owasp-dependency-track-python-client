import pytest
from tinystream import Stream

import owasp_dt
from owasp_dt.api.team import get_teams, create_team, delete_team
from owasp_dt.models import Team

__test_team = Team(
    uuid="",
    name="test-team",
)

def test_create_team(client: owasp_dt.Client):
    resp = create_team.sync_detailed(client=client, body=__test_team)
    assert resp.status_code in [201, 409]
    # __test_team = resp.parsed

@pytest.mark.depends(on=["test_create_team"])
def test_created_team(client: owasp_dt.Client):
    global __test_team
    teams = get_teams.sync(client=client)
    opt_team = Stream(teams).find(lambda team: team.name == "test-team")
    assert opt_team.present
    __test_team = opt_team.get()

@pytest.mark.depends(on=["test_created_team"])
def test_delete_team(client: owasp_dt.Client):
    team_to_delete = Team(uuid=__test_team.uuid, name="")
    resp = delete_team.sync_detailed(client=client, body=team_to_delete)
    assert resp.status_code == 204

@pytest.mark.depends(on=["test_delete_team"])
def test_deleted_team(client: owasp_dt.Client):
    teams = get_teams.sync(client=client)
    assert Stream(teams).filter(lambda team: team.name == "test-team").count() == 0

# @pytest.fixture(scope="module", autouse=True)
# def cleanup_team(client: owasp_dt.Client):
#     yield
#     delete_team.sync_detailed(client=client, body=__test_team)

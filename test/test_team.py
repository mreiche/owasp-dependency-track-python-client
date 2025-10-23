from owasp_dt.api.team import get_teams
import owasp_dt

def test_team_epoch(client: owasp_dt.Client):
    teams = get_teams.sync(client=client)
    for team in teams:
        pass

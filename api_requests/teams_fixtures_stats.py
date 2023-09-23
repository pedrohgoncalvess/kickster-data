from handlers.managers import Managers
from api_requests.address_request import Request
from database.operations import Operations


def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()

    relationTeamsLeague = dataFromDb.get_relation_team_league_id()
    for teamLeague in relationTeamsLeague:
        idLeague = teamLeague[1]
        idTeam = teamLeague[0]
        teamLeagueRawResponse = req.team_league_stats(idTeam, idLeague)
        manager.team_league_fixtures_stats_management(teamLeagueRawResponse)

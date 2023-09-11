from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()

if __name__ == '__main__':
    idTeams = [135]
    idLeague = 71
    for idTeam in idTeams:
        teamLeagueRawResponse = req.team_league_stats(idTeam, idLeague)
        manager.team_league_stats_management(teamLeagueRawResponse)
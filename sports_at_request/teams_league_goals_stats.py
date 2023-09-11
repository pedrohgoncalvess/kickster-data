from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()


if __name__ == '__main__':
    relationTeamsLeague = dataFromDb.get_all_league_teams_id()
    for teamLeague in relationTeamsLeague:
        idLeague = relationTeamsLeague.get(teamLeague).get("id_league")
        idTeam = relationTeamsLeague.get(teamLeague).get("id_team")
        teamLeagueGoalsRawResponse = req.team_league_stats(idTeam, idLeague)
        manager.team_league_goals_stats_management(teamLeagueGoalsRawResponse)
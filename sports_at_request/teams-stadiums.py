from database.data_from_db import DataFromDatabase
from sports_at_request.address_request import Request
from handlers.managers import Managers
from handlers.validators import Validators

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()
idLeagues = dataFromDb.get_all_league_id()


if __name__ == '__main__':
    for idLeague in idLeagues:
        teamsAndStadiumResponseRaw = req.team_stadium(id_league=idLeague)
        manager.stadium_management(stadium_infos=teamsAndStadiumResponseRaw)
        manager.team_management(team_info=teamsAndStadiumResponseRaw)

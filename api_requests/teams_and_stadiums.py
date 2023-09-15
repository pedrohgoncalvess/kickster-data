from database.data_from_db import DataFromDatabase
from api_requests.address_request import Request
from handlers.managers import Managers

def main():
    req = Request()
    manager = Managers()
    dataFromDb = DataFromDatabase()
    idLeagues = dataFromDb.get_all_league_id()


    for idLeague in idLeagues:
        teamsAndStadiumResponseRaw = req.team_stadium(id_league=idLeague)
        manager.stadium_management(stadium_infos=teamsAndStadiumResponseRaw)
        manager.team_management(team_info=teamsAndStadiumResponseRaw)

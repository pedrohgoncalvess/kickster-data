from database.data_from_db import DataFromDatabase
from api_requests.address_request import Request
from handlers.managers import Managers


def main():
    req = Request()
    manager = Managers()
    dataFromDb = DataFromDatabase()
    idLeagues = dataFromDb.get_all_leagues_id()

    for idLeague in idLeagues:
        teamsResponseRaw = req.team_stadium(id_league=idLeague)
        manager.team_management(team_info=teamsResponseRaw)

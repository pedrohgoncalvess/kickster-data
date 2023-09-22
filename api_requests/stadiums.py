from database.operations import Operations
from api_requests.address_request import Request
from handlers.managers import Managers


def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()
    idLeagues = dataFromDb.get_all_leagues_id()

    for idLeague in idLeagues:
        stadiumResponseRaw = req.team_stadium(id_league=idLeague)
        manager.stadium_management(stadium_infos=stadiumResponseRaw)

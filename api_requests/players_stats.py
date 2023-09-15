from handlers.managers import Managers
from api_requests.address_request import Request
from database.data_from_db import DataFromDatabase

def main():
    req = Request()
    manager = Managers()
    dataFromDb = DataFromDatabase()

    idPlayers = dataFromDb.get_all_players_id_serie_a()
    for idPlayer in idPlayers:
        playerStatJson = req.player_stats(idPlayer)
        manager.player_stats_management(playerStatJson)
from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()

if __name__ == '__main__':
    idPlayers = dataFromDb.get_all_players_id_serie_a()
    #idPlayers = [30443]
    for idPlayer in idPlayers:
        playerStatJson = req.player_stats(idPlayer)
        manager.player_stats_management(playerStatJson)
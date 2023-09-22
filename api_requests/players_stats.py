from handlers.managers import Managers
from api_requests.address_request import Request
from database.operations import Operations

def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()

    idPlayers = dataFromDb.get_all_players_id()
    for idPlayer in idPlayers:
        playerStatJson = req.player_stats(idPlayer)
        manager.player_stats_management(playerStatJson)
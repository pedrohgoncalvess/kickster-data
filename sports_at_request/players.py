import requests
from env_var import getHeaders
from database.operations import dbOperations
from database.validators import Validators
from datetime import datetime

validator = Validators()


def make_team_player_request(id_league: str | int, page: str | int = 1) -> tuple[list[dict[str, dict]], str | int, int]:
    headers: dict = getHeaders()

    url: str = f"https://v3.football.api-sports.io/players?team={id_league}&season={datetime.now().year}&page={page}"

    req = requests.get(url, headers=headers)
    response: dict = req.json()
    players: list[dict[str, dict]] = response.get('response')
    maxPage = response.get('paging').get('total')

    return players, page, maxPage


def insert_json_players(players_request_raw: list[dict[str:dict[str:any]]]):
    playersInserted: list[int] = []
    for player in players_request_raw:
        idPlayer = player.get('player').get('id')
        if idPlayer not in playersInserted:
            dbOperations.player_management(player)
            playersInserted.append(idPlayer)


if __name__ == '__main__':
    idTeams = dbOperations.get_all_teams_id()
    for team in idTeams:
        request, currentPage, maxPage = make_team_player_request(team)
        insert_json_players(request)

        while currentPage <= maxPage:
            currentPage += 1
            request, currentPage, _ = make_team_player_request(team, currentPage)
            insert_json_players(request)

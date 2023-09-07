from env_var import getHeaders
import requests
from datetime import datetime


class Request:
    def __init__(self):
        self.headers: dict = getHeaders()

    def team_player(self, id_team: str | int, page: str | int) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/players?team={id_team}&season={datetime.now().year}&page={page}"

        req = requests.get(url, headers=self.headers)
        return req.json()

    def champs(self, country: str, camp_type: str) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/leagues?country={country}&type={camp_type}"

        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def team_stadium(self, country: str) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/teams?country={country}"

        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def team_squad(self, id_team: str | int) -> dict[any:any]:
        url = f"https://v3.football.api-sports.io/players/squads?team={id_team}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def champ_fixture(self, id_champ: str | int, season: str | int):
        url = f"https://v3.football.api-sports.io/fixtures?league={id_champ}&season={season}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def fixture_stats(self, id_fixture: str | int) -> list[dict[str:any]]:
        url = f"https://v3.football.api-sports.io/fixtures/statistics?fixture={id_fixture}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

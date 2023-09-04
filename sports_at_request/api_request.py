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
        return req.json()

    def team_stadium(self, country: str) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/teams?country={country}"

        req = requests.get(url, headers=self.headers)
        return req.json()


from database.generator import Queries
from database.connection import DatabaseConnection
from sqlalchemy import select
from models import leagues_model, players_model, teams_model


class DataFromDatabase:
    def __init__(self):
        self.queries = Queries()
        self.execute_query = DatabaseConnection().query_objects

    def get_all_leagues_id(self):
        statementIdLeagues = select(leagues_model.Leagues.id)
        results = self.execute_query(statementIdLeagues)
        idLeagues = []
        for idLeague in results:
            idLeagues.append(idLeague[0])

        return idLeagues

    def get_all_teams_id(self):
        statementIdTeams = select(teams_model.Teams.id)
        results = self.execute_query(statementIdTeams)
        idTeams = []
        for idTeam in results:
            idTeams.append(idTeam[0])

        return idTeams

    def get_all_players_id(self):
        statementIdPlayers = select(players_model.Players.id)
        results = self.execute_query(statementIdPlayers)
        idPlayers = []
        for idPlayer in results:
            idPlayers.append(idPlayer[0])

        return idPlayers


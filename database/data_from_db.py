from handlers.generators import Queries
from database.connection import DatabaseConnection
from sqlalchemy import select
from models import leagues_model, players_model, teams_model, stadiums_model, fixtures_model


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

    def get_all_stadiums_id(self):
        statementIdStadiums = select(stadiums_model.Stadiums.id)
        results = self.execute_query(statementIdStadiums)
        idStadiums = []
        for idStadium in results:
            idStadiums.append(idStadium[0])

        return idStadiums

    def get_all_fixtures_id(self):
        statementIdFixtures = select(fixtures_model.Fixtures.id)
        results = self.execute_query(statementIdFixtures)
        idFixtures = []
        for idFixture in results:
            idFixtures.append(idFixture[0])

        return idFixtures



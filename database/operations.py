from database.connection import DatabaseConnection
from sqlalchemy import select
from models import leagues_model, players_model, teams_model, stadiums_model, fixtures_model
from sqlalchemy import update
from datetime import datetime


class Operations:
    def __init__(self):
        self.__connection__ = DatabaseConnection()
        self.execute_query = self.__connection__.query_objects
        self.update_query = self.__connection__.update_objects
        self.actual_season = datetime.now().year

    def get_all_leagues_id(self):
        statementIdLeagues = select(leagues_model.Leagues.id_league)
        results = self.execute_query(statementIdLeagues)
        idLeagues = []
        for idLeague in results:
            idLeagues.append(idLeague[0])

        return idLeagues

    def get_all_leagues_intern_id(self):
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

    def get_finished_fixtures_id(self):
        statementIdFinishedFixtures = select(fixtures_model.Fixtures.id).where(
            fixtures_model.Fixtures.status == 'match_finished')
        results = self.execute_query(statementIdFinishedFixtures)
        idFinishedFixtures = []
        for idFixture in results:
            idFinishedFixtures.append(idFixture[0])

        return idFinishedFixtures

    def get_relation_team_league_id(self):
        statementRelationTeamLeague = select(fixtures_model.Fixtures.id_team_home.distinct(),
                                             leagues_model.Leagues.id_league).join(leagues_model.Leagues)
        results = self.execute_query(statementRelationTeamLeague)
        return results

    def get_relation_id_season_leagues(self):
        queryToGetId = select(leagues_model.Leagues.id, leagues_model.Leagues.id_league, leagues_model.Leagues.season)
        results = self.execute_query(queryToGetId)
        relationIdLeagues = {}
        if len(results) > 0:
            for result in results:
                relationIdLeagues.update({f"{result[1]}-{result[2]}": result[0]})
            return relationIdLeagues

    def set_collected_fixtures_stats(self, id_fixture: int):
        queryToGetFixture = (update(fixtures_model.Fixtures).where(fixtures_model.Fixtures.id == id_fixture)).values(
            data_stats='collected')
        resultOfUpdate = self.update_query(queryToGetFixture)
        return resultOfUpdate

    def set_collected_fixtures_events(self, id_fixture: int):
        queryToGetFixture = (update(fixtures_model.Fixtures).where(fixtures_model.Fixtures.id == id_fixture)).values(
            data_events='collected')
        resultOfUpdate = self.update_query(queryToGetFixture)
        return resultOfUpdate

    def set_collected_fixtures_lineups(self, id_fixture: int):
        queryToGetFixture = (update(fixtures_model.Fixtures).where(fixtures_model.Fixtures.id == id_fixture)).values(
            data_lineups='collected')
        resultOfUpdate = self.update_query(queryToGetFixture)
        return resultOfUpdate

    def get_not_collectd_fixtures_stats(self):
        statementNotStatsCollectdFixtures = select(fixtures_model.Fixtures.id).where(
            fixtures_model.Fixtures.status == 'match_finished', fixtures_model.Fixtures.data_stats == 'waiting')
        results = self.execute_query(statementNotStatsCollectdFixtures)
        notStatsCollectedFixtures = []
        for idFixture in results:
            notStatsCollectedFixtures.append(idFixture[0])

        return notStatsCollectedFixtures

    def get_not_collectd_fixtures_events(self):
        statementNotEventsCollectdFixtures = select(fixtures_model.Fixtures.id).where(
            fixtures_model.Fixtures.status == 'match_finished', fixtures_model.Fixtures.data_events == 'waiting')
        results = self.execute_query(statementNotEventsCollectdFixtures)
        notEventsCollectedFixtures = []
        for idFixture in results:
            notEventsCollectedFixtures.append(idFixture[0])

        return notEventsCollectedFixtures

    def get_not_collectd_fixtures_lineups(self):
        statementNotLineupsCollectdFixtures = select(fixtures_model.Fixtures.id).where(
            fixtures_model.Fixtures.status == 'match_finished', fixtures_model.Fixtures.data_lineups == 'waiting')
        results = self.execute_query(statementNotLineupsCollectdFixtures)
        notLineupsCollectedFixtures = []
        for idFixture in results:
            notLineupsCollectedFixtures.append(idFixture[0])

        return notLineupsCollectedFixtures

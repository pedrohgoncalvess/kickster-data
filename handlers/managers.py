from database.connection import db_connection
from typing import NoReturn
from handlers.parsers import Parsers
from handlers.generators import Generators
from database.operations import Operations


class Managers:
    def __init__(self):
        self.parser = Parsers()
        self.generator = Generators()
        self.data_from_db = Operations()
        self.__insert__ = db_connection.insert_object
        self.__set_data_stats_collected__ = self.data_from_db.set_collected_fixtures_stats
        self.__set_data_events_collected__ = self.data_from_db.set_collected_fixtures_events
        self.__set_data_lineups_collected__ = self.data_from_db.set_collected_fixtures_lineups
        self.execute_update_query = "pass"

    def stadium_management(self, stadium_infos: dict[str:str]) -> NoReturn:
        for stadium in stadium_infos:
            stadiumInfosTreated: dict = self.parser.stadium_parser(stadium)
            newStadium = self.generator.generator_stadium(stadium_values=stadiumInfosTreated)
            self.__insert__(newStadium)

    def team_management(self, team_info: dict[str:any]) -> NoReturn:
        for team in team_info:
            teamInfos = self.parser.team_parser(team)
            newTeam = self.generator.generator_team(team_values=teamInfos)
            self.__insert__(newTeam)

    def league_management(self, league_infos: dict[str, dict]):
        for league in league_infos:
            leagueInfos = self.parser.league_parser(league)
            newLeague = self.generator.generator_league(leagueInfos)
            self.__insert__(newLeague)

    def player_management(self, player_values: list[dict[str:str]]):
        playersInDb = self.data_from_db.get_all_players_id()
        for playerValue in player_values:
            if len(playersInDb) != 0:
                playerInfos = self.parser.player_parser(playerValue)
                idPlayer = playerInfos.get("id")

                if idPlayer not in playersInDb:
                    newPlayer = self.generator.generator_player(playerInfos)
                    self.__insert__(newPlayer)
            else:
                playerInfos = self.parser.player_parser(playerValue)
                newPlayer = self.generator.generator_player(playerInfos)
                self.__insert__(newPlayer)

    def fixture_management(self, fixtures_values: dict) -> NoReturn:
        stadiumsInDB = self.data_from_db.get_all_stadiums_id()
        fixturesInDb = []
        for fixtureValues in fixtures_values:
            fixturesInfos = self.parser.fixture_parser(fixtureValues)
            fixtureId = fixturesInfos.get("id_fixture")

            stadiumId = fixturesInfos.get("id_stadium")
            if stadiumId not in stadiumsInDB:
                fixturesInfos.update({"id_stadium": None})

            if fixtureId not in fixturesInDb:
                newFixture = self.generator.generator_fixture(fixturesInfos)
                self.__insert__(newFixture)

    def fixture_stats_management(self, fixture_stats_values: list[dict[str:any]],
                                 fixture_lineups_values: list[dict[str:any]], fixture_id: int) -> NoReturn:

        for team_stats in fixture_stats_values:
            fixtureStatsInfo = self.parser.fixture_stats_parser(team_stats, fixture_lineups_values, fixture_id)
            newFixtureStat = self.generator.generator_fixture_stats(fixtureStatsInfo)
            idFixture = newFixtureStat.id_fixture
            resultInsert = self.__insert__(newFixtureStat)
            if resultInsert is True:
                self.__set_data_stats_collected__(idFixture)

    def fixture_event_management(self, fixture_events_values: list[dict[str:any]], fixture_id: int):
        eventsInserted = []
        for event in fixture_events_values:
            fixtureEventInfo = self.parser.fixture_events_parser(event, fixture_id)
            newFixtureEvent = self.generator.generator_fixture_event(fixtureEventInfo)
            compostKey = f"{fixture_id}-{newFixtureEvent.id_team}-{newFixtureEvent.time}-{newFixtureEvent.type_event}"
            if compostKey not in eventsInserted:
                result = self.__insert__(newFixtureEvent)
                eventsInserted.append(compostKey)
                if result is True:
                    self.__set_data_events_collected__(fixture_id)

    def team_squad_management(self, players_squad_values: list[dict[str:any]]) -> NoReturn:
        playersSquadInfo = self.parser.team_squad_parser(players_squad_values[0])

        for playerInfo in playersSquadInfo:
            newSquadMember = self.generator.generator_team_player_squad(playerInfo)
            self.__insert__(newSquadMember)

    def player_stats_management(self, player_stats_values: list[dict[str:any]]) -> NoReturn:
        leaguesInDb = self.data_from_db.get_all_leagues_intern_id()
        playerStat = self.parser.player_stats_parser(player_stats_values)
        playersLeagueInserted = []
        for stat in playerStat:
            newPlayerStat = self.generator.generator_player_stat(stat)
            compostKey = f"{newPlayerStat.id_player}-{newPlayerStat.id_league}"
            if newPlayerStat.id_league in leaguesInDb:
                if compostKey not in playersLeagueInserted:
                    self.__insert__(newPlayerStat)
                    playersLeagueInserted.append(compostKey)

    def team_league_fixtures_stats_management(self, team_league_stat_values: dict[str:any]) -> NoReturn:
        teamLeagueStat = self.parser.team_league_fixtures_stats_parser(team_league_stat_values)
        newTeamStat = self.generator.generator_team_league_fixtures_stats(teamLeagueStat)
        self.__insert__(newTeamStat)

    def team_league_goals_stats_management(self, team_league_goals_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueGoalsStat = self.parser.team_league_goals_stats_parser(team_league_goals_stats_values)
        for typeGoal in teamLeagueGoalsStat:
            queryInsert = self.generator.generator_team_league_goals_stats(typeGoal)
            self.__insert__(queryInsert)

    def team_league_cards_stats_management(self, team_league_cards_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueCardsStats = self.parser.team_league_cards_stats_parser(team_league_cards_stats_values)
        for typeCard in teamLeagueCardsStats:
            newTeamStatTypeCard = self.generator.generator_team_league_cards_stats(typeCard)
            self.__insert__(newTeamStatTypeCard)

    def fixture_lineups_management(self, fixture_lineups_values: list[dict[str:any]],
                                   id_fixture: str | int) -> NoReturn:
        for teamLineUp in fixture_lineups_values:
            fixtureTeamLineUp = self.parser.fixture_lineup_parser(teamLineUp, id_fixture)
            for playerInLineUp in fixtureTeamLineUp:
                newPlayerInFixtureLineup = self.generator.generator_fixture_lineup(playerInLineUp)
                self.__insert__(newPlayerInFixtureLineup)
        self.__set_data_lineups_collected__(id_fixture=id_fixture)


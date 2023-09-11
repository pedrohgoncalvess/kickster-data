from database.connection import DatabaseConnection
from typing import NoReturn
from handlers.validators import Validators
from database.queries import Queries


class Managers:
    def __init__(self):
        self.validator = Validators()
        self.queries = Queries()
        self.__operations__ = DatabaseConnection()
        self.execute_insert_query = self.__operations__.__perform_insert_query__
        self.execute_update_query = self.__operations__.__perform__update_query__

    def stadium_management(self, stadium_infos: dict[str:str]) -> NoReturn:
        for stadium in stadium_infos:
            stadiumInfosTreated: dict = self.validator.stadium_validator(stadium)
            queryInsert = self.queries.insert_stadium(stadium_values=stadiumInfosTreated)

            self.execute_insert_query(queryInsert)

    def team_management(self, team_info: dict[str:any]) -> NoReturn:
        for team in team_info:
            teamInfos = self.validator.team_validator(team)
            queryInsert = self.queries.insert_team(team_values=teamInfos)

            self.execute_insert_query(queryInsert)

    def league_management(self, champ_infos: dict[str, dict]):
        leagueInfos = self.validator.league_validator(champ_infos)
        queryInsert = self.queries.insert_league(leagueInfos)

        self.execute_insert_query(queryInsert)

    def player_management(self, player_values: dict):
        playerInfos = self.validator.player_validator(player_values)
        queryInsert = self.queries.insert_player(playerInfos)

        self.execute_insert_query(queryInsert)

    def fixture_management(self, fixtures_values: dict) -> NoReturn:
        for fixtureValues in fixtures_values:
            fixturesInfos = self.validator.fixture_validator(fixtureValues)
            queryInsert = self.queries.insert_fixture(fixturesInfos)

            self.execute_insert_query(queryInsert)

    def team_squad_management(self, players_squad_values: list[dict[str:any]]) -> NoReturn:
        playersSquadInfo = self.validator.team_squad_validator(players_squad_values[0])

        for playerInfo in playersSquadInfo:
            queryInsert = self.queries.insert_team_player_squad(playerInfo)

            self.execute_insert_query(queryInsert)

    def fixture_stats_management(self, fixture_stats_values: list[dict[str:any]], fixture_lineups_values:list[dict[str:any]],fixture_id: int) -> NoReturn:
        for team_stats in fixture_stats_values:
            fixtureStatsInfo = self.validator.fixture_stats_validator(team_stats, fixture_lineups_values,fixture_id)
            queryInsert = self.queries.insert_fixture_stats(fixtureStatsInfo)
            self.execute_insert_query(queryInsert)

    def fixture_event_management(self, fixture_events_values: list[dict[str:any]], fixture_id: int):
        for event in fixture_events_values:
            fixtureEventInfo = self.validator.fixture_events_validator(event, fixture_id)
            queryInsert = self.queries.insert_fixture_event(fixtureEventInfo)
            self.execute_insert_query(queryInsert)
        queryUpdate = self.queries.update_fixture_data_status(fixture_id)
        self.execute_update_query(queryUpdate)

    def player_stats_management(self, player_stats_values: list[dict[str:any]]) -> NoReturn:
        playerStat = self.validator.player_stats_validator(player_stats_values)
        for stat in playerStat:
            queryInsert = self.queries.insert_player_stat(stat)
            self.execute_insert_query(queryInsert)

    def team_league_fixtures_stats_management(self, team_league_stat_values:dict[str:any]) -> NoReturn:
        teamLeagueStat = self.validator.team_league_fixtures_stats_validator(team_league_stat_values)
        queryInsert = self.queries.insert_team_league_fixtures_stats(teamLeagueStat)
        self.execute_insert_query(queryInsert)

    def team_league_goals_stats_management(self, team_league_goals_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueGoalsStat = self.validator.team_league_goals_stats_validator(team_league_goals_stats_values)
        for typeGoal in teamLeagueGoalsStat:
            queryInsert = self.queries.insert_team_league_goals_stats(typeGoal)
            self.execute_insert_query(queryInsert)

    def team_league_cards_stats_management(self, team_league_cards_stats_values:list[dict[str:any]]) -> NoReturn:
        teamLeagueCardsStats = self.validator.team_league_cards_stats_validator(team_league_cards_stats_values)
        for typeCard in teamLeagueCardsStats:
            queryInsert = self.queries.insert_team_league_cards_stats(typeCard)
            self.execute_insert_query(queryInsert)


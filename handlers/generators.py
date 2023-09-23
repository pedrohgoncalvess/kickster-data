from models import (
    stadiums_model, teams_model, leagues_model,
    players_model, fixtures_model, fixtures_stats_model,
    players_stats_model, teams_squad_model, fixtures_events_model,
    teams_fixtures_stats_model, teams_cards_stats_model, teams_goals_stats_model
)

class Generators:

    def generator_stadium(self, stadium_values: dict[str:str]) -> stadiums_model.Stadiums:

        idExStadium = stadium_values.get('id')
        nameStadium = stadium_values.get('name')
        stateStadium = stadium_values.get('state')
        cityStatium = stadium_values.get('city')
        addressStatium = stadium_values.get('address')
        capacityStatium = stadium_values.get('capacity')
        surfaceStadium = stadium_values.get('surface')
        imageStadium = stadium_values.get('image')

        newStadium = stadiums_model.Stadiums(
            id=idExStadium, name=nameStadium, state=stateStadium, city=cityStatium, address=addressStatium,
            capacity=capacityStatium, surface=surfaceStadium, image=imageStadium
                                              )

        return newStadium

    def generator_team(self, team_values: dict[str:str]) -> teams_model.Teams:

        idExTeam = team_values.get('id')
        idStadium = team_values.get('id_stadium')
        nameTeam = team_values.get('name')
        logoTeam = team_values.get('logo')
        nationalTeam = team_values.get('national')
        codeTeam = team_values.get('code')
        countryTeam = team_values.get('country')
        foundedTeam = team_values.get('founded')

        newTeam = teams_model.Teams(
            id=idExTeam, id_stadium=idStadium, name=nameTeam, code=codeTeam, country=countryTeam,
            logo=logoTeam, national=nationalTeam, founded=foundedTeam
        )

        return newTeam

    def generator_league(self, leagues_values: dict[str:any]) -> leagues_model.Leagues:

        idLeague = leagues_values.get("id")
        nameLeague = leagues_values.get('name')
        startLeague = leagues_values.get('start')
        endLeague = leagues_values.get('end')
        logoLeague = leagues_values.get('logo')
        countryLeague = leagues_values.get('country')
        typeLeague = leagues_values.get('type')
        seasonLeague = leagues_values.get('season')

        newLeague = leagues_model.Leagues(
            id_league=idLeague, name=nameLeague, start_league=startLeague, end_league=endLeague, type=typeLeague,
            season=seasonLeague, country=countryLeague, logo=logoLeague
        )

        return newLeague

    def generator_player(self, player_values: dict[str:any]) -> players_model.Players:

        idPlayer = player_values.get('id')
        namePlayer = player_values.get('name')
        firstNamePlayer = player_values.get('first_name')
        lastNamePlayer = player_values.get('last_name')
        birthPlayer = player_values.get('birth')
        nationalityPlayer = player_values.get('nationality')
        heightPlayer = player_values.get('height')
        weightPlayer = player_values.get('weight')
        imagePlayer = player_values.get('photo')

        newPlayer = players_model.Players(
            id=idPlayer, name=namePlayer, first_name=firstNamePlayer, last_name=lastNamePlayer, date_of_birth=birthPlayer,
            nationality=nationalityPlayer, height=heightPlayer, weight=weightPlayer, image=imagePlayer
        )

        return newPlayer

    def generator_fixture(self, fixture_values: dict[str:any]) -> fixtures_model.Fixtures:
        idFixture = fixture_values.get("id_fixture")
        dateFixture = fixture_values.get("date")
        refereeFixture = fixture_values.get("referee")
        idStadiumFixture = fixture_values.get("id_stadium")
        idHomeTeamFixture = fixture_values.get("home_team")
        idAwayTeamFixture = fixture_values.get("away_team")
        idLeague = fixture_values.get("id_league")
        roundFixture = fixture_values.get("round")
        seasonFixture = fixture_values.get("season")
        resultFixture = fixture_values.get("result")
        statusFixture = fixture_values.get("status")

        newFixture = fixtures_model.Fixtures(
            id=idFixture, id_stadium=idStadiumFixture, id_team_home=idHomeTeamFixture, id_team_away=idAwayTeamFixture,
            id_league=idLeague, start_at=dateFixture, result=resultFixture, referee=refereeFixture, round=roundFixture,
            status=statusFixture
        )

        return newFixture

    def generator_team_player_squad(self, player_squad_infos: dict[str:any]) -> teams_squad_model.TeamsSquad:
        idPlayer = player_squad_infos.get("id_player")
        idTeam = player_squad_infos.get("id_team")
        positionPlayer = player_squad_infos.get("position")
        numberPlayer = player_squad_infos.get("number")
        injured = player_squad_infos.get("injured")

        newSquadMember = teams_squad_model.TeamsSquad(
            id_player=idPlayer, id_team=idTeam, shirt_number=numberPlayer, position=positionPlayer, injured=injured
        )

        return newSquadMember

    def generator_fixture_stats(self, team_fixture_stats_infos: dict[str:any]) -> fixtures_stats_model.FixturesStats:

        idFixture = team_fixture_stats_infos.get("id_fixture")
        idTeam = team_fixture_stats_infos.get("id_team")
        formation = team_fixture_stats_infos.get("formation")
        idCoach = team_fixture_stats_infos.get("coach")
        shotsOnGoal = team_fixture_stats_infos.get("shots_on_goal")
        shotsOffGoal = team_fixture_stats_infos.get("shots_off_goal")
        shotsBlocked = team_fixture_stats_infos.get("blocked_shots")
        shotsInsideBox = team_fixture_stats_infos.get("shots_insidebox")
        shotsOffsideBox = team_fixture_stats_infos.get("shots_outsidebox")
        fouls = team_fixture_stats_infos.get("fouls")
        cornerKicks = team_fixture_stats_infos.get("corner_kicks")
        offSides = team_fixture_stats_infos.get("offsides")
        ballPossession = team_fixture_stats_infos.get("ball_possession")
        yellowCards = team_fixture_stats_infos.get("yellow_cards")
        redCards = team_fixture_stats_infos.get("red_cards")
        goalKeeperSaves = team_fixture_stats_infos.get("goalkeeper_saves")
        totalPasses = team_fixture_stats_infos.get("total_passes")
        accuratePasses = team_fixture_stats_infos.get("passes_accurate")
        expectedGoals = team_fixture_stats_infos.get("expected_goals")

        newFixtureStat = fixtures_stats_model.FixturesStats(
            id_fixture=idFixture, id_team=idTeam, id_coach=idCoach, formation=formation,shots_on_goal=shotsOnGoal,
            shots_off_goal=shotsOffGoal, shots_blocked=shotsBlocked, shots_inside_box=shotsInsideBox, shots_offside_box=shotsOffsideBox,
            fouls=fouls, corners=cornerKicks, offsides=offSides, possession=ballPossession, yellow_cards=yellowCards, red_cards=redCards,
            goalkeeper_saves=goalKeeperSaves, total_passes=totalPasses, accurate_passes=accuratePasses, expected_goals=expectedGoals
        )

        return newFixtureStat


    def generator_fixture_event(self, fixture_events_infos: dict[str:any]) -> fixtures_events_model.FixturesEvents:
        idTeam = fixture_events_infos.get("id_team")
        idFixture = fixture_events_infos.get("id_fixture")
        timeElapsed = fixture_events_infos.get("time")
        idPrincipalPlayer = fixture_events_infos.get("id_player_principal")
        idPlayerAssist = fixture_events_infos.get("id_player_assist")
        typeEvent = fixture_events_infos.get("type")
        detailEvent = fixture_events_infos.get("detail")
        commentEvent = fixture_events_infos.get("comment")

        newFixtureEvents = fixtures_events_model.FixturesEvents(
            id_team=idTeam, id_fixture=idFixture, time=timeElapsed, id_player_principal=idPrincipalPlayer,
            id_player_assist=idPlayerAssist, type_event=typeEvent, detail=detailEvent, comments=commentEvent
        )

        return newFixtureEvents


    def generator_player_stat(self, player_stat_infos: dict[str:any]) -> players_stats_model.PlayersStats:
        idPlayer = player_stat_infos.get("id_player")
        idTeam = player_stat_infos.get("id_team")
        seasonLeague = player_stat_infos.get("season")
        idLeague = player_stat_infos.get("id_league")
        positionPlayer = player_stat_infos.get("position")
        isCaptain = player_stat_infos.get("captain")
        gamesAppearances = player_stat_infos.get("appearances")
        gamesLineUps = player_stat_infos.get("line_ups")
        gamesMinutes = player_stat_infos.get("minutes")
        ratingPlayer = player_stat_infos.get("rating")
        substitutesIn = player_stat_infos.get("substitutes_in")
        substitutesOut = player_stat_infos.get("substitutes_out")
        bench = player_stat_infos.get("bench")
        shotsTotal = player_stat_infos.get("shots_total")
        shotsOn = player_stat_infos.get("shots_on")
        goals = player_stat_infos.get("goals")
        goalsConceded = player_stat_infos.get("goals_conceded")
        goalsSaved = player_stat_infos.get("goals_saved")
        assists = player_stat_infos.get("assists")
        passesTotal = player_stat_infos.get("total_passes")
        passesKey = player_stat_infos.get("passes_key")
        passesAccuracy = player_stat_infos.get("accuracy_passes")
        tacklesTotal = player_stat_infos.get("tackles_total")
        blocks = player_stat_infos.get("blocks")
        interceptions = player_stat_infos.get("interceptions")
        duelsTotal = player_stat_infos.get("duels_total")
        duelsWin = player_stat_infos.get("duels_win")
        dribblesAttempted = player_stat_infos.get("dribbles_attempted")
        dribblesSuccess = player_stat_infos.get("dribbles_success")
        dribblesPast = player_stat_infos.get("dribbles_past")
        foulsDraw = player_stat_infos.get("fouls_draw")
        foulsCommitted = player_stat_infos.get("fouls_committed")
        cardsYellow = player_stat_infos.get("cards_yellow")
        cardsYellowRed = player_stat_infos.get("cards_yellowred")
        cardsRed = player_stat_infos.get("cards_red")
        penaltiesWon = player_stat_infos.get("penalties_won")
        penaltiesCommitted = player_stat_infos.get("penalties_committed")
        penaltiesScored = player_stat_infos.get("penalties_scored")
        penaltiesMissed = player_stat_infos.get("penalties_missed")
        penaltiesSaved = player_stat_infos.get("penalties_saved")

        newPlayerStat = players_stats_model.PlayersStats(
            id_player=idPlayer, id_league=idLeague, id_team=idTeam, position=positionPlayer, captain=isCaptain,
            appearances=gamesAppearances, lineups=gamesLineUps, minutes=gamesMinutes, rating=ratingPlayer,
            substitutes_in=substitutesIn, substitutes_out=substitutesOut, bench=bench, shots_total=shotsTotal,
            shots_on=shotsOn, goals=goals, assists=assists, conceded_goals=goalsConceded, saved_goals=goalsSaved,
            total_pass=passesTotal, key_pass=passesKey, accuracy_pass=passesAccuracy, tackles=tacklesTotal,
            blocks=blocks, interceptions=interceptions, total_duels=duelsTotal, win_duels=duelsWin,
            attempted_dribbles=dribblesAttempted, success_dribbles=dribblesSuccess, past_dribbles=dribblesPast,
            drawn_fouls=foulsDraw, committed_fouls=foulsCommitted, yellow_cards=cardsYellow, yellow_red_cards=cardsYellowRed,
            red_cards=cardsRed, won_penalties=penaltiesWon, committed_penalties=penaltiesCommitted, scored_penalties=penaltiesScored,
            missed_penalties=penaltiesMissed, saved_penalties=penaltiesSaved
        )

        return newPlayerStat

    def generator_team_league_fixtures_stats(self, team_league_fixtures_stats_infos:dict[str:any]) -> teams_fixtures_stats_model.TeamsFixturesStats:
        idTeam = team_league_fixtures_stats_infos.get("id_team")
        idLeague = team_league_fixtures_stats_infos.get("id_league")
        fixturesHome = team_league_fixtures_stats_infos.get("fixtures_home")
        fixturesAway = team_league_fixtures_stats_infos.get("fixtures_away")
        winsHome = team_league_fixtures_stats_infos.get("wins_home")
        winsAway = team_league_fixtures_stats_infos.get("wins_away")
        drawsHome = team_league_fixtures_stats_infos.get("draws_home")
        drawsAway = team_league_fixtures_stats_infos.get("draws_away")
        losesHome = team_league_fixtures_stats_infos.get("loses_home")
        losesAway = team_league_fixtures_stats_infos.get("loses_away")
        cleanSheetsHome = team_league_fixtures_stats_infos.get("clean_sheets_home")
        cleanSheetsAway = team_league_fixtures_stats_infos.get("clean_sheets_away")
        notScoredHome = team_league_fixtures_stats_infos.get("not_scored_home")
        notScoredAway = team_league_fixtures_stats_infos.get("not_scored_away")
        maxWinStreak = team_league_fixtures_stats_infos.get("max_wins_streak")
        maxDrawsStreak = team_league_fixtures_stats_infos.get("max_draws_streak")
        maxLosesStreak = team_league_fixtures_stats_infos.get("max_loses_streak")
        betterWinHome = team_league_fixtures_stats_infos.get("better_win_home")
        betterWinAway = team_league_fixtures_stats_infos.get("better_win_away")
        worstLoseHome = team_league_fixtures_stats_infos.get("worst_lose_home")
        worstLoseAway = team_league_fixtures_stats_infos.get("worst_lose_away")

        newTeamLeagueStat = teams_fixtures_stats_model.TeamsFixturesStats(
            id_team=idTeam, id_league=idLeague, fixtures_home=fixturesHome, fixtures_away=fixturesAway, wins_home=winsHome,
            wins_away=winsAway, draws_home=drawsHome, draws_away=drawsAway, loses_home=losesHome, loses_away=losesAway,
            clean_sheets_home=cleanSheetsHome, clean_sheets_away=cleanSheetsAway, not_scored_home=notScoredHome, not_scored_away=notScoredAway,
            max_wins_streak=maxWinStreak, max_draws_streak=maxDrawsStreak, max_loses_streak=maxLosesStreak, better_win_home=betterWinHome,
            worst_lose_home=worstLoseHome, better_win_away=betterWinAway, worst_lose_away=worstLoseAway
        )

        return newTeamLeagueStat


    def generator_team_league_goals_stats(self, team_league_goals_stats_infos:dict[str:any]) -> teams_goals_stats_model.TeamsGoalsStats:
        idTeam = team_league_goals_stats_infos.get("id_team")
        idLeague = team_league_goals_stats_infos.get("id_league")
        typeStat = team_league_goals_stats_infos.get("type")
        goalsHome = team_league_goals_stats_infos.get("goals_home")
        goalsAway = team_league_goals_stats_infos.get("goals_away")
        inMinute0_15 = team_league_goals_stats_infos.get("in_minute_0_15")
        inMinute16_30 = team_league_goals_stats_infos.get("in_minute_16_30")
        inMinute31_45 = team_league_goals_stats_infos.get("in_minute_31_45")
        inMinute46_60 = team_league_goals_stats_infos.get("in_minute_46_60")
        inMinute61_75 = team_league_goals_stats_infos.get("in_minute_61_75")
        inMinute76_90 = team_league_goals_stats_infos.get("in_minute_76_90")
        inMinute91_105 = team_league_goals_stats_infos.get("in_minute_91_105")
        inMinute106_120 = team_league_goals_stats_infos.get("in_minute_106_120")

        newTeamGoalStat = teams_goals_stats_model.TeamsGoalsStats(
            id_team=idTeam, id_league=idLeague, type=typeStat, goals_home=goalsHome, goals_away=goalsAway, in_minute_0_15=inMinute0_15, in_minute_16_30=inMinute16_30,
            in_minute_31_45=inMinute31_45, in_minute_46_60=inMinute46_60, in_minute_61_75=inMinute61_75, in_minute_76_90=inMinute76_90,
            in_minute_91_105=inMinute91_105, in_minute_106_120=inMinute106_120
        )

        return newTeamGoalStat

    def generator_team_league_cards_stats(self, team_league_cards_stats_infos: dict[str:any]) -> teams_cards_stats_model.TeamsCardsStats:
        idTeam = team_league_cards_stats_infos.get("id_team")
        idLeague = team_league_cards_stats_infos.get("id_league")
        cardType = team_league_cards_stats_infos.get("card_type")
        inMinute0_15 = team_league_cards_stats_infos.get("in_minute_0_15")
        inMinute16_30 = team_league_cards_stats_infos.get("in_minute_16_30")
        inMinute31_45 = team_league_cards_stats_infos.get("in_minute_31_45")
        inMinute46_60 = team_league_cards_stats_infos.get("in_minute_46_60")
        inMinute61_75 = team_league_cards_stats_infos.get("in_minute_61_75")
        inMinute76_90 = team_league_cards_stats_infos.get("in_minute_76_90")
        inMinute91_105 = team_league_cards_stats_infos.get("in_minute_91_105")
        inMinute106_120 = team_league_cards_stats_infos.get("in_minute_106_120")

        newCardStatTypeCard = teams_cards_stats_model.TeamsCardsStats(
            id_team=idTeam, id_league=idLeague, card_type=cardType, in_minute_0_15=inMinute0_15, in_minute_16_30=inMinute16_30,
            in_minute_31_45=inMinute31_45, in_minute_46_60=inMinute46_60, in_minute_61_75=inMinute61_75, in_minute_76_90=inMinute76_90,
            in_minute_91_105=inMinute91_105, in_minute_106_120=inMinute106_120
        )

        return newCardStatTypeCard

    def generator_fixture_lineup(self, fixture_lineup_infos:dict[str:any]) -> str:
        idTeam = fixture_lineup_infos.get("id_team")
        idFixture = fixture_lineup_infos.get("id_fixture")
        idPlayer = fixture_lineup_infos.get("id_player")
        typeLineUp = fixture_lineup_infos.get("type")
        positionPlayer = fixture_lineup_infos.get("position")
        gridPlayer = fixture_lineup_infos.get("grid")

        queryInsert = f"""
        insert into ftb.fixtures_lineups (id_fixture, id_team, id_player, "type", "position", grid)
        values (
        (select id from ftb.fixtures where id_fixture = {idFixture}),
        (select id from ftb.teams where id_team = {idTeam}),
        (select id from ftb.players where id_player = {idPlayer}),
        '{typeLineUp}',
        '{positionPlayer}',
        '{gridPlayer}'
        ) 
        """

        return queryInsert


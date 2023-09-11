from typing import NoReturn


class Queries:
    def __init__(self):
        self.get_all_team_id = "select id_team from football_data.teams"
        self.get_all_league_id = "select id_league from football_data.leagues"
        self.get_all_teams_id_serie_a = "select distinct(team.id_team) as id_team from football_data.fixtures fx inner join football_data.teams team on team.id = fx.id_team_home where fx.id_league = 1"
        self.get_all_fixtures_id = "select id_fixture from football_data.fixtures"
        self.get_all_id_players_serie_a = "select p.id_player from football_data.teams_squad ts inner join football_data.players p on p.id = ts.id where ts.id_team in (select distinct(team.id) as id_team from football_data.fixtures fx inner join football_data.teams team on team.id = fx.id_team_home where fx.id_league = 1)"

    def update_fixture_data_status(self, id_fixture: int) -> NoReturn:
        return f"update football_data.fixtures set data_status = 'collected' where id_fixture = {id_fixture}"

    def insert_stadium(self, stadium_values: dict[str:str]) -> str:

        idExStadium = stadium_values.get('id')
        nameStadium = stadium_values.get('name')
        stateStadium = stadium_values.get('state')
        cityStatium = stadium_values.get('city')
        addressStatium = stadium_values.get('address')
        capacityStatium = stadium_values.get('capacity')
        surfaceStadium = stadium_values.get('surface')
        imageStadium = stadium_values.get('image')

        queryInsert = f"""

        insert into "football_data".stadiums (id_stadium, "name", state, city, address, capacity, surface, image)
        values ({idExStadium}, '{nameStadium}', '{stateStadium}', '{cityStatium}', '{addressStatium}', {capacityStatium}, '{surfaceStadium}', '{imageStadium}')

        """

        return queryInsert

    def insert_team(self, team_values: dict[str:str]) -> str:

        idExTeam = team_values.get('id')
        idStadium = team_values.get('id_stadium')
        nameTeam = team_values.get('name')
        logoTeam = team_values.get('logo')
        nationalTeam = team_values.get('national')
        codeTeam = team_values.get('code')
        countryTeam = team_values.get('country')
        foundedTeam = team_values.get('founded')

        if idStadium is not None:
            queryInsert = f"""
            insert into football_data.teams (id_team, id_stadium, code, "name", country, logo, founded, "national") values
            ({idExTeam}, (select id from football_data.stadiums where id_stadium = {idStadium}), '{codeTeam}', '{nameTeam}', '{countryTeam}', '{logoTeam}', {foundedTeam}, {nationalTeam})       
            """
        else:
            queryInsert = f"""
                        insert into football_data.teams (id_team, code, "name", country, logo, founded, "national") values
                        ({idExTeam}, '{codeTeam}', '{nameTeam}', '{countryTeam}', '{logoTeam}', {foundedTeam}, {nationalTeam})       
                        """

        return queryInsert

    def insert_league(self, leagues_values: dict[str:any]) -> str:

        idLeague = leagues_values.get("id")
        nameLeague = leagues_values.get('name')
        startLeague = leagues_values.get('start')
        endLeague = leagues_values.get('end')
        logoLeague = leagues_values.get('logo')
        countryLeague = leagues_values.get('country')
        typeLeague = leagues_values.get('type')
        seasonLeague = leagues_values.get('season')

        queryInsert = f"""
        insert into football_data.leagues (id_league,"name",country,"type",season,start_league,end_league,logo)
        values ({idLeague},'{nameLeague}','{countryLeague}','{typeLeague}',{seasonLeague},'{startLeague}','{endLeague}','{logoLeague}')
        """

        return queryInsert

    def insert_player(self, player_values: dict[str:any]) -> str:

        idPlayer = player_values.get('id')
        namePlayer = player_values.get('name')
        firstNamePlayer = player_values.get('first_name')
        lastNamePlayer = player_values.get('last_name')
        birthPlayer = player_values.get('birth')
        nationalityPlayer = player_values.get('nationality')
        heightPlayer = player_values.get('height')
        weightPlayer = player_values.get('weight')
        photoPlayer = player_values.get('photo')

        queryInsert = f"""
        insert into football_data.players (id_player, "name", first_name, last_name, date_of_birth, nationality, height, weight,photo)
        values ({idPlayer},'{namePlayer}','{firstNamePlayer}','{lastNamePlayer}','{birthPlayer}','{nationalityPlayer}',{heightPlayer},{weightPlayer},'{photoPlayer}')
        """

        return queryInsert

    def insert_fixture(self, fixture_values: dict[str:any]) -> str:
        idFixture = fixture_values.get("id_fixture")
        dateFixture = fixture_values.get("date")
        refereeFixture = fixture_values.get("referee")
        idStadiumFixture = fixture_values.get("stadium")
        idHomeTeamFixture = fixture_values.get("home_team")
        idAwayTeamFixture = fixture_values.get("away_team")
        idLeague = fixture_values.get("id_league")
        roundFixture = fixture_values.get("round")
        seasonFixture = fixture_values.get("season")
        resultFixture = fixture_values.get("result")
        statusFixture = fixture_values.get("status")

        if idStadiumFixture != None:
            queryInsert = f"""
            insert into football_data.fixtures (id_fixture,id_stadium,id_league,id_team_home,id_team_away,start_at,result,round,referee,status) 
            values 
            ({idFixture},
            (select id from football_data.stadiums where id_stadium = {idStadiumFixture}),
            (select id from football_data.league where id_league = {idLeague} and season = {seasonFixture}),
            (select id from football_data.teams where id_team = {idHomeTeamFixture}),
            (select id from football_data.teams where id_team = {idAwayTeamFixture}),
            '{dateFixture}',
            '{resultFixture}',
            '{roundFixture}',
            '{refereeFixture}',
            '{statusFixture}'
            )
            """
        else:
            queryInsert = f"""
            insert into football_data.fixtures (id_fixture,id_league,id_team_home,id_team_away,start_at,result,round,referee,status) 
            values 
            ({idFixture},
            (select id from football_data.league where id_league = {idLeague} and season = {seasonFixture}),
            (select id from football_data.teams where id_team = {idHomeTeamFixture}),
            (select id from football_data.teams where id_team = {idAwayTeamFixture}),
            '{dateFixture}',
            '{resultFixture}',
            '{roundFixture}',
            '{refereeFixture}',
            '{statusFixture}'
            )
            """

        return queryInsert

    def insert_team_player_squad(self, player_squad_infos: dict[str:any]):
        idPlayer = player_squad_infos.get("id_player")
        idTeam = player_squad_infos.get("id_team")
        positionPlayer = player_squad_infos.get("position")
        numberPlayer = player_squad_infos.get("number")

        queryInsert = f"""
        insert into football_data.teams_squad (id_team, id_player, shirt_number, "position") 
        values
         (
         (select id from football_data.teams where id_team = {idTeam}),
         (select id from football_data.players where id_player = {idPlayer}),
         {numberPlayer},
         '{positionPlayer}'
         )
        """

        return queryInsert

    def insert_fixture_stats(self, team_fixture_stats_infos: dict[str:any]):

        idFixture = team_fixture_stats_infos.get("id_fixture")
        idTeam = team_fixture_stats_infos.get("id_team")
        shotsOnGoal = team_fixture_stats_infos.get("shots_on_goal")
        shotsOffGoal = team_fixture_stats_infos.get("shots_off_goal")
        shotsBlocked = team_fixture_stats_infos.get("blocked_shots")
        shotsInsideBox = team_fixture_stats_infos.get("shots_insidebox")
        shotsOutsideBox = team_fixture_stats_infos.get("shots_outsidebox")
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

        queryInsert = f"""
        insert into football_data.fixtures_stats (id_fixture, id_team, home, shots_on_goal, shots_off_goal, shots_blocked, shots_inside_box, shots_offside_box, fouls, corners, offsides, possession, yellow_cards, red_cards, goalkeeper_saves, total_passes, accurate_passes, expected_goals)
        values (
        (select id from football_data.fixtures where id_fixture = {idFixture}),
        (select id from football_data.teams where id_team = {idTeam}),
        (select case when id_team_home = (select id from football_data.teams where id_team = {idTeam}) then true else false end from football_data.fixtures where id_fixture = {idFixture}),
        {shotsOnGoal},
        {shotsOffGoal},
        {shotsBlocked},
        {shotsInsideBox},
        {shotsOutsideBox},
        {fouls},
        {cornerKicks},
        {offSides},
        {ballPossession},
        {yellowCards},
        {redCards},
        {goalKeeperSaves},
        {totalPasses},
        {accuratePasses},
        {expectedGoals}
        )
        """

        return queryInsert


    def insert_fixture_event(self, fixture_events_infos: dict[str:any]) -> str:
        idTeam = fixture_events_infos.get("id_team")
        idFixture = fixture_events_infos.get("id_fixture")
        timeElapsed = fixture_events_infos.get("time")
        idPrincipalPlayer = fixture_events_infos.get("id_player_principal")
        idPlayerAssist = fixture_events_infos.get("id_player_assist")
        typeEvent = fixture_events_infos.get("type")
        detailEvent = fixture_events_infos.get("detail")
        commentEvent = fixture_events_infos.get("comment")

        if idPlayerAssist is not None:
            queryInsert = f"""
            insert into football_data.fixtures_events (id_team, id_fixture, id_player_principal, id_player_assist, "time", type_event, "detail", "comments")
            values (
            (select id from football_data.teams where id_team = {idTeam}),
            (select id from football_data.fixtures where id_fixture = {idFixture}),
            (select id from football_data.players where id_player = {idPrincipalPlayer}),
            (select id from football_data.players where id_player = {idPlayerAssist}),
            {timeElapsed},
            '{typeEvent}',
            '{detailEvent}',
            '{commentEvent}'
            )
            """
        else:
            queryInsert = f"""
            insert into football_data.fixtures_events (id_team, id_fixture, id_player_principal, "time", type_event, "detail", "comments")
            values (
            (select id from football_data.teams where id_team = {idTeam}),
            (select id from football_data.fixtures where id_fixture = {idFixture}),
            (select id from football_data.players where id_player = {idPrincipalPlayer}),
            {timeElapsed},
            '{typeEvent}',
            '{detailEvent}',
            '{commentEvent}'
            )
            """
            if idPrincipalPlayer is None:
                queryInsert = f"""
                insert into football_data.fixtures_events (id_team, id_fixture, "time", type_event, "detail", "comments")
                values (
                (select id from football_data.teams where id_team = {idTeam}),
                (select id from football_data.fixtures where id_fixture = {idFixture}),
                {timeElapsed},
                '{typeEvent}',
                '{detailEvent}',
                '{commentEvent}'
                )
                """

        return queryInsert


    def insert_player_stat(self, player_stat_infos: dict[str:any]) -> str:
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

        queryInsert = f"""
        insert into football_data.players_stats (id_player, id_league, id_team, "position", captain, appearances, lineups, "minutes", rating, substitutes_in, 
        substitutes_out, bench, shots_total, shots_on, goals, assists, conceded_goals, saved_goals, total_pass, key_pass, accuracy_pass, tackles, blocks,
        interceptions, total_duels, win_duels, attempted_dribbles, success_dribbles, past_dribbles, drawn_fouls, committed_fouls, yellow_cards, yellow_red_cards,
        red_cards, won_penalties, committed_penalties, scored_penalties, missed_penalty, saved_penalty 
        ) values (
        (select id from football_data.players where id_player = {idPlayer}),
        (select id from football_data.leagues where id_league = {idLeague} and season = {seasonLeague}),
        (select id from football_data.teams where id_team = {idTeam}), 
        '{positionPlayer}', {isCaptain}, {gamesAppearances}, {gamesLineUps}, {gamesMinutes}, {ratingPlayer}, {substitutesIn}, {substitutesOut}, 
        {bench}, {shotsTotal}, {shotsOn}, {goals}, {assists}, {goalsConceded}, {goalsSaved}, {passesTotal}, {passesKey}, 
        {passesAccuracy}, {tacklesTotal}, {blocks}, {interceptions}, {duelsTotal}, {duelsWin}, {dribblesAttempted},
        {dribblesSuccess}, {dribblesPast}, {foulsDraw}, {foulsCommitted}, {cardsYellow}, {cardsYellowRed}, {cardsRed}, {penaltiesWon},
        {penaltiesCommitted}, {penaltiesScored}, {penaltiesMissed}, {penaltiesSaved}
        )
        """

        return queryInsert

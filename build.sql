create schema if not exists "ftb";
SET timezone = 'America/Sao_Paulo';

CREATE OR REPLACE FUNCTION update_teams_squad_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = current_timestamp;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_fixture_team(id_fixture integer, id_team integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_fixture || '-' || id_team;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_fixture_lineup(id_fixture integer, id_player integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_fixture || '-' || id_player;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_fixture_event(id_fixture integer, id_team integer,"time" integer, type_event text)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_fixture || '-' || id_team || '-' || "time" || '-' || type_event;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_team_player(id_team integer, id_player integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_team || '-' || id_player;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_player_stat(id_player integer, id_league integer, id_team integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_player || '-' || id_league || '-' || id_team;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_team_league(id_team integer, id_league integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_team || '-' || id_league;
END;
$$ LANGUAGE plpgsql;

create or replace function generate_compost_id_team_league_goal_type(id_team integer, id_league integer, "type" text)
returns varchar(20) immutable
as $$
BEGIN
    return id_team || '-' || id_league || '-' || "type";
end;
$$
language plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_team_league_card(id_team integer, id_league integer, card_type text)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_team || '-' || id_league || '-' || card_type;
END;
$$ LANGUAGE plpgsql;

create or replace function generate_compost_id_leagues(id_champ integer, season integer)
returns varchar(20) immutable
as $$
BEGIN
    return id_champ || '-' || season;
end;
$$
language plpgsql;


create table if not exists "ftb".stadiums
(
    id serial,
    id_stadium integer not null unique,
    "name" varchar(150) not null unique,
    state varchar(20) not null,
    city varchar(50) not null,
    address varchar(250) not null,
    capacity integer not null,
    surface varchar(30) not null,
    image varchar(250),

    constraint stadiums_pk primary key (id)
);

create table if not exists "ftb".teams
(
    id serial,
    id_team integer not null unique,
    id_stadium integer,
    code char(3),
    "name" varchar(100) not null unique,
    country varchar(15) not null,
    logo varchar(250),
    founded integer,
    "national" bool not null,

    constraint teams_pk primary key (id),
    constraint teams_stadium foreign key (id_stadium) references "ftb".stadiums (id)
);


create table if not exists "ftb".players
(
    id serial,
    id_player integer not null unique,
    "name" varchar(50) not null,
    first_name varchar(30) not null,
    last_name varchar(40) not null,
    date_of_birth date not null,
    nationality varchar(30),
    height int,
    weight int,
    photo varchar(250),

    constraint players_id primary key (id)
);


create table if not exists "ftb".teams_squad
(
    id serial,
    id_team integer not null,
    id_player integer not null unique,
    shirt_number integer not null,
    "position" varchar(30) not null,
    injured boolean default false not null,
    updated_at timestamp default current_timestamp not null,
    id_compost varchar(15) unique GENERATED ALWAYS as (generate_compost_id_team_player(id_team,id_player)) STORED,

    constraint teams_squad_pk primary key (id),
    constraint squad_team_fk foreign key (id_team) references "ftb".teams (id),
    constraint squad_player_fk foreign key (id_player) references "ftb".players (id)
);

CREATE OR REPLACE TRIGGER teams_squad_updated_at_trigger
BEFORE UPDATE ON "ftb".teams_squad
FOR EACH ROW
EXECUTE FUNCTION update_teams_squad_updated_at();

create table if not exists "ftb".leagues
(
    id serial,
    id_league integer not null,
    "name" varchar(50) not null,
    country varchar(15) not null,
    "type" varchar(7) not null,
    season integer not null,
    start_league date not null,
    end_league date not null,
    logo varchar(250),
    id_compost varchar(20) unique generated always as (generate_compost_id_leagues(id_league, season)) stored,

    constraint champs_pk primary key (id)
);

create table if not exists "ftb".fixtures
(
    id serial,
    id_fixture integer not null unique,
    id_stadium integer,
    id_league integer not null,
    id_team_home integer not null,
    id_team_away integer not null,
    start_at timestamp not null,
    result varchar(11) not null,
    round varchar(30) not null,
    referee varchar(50),
    status varchar(20),
    data_status varchar(10) default 'waiting',

    constraint fixtures_pk primary key (id),
    constraint fixtures_league_fk foreign key (id_league) references "ftb".leagues (id),
    constraint fixtures_team_home_fk foreign key (id_team_home) references "ftb".teams (id),
    constraint fixtures_team_away_fk foreign key (id_team_away) references "ftb".teams (id),
    constraint fixtures_stadium_fk foreign key (id_stadium) references "ftb".stadiums (id)
);

create table if not exists "ftb".fixtures_stats
(
    id serial,
    id_fixture integer not null,
    id_team integer not null,
    home bool not null,
    id_coach integer not null,
    formation varchar(10) not null,
    shots_on_goal integer not null,
    shots_off_goal integer not null,
    shots_blocked integer not null,
    shots_inside_box integer not null,
    shots_offside_box integer not null,
    fouls integer not null,
    corners integer not null,
    offsides integer not null,
    possession integer not null,
    yellow_cards integer not null,
    red_cards integer not null,
    goalkeeper_saves integer not null,
    total_passes integer not null,
    accurate_passes integer not null,
    expected_goals numeric not null,
    id_compost varchar(15) generated always as (generate_compost_id_fixture_team(id_fixture,id_team)) stored,

    constraint fixtures_statistics_pk primary key (id),
    constraint fixtures_statistics_fixture_fk foreign key (id_fixture) references ftb.fixtures (id),
    constraint fixtures_statistics_team_fk foreign key (id_team) references ftb.teams (id)
);

create table if not exists "ftb".fixtures_events
(
    id serial,
    id_team integer not null,
    id_fixture integer not null,
    id_player_principal integer,
    id_player_assist integer,
    "time" integer not null,
    type_event varchar(20) not null,
    "detail" varchar(30) not null,
    "comments" varchar(50) not null,
    id_compost varchar(50) not null unique generated always as (generate_compost_id_fixture_event(id_fixture, id_team, "time", type_event)) stored,

    constraint fixtures_events_pk primary key (id),
    constraint fixtures_events_player_principal foreign key (id_player_principal) references "ftb".players (id),
    constraint fixtures_events_player_assist foreign key (id_player_assist) references "ftb".players (id),
    constraint fixtures_events_team foreign key (id_team) references "ftb".teams (id),
    constraint fixtures_events_fk foreign key (id_fixture) references "ftb".fixtures (id)
);

create table if not exists "ftb".players_stats
(
  id serial,
  id_player integer not null,
  id_league integer not null,
  id_team integer not null,
  "position" varchar(30) not null,
  captain boolean default false not null,
  appearances integer not null,
  lineups integer not null,
  "minutes" integer not null,
  rating numeric not null,
  substitutes_in integer not null,
  substitutes_out integer not null,
  bench integer not null,
  shots_total integer not null,
  shots_on integer not null,
  goals integer not null,
  assists integer not null,
  conceded_goals integer not null,
  saved_goals integer not null,
  total_pass integer not null,
  key_pass integer not null,
  accuracy_pass integer not null,
  tackles integer not null,
  blocks integer not null,
  interceptions integer not null,
  total_duels integer not null,
  win_duels integer not null,
  attempted_dribbles integer not null,
  success_dribbles integer not null,
  past_dribbles integer not null,
  drawn_fouls integer not null,
  committed_fouls integer not null,
  yellow_cards integer not null,
  yellow_red_cards integer not null,
  red_cards integer not null,
  won_penalties integer not null,
  committed_penalties integer not null,
  scored_penalties integer not null,
  missed_penalty integer not null,
  saved_penalty integer not null,
  id_compost varchar(20) unique generated always as (generate_compost_id_player_stat(id_player,id_league,id_team)) stored,

  constraint players_stats_pk primary key (id),
  constraint players_fk foreign key (id_player) references "ftb".players (id),
  constraint players_leagues_fk foreign key (id_league) references "ftb".leagues (id),
  constraint players_teams_fk foreign key (id_team) references "ftb".teams (id)
);


create table if not exists "ftb".teams_fixtures_stats
(
    id serial,
    id_team integer not null,
    id_league integer not null,
    fixtures_home integer not null,
    fixtures_away integer not null,
    wins_home integer not null,
    wins_away integer not null,
    draws_home integer not null,
    draws_away integer not null,
    loses_home integer not null,
    loses_away integer not null,
    clean_sheets_home integer not null,
    clean_sheets_away integer not null,
    not_scored_home integer not null,
    not_scored_away integer not null,
    max_wins_streak integer not null,
    max_draws_streak integer not null,
    max_loses_streak integer not null,
    better_win_home varchar(5) not null,
    worst_lose_home varchar(5) not null,
    better_win_away varchar(5) not null,
    worst_lose_away varchar(5) not null,
    id_compost varchar(20) unique
        GENERATED ALWAYS AS (generate_compost_id_team_league(id_team, id_league)) STORED,

    constraint teams_fixtures_stats_pk primary key (id),
    constraint teams_fixtures_stats_team_fk foreign key (id_team) references "ftb".teams (id),
    constraint teams_fixtures_stats_league_fk foreign key (id_league) references "ftb".leagues (id)
);

create table if not exists "ftb".teams_goals_stats
(
    id serial,
    id_team integer not null,
    id_league integer not null,
    "type" varchar(7) not null,
    goals_home integer not null,
    goals_away integer not null,
    in_minute_0_15 integer not null,
    in_minute_16_30 integer not null,
    in_minute_31_45 integer not null,
    in_minute_46_60 integer not null,
    in_minute_61_75 integer not null,
    in_minute_76_90 integer not null,
    in_minute_91_105 integer not null,
    in_minute_106_120 integer not null,
    id_compost varchar(30) unique
        GENERATED ALWAYS AS (generate_compost_id_team_league_goal_type(id_team, id_league, "type")) STORED,

    constraint teams_goals_stats_pk primary key (id),
    constraint teams_goals_stats_team_fk foreign key (id_team) references "ftb".teams,
    constraint teams_goals_stats_league_fk foreign key (id_league) references "ftb".leagues
);

create table if not exists "ftb".teams_cards_stats
(
    id serial,
    id_team integer not null,
    id_league integer not null,
    card_type varchar(6) not null,
    in_minute_0_15 integer not null,
    in_minute_16_30 integer not null,
    in_minute_31_45 integer not null,
    in_minute_46_60 integer not null,
    in_minute_61_75 integer not null,
    in_minute_76_90 integer not null,
    in_minute_91_105 integer not null,
    in_minute_106_120 integer not null,
    id_compost varchar(20) unique
        GENERATED ALWAYS as (generate_compost_id_team_league_card(id_team,id_league, card_type)) STORED,

    constraint teams_cards_stats_pk primary key (id),
    constraint teams_cards_stats_team_fk foreign key (id_team) references "ftb".teams (id),
    constraint teams_cards_stats_league_fk foreign key (id_league) references "ftb".leagues (id)
);

create table if not exists "ftb".fixtures_lineups
(
    id serial,
    id_fixture integer not null,
    id_team integer not null,
    id_player integer not null,
    "type" char(5) not null,
    "position" char(1) not null,
    grid char(3) not null,
    id_compost varchar(10) unique
        generated always as (generate_compost_id_fixture_lineup(id_fixture, id_player)) stored,

    constraint fixtures_lineups_pk primary key (id),
    constraint fixtures_lineups_fixture_fk foreign key (id_fixture) references "ftb".fixtures (id),
    constraint fixtures_lineups_team_fk foreign key (id_team) references "ftb".teams (id),
    constraint fixtures_lineups_player_fk foreign key (id_player) references "ftb".players (id)
)
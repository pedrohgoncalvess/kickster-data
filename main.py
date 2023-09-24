from api_requests import leagues
from api_requests import stadiums
from api_requests import teams
from api_requests import players
from api_requests import fixtures
from api_requests import fixtures_stats
from api_requests import fixtures_events
from api_requests import fixtures_lineups
from api_requests import teams_squad
from api_requests import players_stats
from api_requests import teams_cards_stats
from api_requests import teams_goals_stats
from api_requests import teams_fixtures_stats
from datetime import datetime
from datetime import timedelta


if __name__ == "__main__":
    startedAt = datetime.now()
    print(f"Starting process... Time: {startedAt}")
    leagues.main()
    stadiums.main()
    teams.main()
    print("Starting players table....")
    players.main()
    teams_squad.main()
    players_stats.main()
    print("Starting fixtures tables....")
    fixtures.main()
    fixtures_stats.main()
    fixtures_events.main()
    fixtures_lineups.main()
    print("Starting teams stats....")
    teams_cards_stats.main()
    teams_goals_stats.main()
    teams_fixtures_stats.main()
    finishedAt = datetime.now()
    print(f"Finishing process... Time: {finishedAt}")
    print(f"Time elapsed: {timedelta(hours=finishedAt.hour, seconds=finishedAt.second, minutes=finishedAt.minute) - timedelta(seconds=startedAt.second, hours=finishedAt.hour, minutes=startedAt.minute)}")

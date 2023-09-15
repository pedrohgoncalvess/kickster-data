from api_requests import leagues
from api_requests import teams_and_stadiums
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
    leagues.main()
    teams_and_stadiums.main()
    print("Starting players table....")
    players.main()
    print("Starting fixtures tables....")
    fixtures.main()
    fixtures_stats.main()
    fixtures_events.main()
    fixtures_lineups.main()
    teams_squad.main()
    players_stats.main()
    print("Starting teams stats....")
    teams_cards_stats.main()
    teams_goals_stats.main()
    teams_fixtures_stats.main()
    finishedAt = datetime.now()
    print(f"Time elapsed: {timedelta(seconds=finishedAt.second, minutes=finishedAt.minute) - timedelta(seconds=startedAt.second, minutes=startedAt.minute)}")

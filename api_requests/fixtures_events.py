from handlers.managers import Managers
from api_requests.address_request import Request
from database.data_from_db import DataFromDatabase


req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()

if __name__ == "__main__":
    listFixtures = dataFromDb.get_all_fixtures_id()

    for fixtureId in listFixtures:
        jsonEvents = req.fixture_events(fixtureId)
        manager.fixture_event_management(jsonEvents, fixtureId)
from handlers.managers import Managers
from api_requests.address_request import Request
from database.operations import Operations


def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()

    listFixtures = dataFromDb.get_all_fixtures_id()

    for fixtureId in listFixtures:
        jsonEvents = req.fixture_events(fixtureId)
        manager.fixture_event_management(jsonEvents, fixtureId)

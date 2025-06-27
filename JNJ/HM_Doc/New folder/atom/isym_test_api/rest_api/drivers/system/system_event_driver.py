from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.system.event_map_response import EventMap
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class SystemEventDriver(object):

    def __init__(self, auth_rest_api_driver: RestAPIDriver, base_url):
        self.events_url = urljoin(base_url, "api/system/data/events")
        self.subscriptions_events_url = urljoin(base_url, "api/system/subscriptions/events")
        self._request = auth_rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def get_events(self) -> RestResponse[EventMap]:
        return self._request.get_request(self.events_url, EventMap)

    def set_events_subscriptions(self, payload: EventMap) -> RestResponse[EventMap]:
        return self._request.post_request(self.subscriptions_events_url, payload,  response_type=EventMap)

    def get_events_subscriptions(self) -> RestResponse[EventMap]:
        return self._request.get_request(self.subscriptions_events_url, response_type=EventMap)

    def delete_events_subscriptions(self, payload: EventMap) -> RestResponse[EventMap]:
        return self._request.delete_request(self.subscriptions_events_url, payload)

from typing import Dict

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.system.session_models import SessionCredentials, Session
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger
from utilities.requests_helper import urljoin


class SessionDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.session_url = urljoin(base_url, "api/system/auth/sessions")
        self.subscriptions_events_url = urljoin(base_url, "api/system/subscriptions/events")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def create_session(self, payload: SessionCredentials) -> RestResponse[Session]:
        received_data = self._request.post_request(self.session_url, payload, response_type=Session)
        self.logger.debug(f"Set sessions response: \n{received_data}")
        return received_data

    def delete_session(self, payload: Session) -> RestResponse[Dict]:
        return self._request.delete_request(self.session_url, payload=payload)

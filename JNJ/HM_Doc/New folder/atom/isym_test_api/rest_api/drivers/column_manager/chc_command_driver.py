from urllib.parse import urljoin

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class ChcCommandDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.scan_column_tag_url = urljoin(base_url, "api/separation/cm/command/scancolumntag")
        self.scan_column_tag_status_url = urljoin(base_url, "api/separation/cm/command/scancolumntag/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def start_scan_column_tag(self):
        self.logger.debug("Post Request: Scan Column Tag")
        self._request.post_request(self.scan_column_tag_url)

    def get_scan_column_tag_status(self) -> BehaviorStatus:
        self.logger.debug("Post Request: Read Scan Column Tag")
        return self._request.get_request(self.scan_column_tag_status_url, BehaviorStatus).data

    def is_scan_column_tag_status_complete(self) -> bool:
        return self.get_scan_column_tag_status().state == BehaviorState.BehaviorState_COMPLETE

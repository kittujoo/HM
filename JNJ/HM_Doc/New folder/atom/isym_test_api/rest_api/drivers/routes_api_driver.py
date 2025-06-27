from urllib.parse import urljoin

from isym_test_api.rest_api.api.rest_endpoints_response import RestEndpointsResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class RoutesApiDriver(object):
    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.routes_api_url = urljoin(base_url, "api/routes")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def get_endpoint_routes(self):
        return self._request.get_request(self.routes_api_url, RestEndpointsResponse).data

import os.path
from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.system.ambient_temperature_response import AmbientTemperatureResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class AmbientTemperatureDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.ambient_temperature_url = urljoin(base_url, "api/system/ambienttemperature")
        self._request = rest_api_driver

        self.logger = Logger(self.__class__.__name__)

    def get_ambient_temperature(self) -> RestResponse[AmbientTemperatureResponse]:
        return self._request.get_request(self.ambient_temperature_url, AmbientTemperatureResponse)

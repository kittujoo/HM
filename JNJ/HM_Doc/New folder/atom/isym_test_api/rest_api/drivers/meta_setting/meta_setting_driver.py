from isym_test_api.rest_api.api.meta_setting.meta_setting_request import ValidateSampleSetRequest, MetaSettingRequest
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger
from utilities.requests_helper import urljoin


class MetaSettingDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.meta_setting_url = urljoin(base_url, "api/system/store/setting")
        self.meta_validation_url = urljoin(base_url, "api/datasystem/acquisition/validatesamplesetonsubmit")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_meta_checks(self, payload: MetaSettingRequest):
        self.logger.debug(f"Put Request Method dataset: \n{payload}")
        self._request.put_request(self.meta_setting_url, payload)

    def set_validate_sample_set_on_submit(self, payload: ValidateSampleSetRequest):
        self.logger.debug(f"Put Request Method dataset: \n{payload}")
        return self._request.put_request(self.meta_validation_url, payload)

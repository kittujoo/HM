from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.api.behavior.system_meta_tuv_wavelength_calibration_request import SystemMetaTuvWavelengthCalibration
from isym_test_api.rest_api.api.detection.autozero_offsets_response import TuvAutoZeroOffsets
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class TuvCommandDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.auto_zero_url = urljoin(base_url, "api/detection/tuv/command/autozero")
        self.auto_zero_status_url = urljoin(base_url, "api/detection/tuv/command/autozero/status")
        self.auto_zero_offsets_url = urljoin(base_url, "api/detection/tuv/configuration/autozerooffsets")
        self.calibrate_wavelength_url = urljoin(base_url, "api/detection/tuv/behavior/calibratewavelength")
        self.calibrate_wavelength_status_url = urljoin(base_url, "api/detection/tuv/behavior/calibratewavelength/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_auto_zero(self):
        self.logger.debug("Post Request: AutoZero")
        self._request.post_request(self.auto_zero_url)

    def get_auto_zero_status(self) -> BehaviorStatus:
        self.logger.debug("Get Request: Read AutoZero Status")
        return self._request.get_request(self.auto_zero_status_url, BehaviorStatus).data

    def get_auto_zero_offsets_value(self) -> TuvAutoZeroOffsets:
        self.logger.debug("Get Request: Read AutoZero Offsets Status")
        return self._request.get_request(self.auto_zero_offsets_url, TuvAutoZeroOffsets).data

    def is_auto_zero_status_complete(self) -> bool:
        return self.get_auto_zero_status().state == BehaviorState.BehaviorState_COMPLETE

    def calibrate_wavelength(self, payload: SystemMetaTuvWavelengthCalibration) -> RestResponse[None]:
        self.logger.debug("Put Request: Calibrate Wavelength")
        return self._request.put_request(self.calibrate_wavelength_url, payload)

    def get_calibrate_wavelength_status(self) -> RestResponse[BehaviorStatus]:
        received_data = self._request.get_request(self.calibrate_wavelength_status_url, response_type=BehaviorStatus)
        self.logger.debug(f"Get Request: Calibrate Wavelength Status: \n{received_data}")
        return received_data

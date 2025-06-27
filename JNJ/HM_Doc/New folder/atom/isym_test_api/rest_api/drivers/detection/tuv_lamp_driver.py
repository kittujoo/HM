"""
    Driver to create TUV Lamp API requests
"""
from urllib.parse import urljoin

from isym_test_api.rest_api.api.detection.tuv_lamp_response import LampStatusResponse
from isym_test_api.rest_api.api.detection.tuv_lamp_request import LampRequest
from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.api.detection.lamp_history_response import TuvLampHistory
from isym_test_api.rest_api.api.detection.lamp_hours_response import UsageCounter
from isym_test_api.rest_api.api.detection.lamp_intensity_response import TuvLampIntensityTestResult
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class TuvLampDriver(object):
    """
    Defines Tuv Lamp API driver, inheriting from RestAPIDriver
    """

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.tuv_lamp_history_url = urljoin(base_url, "api/detection/tuv/lamphistory")
        self.tuv_lamp_intensity_url = urljoin(base_url, "api/detection/tuv/lampintensity")
        self.tuv_lamp_hours_url = urljoin(base_url, "api/detection/tuv/usagecounter/lamphours")
        self.tuv_lamp_replace_lamp_url = urljoin(base_url, "api/detection/tuv/behavior/replacelamp")
        self.tuv_lamp_replace_lamp_status_url = urljoin(base_url, "api/detection/tuv/behavior/replacelamp/status")
        self.tuv_lamp_replace_lamp_completed_url = urljoin(base_url, "api/detection/tuv/behavior/replacelampcompleted")
        self.tuv_lamp_replace_lamp_completed_status_url = urljoin(base_url, "api/detection/tuv/behavior/replacelampcompleted/status")
        self.tuv_lamp_url = urljoin(base_url, "api/detection/tuv/lamp")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_tuv_lamp_status(self, payload: LampRequest) -> RestResponse[None]:
        return self._request.put_request(self.tuv_lamp_url, payload)

    def get_lamp_history(self) -> RestResponse[TuvLampHistory]:
        return self._request.get_request(self.tuv_lamp_history_url, TuvLampHistory)

    def get_tuv_lamp_status(self) -> RestResponse[LampStatusResponse]:
        return self._request.get_request(self.tuv_lamp_url, LampStatusResponse)

    def get_lamp_intensity(self) -> RestResponse[TuvLampIntensityTestResult]:
        return self._request.get_request(self.tuv_lamp_intensity_url, TuvLampIntensityTestResult)

    def get_lamp_hours(self) -> RestResponse[UsageCounter]:
        return self._request.get_request(self.tuv_lamp_hours_url, UsageCounter)

    def get_replace_lamp_status(self) -> RestResponse[BehaviorStatus]:
        return self._request.get_request(self.tuv_lamp_replace_lamp_status_url, BehaviorStatus)

    def is_replace_lamp_status_started(self) -> bool:
        return self.get_replace_lamp_status().data.state == BehaviorState.BehaviorState_ACTIVE

    def is_replace_lamp_status_complete(self) -> bool:
        return self.get_replace_lamp_status().data.state == BehaviorState.BehaviorState_INACTIVE

    def get_replace_lamp_completed_status(self) -> RestResponse[BehaviorStatus]:
        return self._request.get_request(self.tuv_lamp_replace_lamp_completed_status_url, BehaviorStatus)

    def is_replace_lamp_completed_status_started(self) -> bool:
        return self.get_replace_lamp_completed_status().data.state == BehaviorState.BehaviorState_ACTIVE

    def is_replace_lamp_completed_status_completed(self) -> bool:
        return self.get_replace_lamp_completed_status().data.state == BehaviorState.BehaviorState_INACTIVE

    def set_replace_lamp(self) -> RestResponse[None]:
        return self._request.put_request(self.tuv_lamp_replace_lamp_url)

    def set_replace_lamp_completed(self) -> RestResponse[None]:
        return self._request.put_request(self.tuv_lamp_replace_lamp_completed_url)

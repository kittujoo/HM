"""
    Filename: qsm_flow_driver.py
    Driver to create QSM flow API requests
"""
from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.api.solvent_management.flow_control_request import SolvFlowControlW
from isym_test_api.rest_api.api.solvent_management.flow_control_response import SolvFlowControlR
from isym_test_api.rest_api.api.solvent_management.flow_request import SolvFlowRateAndCompositionW
from isym_test_api.rest_api.api.solvent_management.flow_response import SolvFlowRateAndCompositionR
from isym_test_api.rest_api.api.solvent_management.full_flow_control_request import SolvFullFlowControlW
from isym_test_api.rest_api.api.solvent_management.full_flow_control_response import SolvFullFlowControlR
from isym_test_api.rest_api.api.solvent_management.leak_sensor_request import LeakSensorConfig
from isym_test_api.rest_api.api.solvent_management.leak_sensor_response import LeakSensorResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class QSMFlowDriver(object):
    """
    Defines QSM Flow API driver, inheriting from RestAPIDriver
    """

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.flow_control_url = urljoin(base_url, "/api/solventmanagement/qsm/flowcontrol")
        self.full_flow_control_url = urljoin(base_url, "/api/solventmanagement/qsm/fullflowcontrol")
        self.full_flow_control_status_url = urljoin(base_url, "/api/solventmanagement/qsm/fullflowcontrol/status")
        self.qsm_leak_sensor_url = urljoin(base_url, "/api/solventmanagement/qsm/leaksensor/configuration")
        self.flow_url = urljoin(base_url, "/api/solventmanagement/qsm/flow")
        self.qsm_leak_sensor_status_url = urljoin(base_url, "/api/solventmanagement/qsm/leaksensor/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_flow_control(self, state: bool) -> RestResponse[None]:
        """
        Method to set flow control on or off
        :param state: True = on | False = off
        """
        set_flow_request = SolvFlowControlW(state)
        return self._request.put_request(self.flow_control_url, set_flow_request)

    def get_flow_control(self) -> RestResponse[SolvFlowControlR]:
        """
        Method to get flow control request
        :return: Flow control request
        """
        received_data = self._request.get_request(self.flow_control_url, SolvFlowControlR)
        self.logger.debug(f"Get flow control response: {received_data}")
        return received_data

    def get_flow_control_status(self) -> bool:
        """
        Method to get flow control status
        :return: Flow control status (True or False)
        """
        return self.get_flow_control().data.flowOn

    def set_full_flow_control(self, payload: SolvFullFlowControlW) -> RestResponse[None]:
        self.logger.debug(f"Post Request Full Flow Control dataset: \n{payload}")
        return self._request.put_request(self.full_flow_control_url, payload)

    def get_full_flow_control(self) -> RestResponse[SolvFullFlowControlR]:
        received_data = self._request.get_request(self.full_flow_control_url, SolvFullFlowControlR)
        self.logger.debug(f"Get full flow control response: {received_data}")
        return received_data

    def get_full_flow_control_status(self) -> RestResponse[BehaviorStatus]:
        received_data = self._request.get_request(self.full_flow_control_status_url, BehaviorStatus)
        self.logger.debug(f"Get flow control status response: {received_data}")
        return received_data

    def is_full_flow_control_started(self) -> bool:
        return self.get_full_flow_control_status().data.state == BehaviorState.BehaviorState_ACTIVE

    def is_full_flow_control_complete(self) -> bool:
        return self.get_full_flow_control_status().data.state == BehaviorState.BehaviorState_INACTIVE

    def set_qsm_leak_sensor_configuration(self, payload: LeakSensorConfig) -> RestResponse[None]:
        self.logger.debug(f"Put Request Method dataset: \n{payload}")
        return self._request.put_request(self.qsm_leak_sensor_url, payload)

    def start_flow(self, payload: SolvFlowRateAndCompositionW) -> RestResponse[None]:
        self.logger.debug(f"Start flow test with payload: \n{payload}")
        return self._request.put_request(self.flow_url, payload)

    def get_qsm_leak_sensor_configuration(self) -> LeakSensorResponse:
        return self._request.get_request(self.qsm_leak_sensor_status_url, LeakSensorResponse).data

    def get_flow_status(self) -> SolvFlowRateAndCompositionR:
        return self._request.get_request(self.flow_url, SolvFlowRateAndCompositionR).data

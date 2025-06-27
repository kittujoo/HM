"""
    Filename: qsm_vent_valve_driver.py
    Driver to create QSM vent valve API requests
"""
from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.api.solvent_management.vent_valve_request import QsmMetaVentValve
from isym_test_api.rest_api.api.solvent_management.vent_valve_response import QsmVentValveR
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class QsmVentValveDriver(object):
    """
    Defines QSM Vent Valve API driver, inheriting from RestAPIDriver
    """

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.vent_valve_url = urljoin(base_url, "api/solventmanagement/qsm/ventvalve")
        self.vent_valve_status_url = urljoin(base_url, "api/solventmanagement/qsm/ventvalve/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_vent_valve(self, payload: QsmMetaVentValve) -> RestResponse[None]:
        self.logger.debug(f"Vent Valve payload: \n{payload}")
        return self._request.put_request(self.vent_valve_url, payload)

    def get_vent_valve(self) -> RestResponse[QsmVentValveR]:
        received_data = self._request.get_request(self.vent_valve_url, QsmVentValveR)
        self.logger.debug(f"Vent Valve response: \n{received_data}")
        return received_data

    def get_vent_valve_status(self) -> RestResponse[BehaviorStatus]:
        received_data = self._request.get_request(self.vent_valve_status_url, BehaviorStatus)
        self.logger.debug(f"Vent Valve status response: \n{received_data}")
        return received_data

    def is_vent_valve_complete(self) -> bool:
        return self.get_vent_valve_status().data.state == BehaviorState.BehaviorState_INACTIVE

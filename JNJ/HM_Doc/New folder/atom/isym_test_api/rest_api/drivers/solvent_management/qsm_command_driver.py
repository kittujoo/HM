from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.api.solvent_management.delta_pressure_limit_request import QsmDeltaPressureLimit
from isym_test_api.rest_api.api.solvent_management.delta_pressure_response import QsmDeltaPressure
from isym_test_api.rest_api.api.solvent_management.prime_pump_request import QsmMetaPrimePump
from isym_test_api.rest_api.api.system.initiate_behavior_request import InitiateBehaviorRequest
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class QsmCommandDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.delta_pressure_url = urljoin(base_url, "api/solventmanagement/qsm/deltapressure")
        self.delta_pressure_limit_url = urljoin(base_url, "api/solventmanagement/qsm/deltapressurelimit")
        self.single_prime_line_url = urljoin(base_url, "api/solventmanagement/qsm/behavior/routine/primeline")
        self.single_prime_line_status_url = urljoin(base_url, "api/solventmanagement/qsm/behavior/routine/primeline/status")
        self.prime_pump_initiate_url = urljoin(base_url, "api/solventmanagement/qsm/behavior/routine/primepump/initiate")
        self.prime_pump_url = urljoin(base_url, "api/solventmanagement/qsm/behavior/routine/primepump")
        self.prime_pump_status_url = urljoin(base_url, "api/solventmanagement/qsm/behavior/routine/primepump/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def initiate_prime_pump(self, payload: InitiateBehaviorRequest):
        self.logger.debug(f"Initiate Prime Pump payload: \n{payload}")
        self._request.post_request(self.prime_pump_initiate_url, payload)

    def start_prime_pump(self, payload: QsmMetaPrimePump):
        self.logger.debug(f"Start Prime Pump payload: \n{payload}")
        self._request.put_request(self.prime_pump_url, payload)

    def get_prime_pump_test_status(self) -> BehaviorStatus:
        received_data = self._request.get_request(self.prime_pump_status_url, BehaviorStatus).data
        self.logger.debug(f"Get prime fluidics status response: \n{received_data}")
        return received_data

    def is_prime_pump_test_started(self) -> bool:
        return self.get_prime_pump_test_status().state == BehaviorState.BehaviorState_ACTIVE

    def is_prime_pump_test_complete(self) -> bool:
        return self.get_prime_pump_test_status().state == BehaviorState.BehaviorState_INACTIVE

    def set_delta_pressure_limit(self, payload: QsmDeltaPressureLimit) -> RestResponse[None]:
        self.logger.debug(f"Delta Pressure Limit payload: \n{payload}")
        return self._request.put_request(self.delta_pressure_limit_url, payload)

    def get_delta_pressure_limit(self) -> RestResponse[QsmDeltaPressureLimit]:
        received_data = self._request.get_request(self.delta_pressure_limit_url, QsmDeltaPressureLimit)
        self.logger.debug(f"Delta Pressure Limit response: \n{received_data}")
        return received_data

    def get_delta_pressure(self) -> RestResponse[QsmDeltaPressure]:
        received_data = self._request.get_request(self.delta_pressure_url, QsmDeltaPressure)
        self.logger.debug(f"Get delta pressure response: \n{received_data}")
        return received_data

    def set_single_prime_line(self, payload: QsmMetaPrimePump) -> RestResponse[None]:
        self.logger.debug(f"Set Single Prime Line payload: \n{payload}")
        return self._request.put_request(self.single_prime_line_url, payload)

    def get_single_prime_line_status(self) -> RestResponse[BehaviorStatus]:
        received_data = self._request.get_request(self.single_prime_line_status_url, BehaviorStatus)
        self.logger.debug(f"Get prime fluidics status response: \n{received_data}")
        return received_data

    def is_single_prime_line_complete(self) -> bool:
        return self.get_single_prime_line_status().data.state == BehaviorState.BehaviorState_COMPLETE

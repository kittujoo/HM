from urllib.parse import urljoin

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus
from isym_test_api.rest_api.api.system.system_reset_request import SystemResetRequest
from isym_test_api.rest_api.api.system.workflow_request import SystemMetaBeginWorkflowRequest
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from isym_test_api.rest_api.api.base_response import RestResponse
from utilities.logger import Logger


class SystemCommandDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.system_reset_url = urljoin(base_url, "api/system/command/reset")
        self.system_stop_url = urljoin(base_url, "api/system/command/stop")
        self.system_initialize_url = urljoin(base_url, "api/system/command/initialize")
        self.system_initialize_status_url = urljoin(base_url, "api/system/command/initialize/status")
        self.emergency_stop_url = urljoin(base_url, 'api/system/command/emergencystop')
        self.system_workflow_url = urljoin(base_url, "api/system/workflow")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def system_reset(self):
        self.logger.debug("Post Request: System Reset")
        self._request.post_request(self.system_reset_url)

    def system_reset_request(self, payload: SystemResetRequest):
        self.logger.debug("Post Request: System Reset request")
        self._request.post_request(self.system_reset_url, payload)

    def system_stop(self):
        self.logger.debug("Post Request: System Stop")
        self._request.post_request(self.system_stop_url)

    def system_initialize(self):
        self.logger.debug("Post Request: System Initialize")
        self._request.post_request(self.system_initialize_url)

    def get_system_initialize_status(self) -> BehaviorStatus:
        received_data = self._request.get_request(self.system_initialize_status_url, BehaviorStatus).data
        self.logger.debug(f"Get Request: System Initialize Status response: \n{received_data}")
        return received_data

    def system_emergency_stop(self) -> RestResponse:
        self.logger.debug("Post Request: System Emergency Stop")
        return self._request.post_request(self.emergency_stop_url)

    def system_workflow_start(self, payload: SystemMetaBeginWorkflowRequest) -> RestResponse[None]:
        self.logger.debug("Post Request: System Workflow Start")
        return self._request.post_request(self.system_workflow_url, payload)

    def system_workflow_delete(self) -> RestResponse[None]:
        self.logger.debug("Delete Request: System Workflow Delete")
        return self._request.delete_request(self.system_workflow_url)

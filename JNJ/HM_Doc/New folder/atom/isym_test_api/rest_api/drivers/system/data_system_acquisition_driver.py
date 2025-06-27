from urllib.parse import urljoin

from isym_test_api.rest_api.api.behavior.channel_configuration_response import ChannelConfigurationResponse
from isym_test_api.rest_api.api.behavior.system_meta_report_response import SystemMetaReportResponse
from isym_test_api.rest_api.api.system.system_sample_queue_request import SystemSampleQueue
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from isym_test_api.rest_api.api.base_response import RestResponse
from utilities.logger import Logger


class DatasystemAcquisitionDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.data_channels_url = urljoin(base_url, "api/datasystem/acquisition/channels")
        self.injection_url = urljoin(base_url, "api/datasystem/acquisition/inject")
        self.method_url = urljoin(base_url, "api/datasystem/acquisition/method")
        self.method_status_url = urljoin(base_url, "api/datasystem/acquisition/method/status")
        self.monitor_baseline_url = urljoin(base_url, "api/datasystem/acquisition/monitorbaseline")
        self.purge_injector_url = urljoin(base_url, "api/datasystem/acquisition/purgeinjector")
        self.post_run_report_url = urljoin(base_url, "api/datasystem/acquisition/postrunreport")
        self.sample_queue_url = urljoin(base_url, "/api/datasystem/acquisition/samplequeue")
        self.start_equilibrating_url = urljoin(base_url, "/api/datasystem/acquisition/equilibrate")
        self.wash_needle_url = urljoin(base_url, "api/datasystem/acquisition/washneedle")
        self.wet_prime_url = urljoin(base_url, "api/datasystem/acquisition/wetprime")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def get_data_channels_status(self):
        received_data = self._request.get_request(self.data_channels_url, ChannelConfigurationResponse).data
        self.logger.debug(f"Get data channels status response: \n{received_data}")
        return received_data

    def get_post_run_report(self):
        received_data = self._request.get_request(self.post_run_report_url, SystemMetaReportResponse).data
        self.logger.debug(f"Get post run report response: \n{received_data}")
        return received_data

    def set_method_tuv(self, payload) -> RestResponse:
        self.logger.debug(f"Post Request Method dataset: \n{payload}")
        return self._request.post_request(self.method_url, payload)

    def start_injection(self, payload):
        self.logger.debug(f"Post Request Inject dataset: \n{payload}")
        self._request.post_request(self.injection_url, payload)

    def start_monitor_baseline(self, payload):
        self.logger.debug(f"Post Request Monitor baseline dataset: \n{payload}")
        self._request.post_request(self.monitor_baseline_url, payload)

    def start_equilibrate(self, payload):
        self.logger.debug(f"Post Request Equilibrate dataset: \n{payload}")
        self._request.post_request(self.start_equilibrating_url, payload)

    def start_wet_prime(self, payload):
        self.logger.debug(f"Post Request Wet Prime dataset: \n{payload}")
        self._request.post_request(self.wet_prime_url, payload)

    def start_wash_needle(self, payload):
        self.logger.debug(f"Post Request Wash Needle dataset: \n{payload}")
        self._request.post_request(self.wash_needle_url, payload)

    def start_purge_injector(self, payload):
        self.logger.debug(f"Post Request Purge Injector dataset: \n{payload}")
        self._request.post_request(self.purge_injector_url, payload)

    def set_sample_queue(self, payload) -> RestResponse[None]:
        received_data = self._request.put_request(self.sample_queue_url, payload)
        self.logger.debug(f"Post Put Sample Queue dataset: \n{payload}")
        return received_data

    def get_sample_queue(self) -> RestResponse[SystemSampleQueue]:
        received_data = self._request.get_request(self.sample_queue_url, response_type=SystemSampleQueue)
        self.logger.debug(f"Post Get Sample Queue dataset: \n{received_data}")
        return received_data

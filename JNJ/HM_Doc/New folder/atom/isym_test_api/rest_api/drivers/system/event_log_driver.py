from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.system.event_log_request import EventLogConfiguration
from isym_test_api.rest_api.api.behavior.system_meta_report_response import CommonMetaEventMetadata
from isym_test_api.rest_api.api.system.event_log_response import EventLogMultipleResponse
from isym_test_api.rest_api.api.system.event_log_entry_request import EventLogSingleEntry, EventLogMultipleEntries
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class EventLogDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.event_entry_url = urljoin(base_url, "api/system/logs/event/entry")
        self.event_entries_url = urljoin(base_url, "api/system/logs/event/entries")

        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def add_event_log_entry(self, payload: EventLogConfiguration) -> RestResponse[None]:
        self.logger.debug(f"Put Request Event Log Entry: \n{payload}")
        return self._request.put_request(self.event_entry_url, payload)

    def get_single_event_log_entry(self, payload: EventLogSingleEntry) -> RestResponse[CommonMetaEventMetadata]:
        return self._request.post_request(self.event_entry_url, payload, CommonMetaEventMetadata)

    def get_all_event_log_entry(self, payload: EventLogMultipleEntries) -> RestResponse[EventLogMultipleResponse]:
        return self._request.post_request(self.event_entries_url, payload, EventLogMultipleResponse)


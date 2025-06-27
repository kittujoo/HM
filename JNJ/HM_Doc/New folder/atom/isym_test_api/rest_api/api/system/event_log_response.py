from dataclasses import dataclass
from typing import List
from isym_test_api.rest_api.api.behavior.system_meta_report_response import CommonMetaEventMetadata


@dataclass
class EventLogEvents:
    # The encapsulation of alarm information that a subscriber will receive
    events: List[CommonMetaEventMetadata]


@dataclass
class EventLogMultipleResponse:
    # The collection of alarm information produced in response to client query
    events: EventLogEvents
    # The page number of the events
    pageNumber: int
    # The total number of pages
    pageCount: int
    dataModelType: str
    dataModelVersion: int

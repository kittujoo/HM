from dataclasses import dataclass
from typing import List


@dataclass
class Request:
    verb: str
    sbPayload: str
    nbPayload: str
    publicTopic: str
    internalTopic: str


@dataclass
class Endpoint:
    requestHandler: str
    endpoint: str
    requests: List[Request]


@dataclass
class RestEndpointsResponse:
    endpoints: List[Endpoint]

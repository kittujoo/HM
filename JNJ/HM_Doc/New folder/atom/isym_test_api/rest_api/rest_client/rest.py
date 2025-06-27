import json
from dataclasses import is_dataclass
from enum import Enum
from json import JSONDecodeError
from typing import Dict
from typing import Type, Any

from requests import Session

from isym_test_api.rest_api.rest_client.rest_response import RestResponse
from utilities.json_utility import as_dict
from utilities.logger import Logger
from utilities.requests_helper import urljoin
from utilities.type_converter import T


class HttpMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class RestClient(Session):

    def __init__(self, base_url: str, log_request: bool = False, log_response: bool = False, **kwargs):
        super().__init__()
        self._base_url: str = base_url
        self.log_request = log_request
        self.log_response = log_response
        session_headers = kwargs.pop("session_headers", None)
        self.headers.update(session_headers)
        self.logger = Logger(self.__class__.__name__)

    def _request(self, method: HttpMethods, endpoint: str, payload: Any = None, response_type: Type[T] = None, **kwargs):

        url = urljoin(self._base_url, endpoint)

        if payload is not None:
            payload = self._prepare_data(payload)

        if self.log_request:
            self.logger.debug(f"{method.value} request\nURL: [{url}]\nPayload: {payload}")

        response = super().request(method.value, url, json=payload, **kwargs)

        if self.log_response:
            self.logger.debug(f"{method.value} Response\nURL: [{url}]\nStatus code: [{response.status_code}]\nResponse: [{response.text}]")

        try:
            json_obj = json.loads(response.text) if response.text else None
        except JSONDecodeError as ex:
            self.logger.error(f"Failed to decode response from [{method} {endpoint}] with error [{ex}]. "
                              f"Status code was: [{response.status_code}]. Body: [{response.text}]")
            raise ex from None
        result = RestResponse(response.status_code, json_obj, response_type)
        return result

    def get(self, url, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        result = self._request(HttpMethods.GET, url, response_type=response_type, **kwargs)

        return result

    def put(self, url, payload: Any = None, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        result = self._request(HttpMethods.PUT, url, payload=payload, response_type=response_type, **kwargs)

        return result

    def post(self, url, payload=None, response_type: Type[T] = None, **kwargs) -> RestResponse[T]:

        result = self._request(HttpMethods.POST, url, payload=payload, response_type=response_type, **kwargs)

        return result

    def delete(self, url, payload=None, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        result = self._request(HttpMethods.DELETE, url, payload=payload, response_type=response_type, **kwargs)

        return result

    @staticmethod
    def _prepare_data(payload):
        if is_dataclass(payload):
            return as_dict(payload)
        else:
            return payload

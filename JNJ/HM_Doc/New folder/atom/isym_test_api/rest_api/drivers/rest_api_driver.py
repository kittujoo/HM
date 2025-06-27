from dataclasses import is_dataclass
from typing import Dict
from typing import Type, Any

from requests import Session

from isym_test_api.rest_api.api.base_response import RestResponse
from utilities.json_utility import as_dict
from utilities.logger import Logger
from utilities.type_converter import T


class RestAPIDriver(object):

    def __init__(self, session: Session, log_request: bool = False, log_response: bool = False):
        self.log_request = log_request
        self.log_response = log_response
        self.logger = Logger(self.__class__.__name__)
        self._session = session

    def get_request(self, url, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        api_response = self._session.get(url)

        response = self._process_response(url, "Get", api_response.status_code, api_response.text, response_type, **kwargs)

        return response

    def put_request(self, url, payload: Any = None, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        if self.log_request:
            self.logger.debug(f"Put request\nURL => {url}\nPayload => {payload}")

        data = self._prepare_data(payload)

        api_response = self._session.put(url, json=data)

        response = self._process_response(url, "Put", api_response.status_code, api_response.text, response_type, **kwargs)

        return response

    def post_request(self, url, payload=None, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        if self.log_request:
            self.logger.debug(f"Post request\nURL => {url}\nPayload => {payload}")

        data = self._prepare_data(payload)

        api_response = self._session.post(url, json=data)

        response = self._process_response(url, "Post", api_response.status_code, api_response.text, response_type, **kwargs)

        return response

    def delete_request(self, url, payload=None, response_type: Type[T] = Dict, **kwargs) -> RestResponse[T]:

        if self.log_request:
            self.logger.debug(f"Post request\nURL => {url}\nPayload => {payload}")

        data = self._prepare_data(payload)

        api_response = self._session.delete(url, json=data)

        response = self._process_response(url, "Delete", api_response.status_code, api_response.text, response_type, **kwargs)
        return response

    def _process_response(self, url, verb, status_code, response_text, response_type: Type[T], **kwargs) -> RestResponse[T]:
        if self.log_response:
            self.logger.debug(f"{verb} Response\nURL => {url}\nStatus code => {status_code}\nResponse => {response_text}")

        if expected_status_code := kwargs.get("expected_status_code", False):
            assert status_code == expected_status_code, f"Unexpected status code: [{status_code}]"

        if not response_text:
            raise ValueError("Response body was empty, nothing to process")
        return RestResponse(status_code, response_text, response_type)

    @staticmethod
    def _prepare_data(payload: Any):
        if is_dataclass(payload):
            return as_dict(payload)
        else:
            return payload

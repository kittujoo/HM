"""
File_Name: base_response.py
Desc: This file contains the function that return the common response from any request
"""
import json
from json import JSONDecodeError
from typing import Generic, Type, Dict

import marshmallow_dataclass
from marshmallow import RAISE, Schema, pre_load, ValidationError

from argument_constants import notset
from utilities.logger import Logger
from utilities.types import T

logger = Logger("base_response")


class RestApiException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ClientRestApiException(RestApiException):
    """Exception raised for rest response that have status code 400 ~ 499.
    """

    def __init__(self, status_code: int, response_body):
        self.message = (f"Request failed with status code {status_code}\n"
                        "Response body:\n"
                        f"{response_body}")
        super().__init__(self.message)


class ServerRestApiException(RestApiException):
    """Exception raised for rest response that have status code 500 ~ 599.
    """

    def __init__(self, status_code: int, response_body):
        self.message = (f"Request failed with status code {status_code}\n"
                        "Response body:\n"
                        f"{response_body}")
        super().__init__(self.message)


class IsymSchema(Schema):

    @pre_load
    def resolve_absent_fields(self, data: Dict, **kwargs):
        absent_fields = self.load_fields.keys() - data.keys()
        if absent_fields:
            data.update({key: None for key in absent_fields})
        return data


class RestResponse(Generic[T]):
    def __init__(self, status_code: int, response_text: str, response_type: Type[T]):
        self._response_text: str = response_text
        self._body: Dict = notset
        self._status_code = status_code
        self._response_type = response_type
        self._response_object: T = notset

    @property
    def data(self) -> T:
        if self._response_object != notset:
            return self._response_object
        else:
            body = self.body.get("data")
            if not body:
                self._response_object = None
                return self._response_object
            if self._response_type == Dict:
                self._response_object = body
                return self._response_object
            schema = marshmallow_dataclass.class_schema(self._response_type)()
            try:
                self._response_object = schema.load(body, unknown=RAISE)
            except ValidationError as e:
                message = (f"Failed to deserialize type: [{self._response_type}]\n"
                           f"Valid data: [{e.data}]\n"
                           f"Actual data: [{e.valid_data}]\n"
                           f"Error: [{e.messages}]")
                logger.error(message)
                raise ValueError(message)
            return self._response_object

    @property
    def body(self) -> dict:
        if self._body != notset:
            return self._body
        elif self.is_successful():
            try:
                self._body = json.loads(self._response_text)
                return self._body
            except JSONDecodeError as ex:
                logger.error(f"Failed to decode response: [{self._response_text}]")
                raise ex from None
        elif 400 <= self.status_code <= 499:
            raise ClientRestApiException(self.status_code, str(self._response_text))
        elif 500 <= self.status_code:
            raise ServerRestApiException(self.status_code, str(self._response_text))
        else:
            raise RestApiException(f"Unexpected status code returned: {self.status_code}")

    @property
    def error_code(self):
        return self.body.get("errorCode")

    @property
    def message(self) -> str:
        return self.body.get("message")

    @property
    def status_code(self):
        return self._status_code

    def is_successful(self):
        return 200 <= self.status_code <= 299

    def is_failed(self):
        return not self.is_successful()

    def __repr__(self):
        return str(f"Status code: [{self.status_code}]\n"
                   f"Body: {self._response_text}")

    def __str__(self):
        return self.__repr__()

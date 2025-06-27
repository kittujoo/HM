from typing import Dict, Type, Generic, Optional

import marshmallow_dataclass
from marshmallow import RAISE

from argument_constants import notset
from isym_test_api.rest_api.api.base_response import IsymSchema, ClientRestApiException, ServerRestApiException, RestApiException
from utilities.types import T


class RestResponse(Generic[T]):
    def __init__(self, status_code: int, response_obj: Optional[Dict], response_type: Type[T]):
        self._body = response_obj
        self._status_code = status_code
        self._response_type = response_type
        self._response_object: T = notset

    @property
    def data(self) -> T:
        if self._response_object != notset:
            return self._response_object
        elif self.is_successful():
            if not self._body:
                self._response_object = None
                return self._response_object
            if self._response_type is None:
                self._response_object = None
                return self._response_object
            if self._response_type == Dict:
                self._response_object = self._body
                return self._response_object
            schema = marshmallow_dataclass.class_schema(self._response_type, base_schema=IsymSchema)()
            self._response_object = schema.load(self._body, unknown=RAISE)
            return self._response_object
        elif 400 <= self.status_code <= 499:
            raise ClientRestApiException(self.status_code, str(self.body))
        elif 500 <= self.status_code:
            raise ServerRestApiException(self.status_code, str(self.body))
        else:
            raise RestApiException(f"Unexpected status code returned: {self.status_code}")

    @property
    def body(self) -> dict:
        return self._body

    @property
    def status_code(self):
        return self._status_code

    def is_successful(self):
        return 200 <= self.status_code <= 299

    def is_failed(self):
        return not self.is_successful()

    def __repr__(self):
        return str(f"Status code: [{self.status_code}]\n"
                   f"Body: {self._body}")

    def __str__(self):
        return self.__repr__()

    def validate_status_code(self):
        assert self.is_successful(), f"Request failed with status code {self.status_code}"

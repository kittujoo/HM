import os
from functools import wraps
from time import time

import requests

from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def if_none_get(value, backing_value):
    if value is None:
        return backing_value
    return value


def retrieve_http_request_status(url):
    """Retrieves the http status code for a given url.
    Args:
        url (_type_): URL to retrieve http status code for.
    Raises:
        e: Exception raised if there is an error retrieving the http status code.
    Returns:
        _type_: Http status code.
    """
    try:
        r = requests.head(url)
        return r.status_code
    except Exception as e:
        logger.error(f"Error retrieving http status code for url: {url} with error: {e}")
        raise e


class Task:
    def __init__(self, task_name):
        self.task_name = task_name
        self._start_time = None

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self._start_time = time()
            print(self.task_name, end=" STARTED\n")
            status = ""
            try:
                result = func(*args, **kwargs)
                status = "PASSED"
                return result
            except Exception as e:
                status = "FAILED"
                raise e from None
            finally:
                finish_time = round(time() - self._start_time, 2)
                print(f"{self.task_name} {status} after {finish_time} seconds")

        return wrapper

    def __enter__(self):
        self._start_time = time()
        print(self.task_name, end=" STARTED\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        finish_time = round(time() - self._start_time, 2)
        if exc_type:
            print(f"{self.task_name} FAILED after {finish_time} seconds")
        else:
            print(f"{self.task_name} PASSED after {finish_time} seconds")


task = Task

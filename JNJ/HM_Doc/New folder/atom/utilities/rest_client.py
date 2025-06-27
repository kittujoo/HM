from requests import Session
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def rest_session() -> Session:
    session = Session()
    retry = Retry(total=None, connect=10, backoff_factor=0.1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

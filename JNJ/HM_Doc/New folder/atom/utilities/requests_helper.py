import os

import requests
from requests_toolbelt import MultipartEncoder

from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def download_file(url, target_path, fail_on_error=True):
    r = requests.get(url, allow_redirects=True)
    if fail_on_error and not 200 <= r.status_code < 300:
        raise ValueError(f"Failed to download a file from: [{url}]")

    open(target_path, 'wb').write(r.content)


def download_file_stream(url, target_path, fail_on_error=True):
    with requests.get(url, allow_redirects=True, stream=True) as response:
        if fail_on_error and not 200 <= response.status_code < 300:
            raise ValueError(f"Failed to download a file from: [{url}]")
        length = int(response.headers["content-length"])
        chunk_size = 1024
        with open(target_path, 'wb') as file:
            i = 1
            downloaded_percents = 0.0
            print(f"[0.0%] received")
            for chunk in response.iter_content(chunk_size):
                percentage = round((i * chunk_size) / length * 100, 2)
                if percentage - downloaded_percents >= 1:
                    print(f"\r[{percentage}%] received")
                    downloaded_percents = percentage
                i += 1
                file.write(chunk)


def upload_file(url, file_path, fail_on_error=True):
    file_name = os.path.basename(file_path)
    m = MultipartEncoder(
        fields={'file': (file_name, open(file_path, 'rb'))}
    )
    r = requests.post(url, allow_redirects=True, verify=False, data=m, headers={'Content-Type': m.content_type})
    if fail_on_error and not 200 <= r.status_code < 300:
        raise ValueError(f"Failed to upload a file to: [{url}]")


def urljoin(*args):
    """
    Joins given arguments into an url. Trailing but not leading slashes are
    stripped for each argument.
    """

    return "/".join(map(lambda x: str(x).rstrip('/'), args))

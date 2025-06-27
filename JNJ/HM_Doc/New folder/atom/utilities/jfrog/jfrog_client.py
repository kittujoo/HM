import os
from typing import List

from artifactory import ArtifactoryPath
from retry import retry

from utilities.hash_functions import get_file_md5
from utilities.logger import Logger
from utilities.requests_helper import urljoin

logger = Logger(os.path.basename(__file__))


class DownloadProgressLogger:
    def __init__(self):
        self._downloaded_percents = 0.0
        self._downloaded_mb = 0

    def __call__(self, bytes_now, total_size):
        """
        Function to log download progress
        :param bytes_now: current number of bytes
        :param total_size: total file size in bytes
        :return:
        """
        current_progress_mb = int(bytes_now / 1024 / 1024)
        if total_size > 0:
            current_progress_perc = round(bytes_now / total_size * 100, 2)
            total_size_mb = int(total_size / 1024 / 1024)
            if current_progress_perc - self._downloaded_percents > 1:
                self._downloaded_percents = current_progress_perc
                logger.debug(f"Downloaded {current_progress_mb}/{total_size_mb}MB...[{current_progress_perc}%]")
        else:
            if current_progress_mb - self._downloaded_mb > 25:
                self._downloaded_mb = current_progress_mb
                logger.debug(f"Downloaded {current_progress_mb}MB")


class JfrogClient:
    def __init__(self, host, port, api_token):
        self.api_key = api_token
        self.artifactory_url = f"http://{host}:{port}/artifactory"

    def aql_search_artifact(self, query: str) -> List[ArtifactoryPath]:
        path = ArtifactoryPath(self.artifactory_url, apikey=self.api_key)
        results = path.aql(*query)
        paths = [path.from_aql(result) for result in results]
        return paths

    def get_artifact_properties(self, path_to_artifact):
        artifact_url = urljoin(self.artifactory_url, path_to_artifact)
        path = ArtifactoryPath(artifact_url)
        return path.properties

    def get_artifact_property(self, path_to_artifact, property_name: str):
        properties = self.get_artifact_properties(path_to_artifact)
        prop = properties.get(property_name, None)
        assert prop, f"Property [{property_name}] not found"
        return prop[0] if isinstance(prop, list) else prop

    @staticmethod
    @retry(exceptions=FileNotFoundError, tries=3)
    def download_artifact_in_chunks(artifact_path: ArtifactoryPath, save_path: str):
        # download by providing path to out file and use default chunk 1024
        artifact_path.writeto(out=save_path, progress_func=DownloadProgressLogger())
        expected_file_md5 = artifact_path.stat().md5
        actual_file_md5 = get_file_md5(save_path)
        if actual_file_md5 != expected_file_md5:
            message = f"Downloaded file was broken, expected file md5: [{expected_file_md5}], actual: [{actual_file_md5}]"
            logger.error(message)
            os.remove(save_path)
            raise FileNotFoundError(message)


def get_client(token: str):
    return JfrogClient("rdeidgart.rdeadmin.waters.com", 8081, token)

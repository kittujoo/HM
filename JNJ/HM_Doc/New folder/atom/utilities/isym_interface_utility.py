import io
import os
import zipfile

import requests

from utilities.file_handler import delete_folder
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def get_isym_interface_commit_by_application_version(token, isym_application_version):
    if not token:
        raise ValueError("Token for isym repository was not provided.")

    url = "https://code.waters.com/bitbucket/rest/api/latest/projects/IS/repos/isym-application/browse"

    parameters = {'at': f'refs/tags/{isym_application_version}', 'limit': '1000'}
    response = _get_bitbucket_response(url, token, parameters)

    json_obj = response.json()
    submodule_details = [x for x in json_obj['children']['values'] if x.get("url") == "../isym-interface.git"]
    commit_id = submodule_details[-1]['contentId'] if submodule_details else None
    return commit_id


def download_isym_interface(target_path, token, isym_interface_version, isym_application_version):
    """
    Download the isym-interface proto models
    """
    logger.info("Starting to download isym-interface")

    query = {
        "path": "/Api/Python/"
    }

    if isym_interface_version == "auto":
        if not isym_application_version:
            raise ValueError("Application version for isym was not provided.")
        logger.info("Starting to obtain proper isym interface version")
        isym_interface_version = get_isym_interface_commit_by_application_version(token, isym_application_version)

    logger.debug("Delete interface directory before cloning")
    delete_folder(target_path)

    logger.debug("Cloning isym-interface")
    get_bitbucket_repo(token=token,
                       target_folder=target_path,
                       project_name="IS",
                       repo_name="isym-interface",
                       query=query)
    logger.debug(f"checking out isym-interface specific version '{isym_interface_version}'")

    logger.info("isym-interface cloned successfully")


def download_isym_python_models(target_path, token, isym_interface_version="develop", isym_application_version=None):
    """
        Download the isym-interface proto models
    """
    logger.info("Starting to download isym-interface")

    query = {
        "path": "Api/V4/Python/"
    }

    if isym_interface_version == "auto":
        if not isym_application_version:
            raise ValueError("Application version for isym was not provided.")
        logger.info("Starting to obtain proper isym interface version")
        query["at"] = get_isym_interface_commit_by_application_version(token, isym_application_version)
    else:
        query["at"] = isym_interface_version

    logger.debug("Delete interface directory before cloning")
    delete_folder(target_path)

    get_bitbucket_repo(token=token,
                       target_folder=target_path,
                       project_name="IS",
                       repo_name="isym-interface",
                       query=query)
    logger.debug(f"checking out isym-interface python models specific version '{isym_interface_version}'")

    logger.info("isym-interface cloned successfully")


def get_bitbucket_repo(token, target_folder, project_name="IS", repo_name="isym-interface", query=None):
    if not token:
        raise ValueError("Token for isym repository was not provided.")

    url = f"https://code.waters.com/bitbucket/rest/api/latest/projects/{project_name}/repos/{repo_name}/archive"

    logger.debug("Call for bitbucket repo zip file")

    response = _get_bitbucket_response(url, token, query)

    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    logger.debug("Unzipping downloaded repo files")
    path = query.get("path", None)
    if not path:
        zip_file.extractall(target_folder)
    else:
        for zip_item in zip_file.infolist():
            if zip_item.filename in path:
                continue
            zip_item.filename = zip_item.filename.replace(path, "")
            zip_file.extract(zip_item, target_folder)


def _get_bitbucket_response(url, token, parameters):
    response = requests.get(url=url,
                            params=parameters,
                            headers={'Authorization': f'Bearer {token}'})

    if response.status_code != 200:
        message = f"Failed to get [{url}] with status code [{response.status_code}], response: [{response.text}]"
        logger.error(message)
        raise ValueError(message)

    return response

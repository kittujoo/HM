import os
import subprocess

from utilities.constants import EMPOWER_BIN_FOLDER
from utilities.constants import EMPOWER_PROJECTS_FOLDER
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class ProjectRestoreDriver:
    """
    Class to manage the project restore process
    """

    def __init__(self, username: str, password: str, test_data_dir: str):
        self._username: str = username
        self._password: str = password
        self.test_data_dir: str = test_data_dir
        self._project_manager_exe: str = f"{EMPOWER_BIN_FOLDER}\\cmgr.exe"

    def restore(self, project_name):
        ics_project_path = os.path.join(EMPOWER_PROJECTS_FOLDER, project_name)
        if os.path.exists(ics_project_path):
            logger.info(f"Empower project already exists: '{ics_project_path}'.")
            return
        project_folder = os.path.join(self.test_data_dir, project_name)
        args = " ".join([
            f"-user {self._username}",
            f"-pw {self._password}",
            "-proj all",
            f"-restore {project_folder}",
            f"-projName {project_name}"
        ])
        return_code = subprocess.call(["powershell", "start-process", "-FilePath", self._project_manager_exe, "-ArgumentList", f'"{args}"'])
        assert return_code == 0, f"Failed to restore the Empower project '{project_name}', return code: '{return_code}'"

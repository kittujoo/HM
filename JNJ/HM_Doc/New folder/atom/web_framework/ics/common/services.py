import os
import subprocess
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class Services:
    """Class to Manage Services"""

    @staticmethod
    def validate_service_status(service_name):
        logger.info(f"Checking for running service: {service_name}")

        command = f'sc query "{service_name}" | findstr "STATE"'
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        logger.debug(f"Running services output: {output}")

        assert "RUNNING" in output, f"Service '{service_name}' is not running"

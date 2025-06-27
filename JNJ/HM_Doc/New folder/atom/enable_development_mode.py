import os
import subprocess
import sys
from winreg import REG_DWORD

from utilities.atom.configurations import configure_logger
from utilities.atom.constants import ATOM_ROOT_FOLDER, RESULTS_FOLDER
from utilities.common_utilities import task
from utilities.constants import EMPOWER_INSTRUMENTS_FOLDER
from utilities.logger import Logger
from utilities.windows_registry_utility import set_registry_key_value

if not os.path.exists(RESULTS_FOLDER):
    # create results directory if missing
    os.makedirs(RESULTS_FOLDER)

logger = Logger(os.path.basename(__file__))

nginx_conf_file = os.path.join(EMPOWER_INSTRUMENTS_FOLDER, "Nginx", "conf", "instruments", "instruments.conf")


def main():
    configure_logger(RESULTS_FOLDER)
    path = r"SOFTWARE\WOW6432Node\Waters\Instruments\Alliance iS"
    prop_name = "UIDevelopmentMode"

    with task("Enable registry ics development mode"):
        set_registry_key_value(path, prop_name, 1, REG_DWORD)

    with task(f"Delete old nginx configuration file"):
        if os.path.exists(nginx_conf_file):
            os.remove(nginx_conf_file)

    with task("Restart waters nginx service"):
        service_name = "WatersNGINXInstrumentService"
        subprocess.run(["net", "stop", service_name], check=True)
        subprocess.run(["net", "start", service_name], check=True)

    with task("Validate new nginx configuration file created"):
        if not os.path.exists(nginx_conf_file):
            raise ValueError(f"No nginx configuration was found: [{nginx_conf_file}]")


if __name__ == "__main__":
    if ATOM_ROOT_FOLDER not in sys.path:
        sys.path.append(ATOM_ROOT_FOLDER)
    main()

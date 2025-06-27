import os
import re

from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface
from utilities.telnet_connection import TelnetConnection

logger = Logger(os.path.basename(__file__))


class InstrumentManifestCollector(ManifestCollectorInterface):
    """Collects instruments versions into manifest file"""

    def __init__(self, instrument_name, hostname, username, password, port):
        self.instrument_name = instrument_name
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def _get_instrument_manifest_version(self):
        """  This function will collect the manifest version for instruments
             return: string (contains build version)
        """
        res = ''
        try:
            with TelnetConnection(self.hostname, self.username, self.password, self.port) as telnet:
                telnet.read_until_console_available()
                telnet.send_command(command="banner")
                res = str(telnet.read_until(text=b"Common Library Version:"))
                results = re.findall(r"Version: ([\w.-]*).*Common Library Version", res)
                res = results[0] if results else 'Version is not captured although telnet session was created'
                return res
        except Exception as e:
            logger.error(f"Exception raised while capturing version of {self.instrument_name} instrument from response: {str(res)}, error was [{e}]")
            return "Failed to obtain"

    def enrich_manifest(self, manifest_dict):
        manifest_dict.setdefault("Instruments", {})
        manifest_dict["Instruments"][self.instrument_name] = self._get_instrument_manifest_version()

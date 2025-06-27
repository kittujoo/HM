"""
File_Name: empower_utility.py
Desc:
    Generic class for Empower related actions.

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Catalin Goran" Initial check-in - April 18, 2023
"""

import os
from dataclasses import dataclass, field
from logging import Logger
from pathlib import Path
from typing import Optional, Dict
from xml.etree import ElementTree

from utilities.constants import SYSTEM_TYPE, BETA_SYSTEM_TYPE, DHCP_CONFIG_PATH
from utilities.ssh_connection import SSh
from utilities.windows_registry_utility import get_registry_key_value

logger = Logger(os.path.basename(__file__))


@dataclass
class EmpowerConfiguration:
    ics_executable_name: str
    ics_instrument_type: str
    empower_system_name: str
    ics_installer_path: str
    ics_download_url: str
    ics_version: str
    reg_key: str
    username: str
    password: str
    hardware_system_name: str
    install_path: Optional[str] = field(init=False)

    def __post_init__(self):
        try:
            empower_bin_path = get_registry_key_value(reg_name="BinDirectory", key=self.reg_key)
            self.install_path = str(Path(empower_bin_path).parent.absolute())
        except Exception as e:
            logger.error("Exception on reading Empower path: {e}")
            self.install_path = None


def extract_instruments_dhcp_lease(content: str, system_name: str = '') -> Dict[str, str]:
    """
    Get IP from DHCP.xml file for Name
    :param content: Content of the XML file
    :param system_name: Name of the system
    :return: IP Address
    """
    found_leases = []
    try:
        xml, ids = ElementTree.XMLID(content)
        for lease in xml.findall("./Leases/Lease"):
            found_leases.append(
                {
                    "name": lease.find("./Name").text,
                    "type": lease.find("./Type").text,
                    "ip": lease.find("./IP").text,
                    "mac": lease.find("./MAC").text
                }
            )

    except Exception as e:
        logger.error(f"Error happened during dealing with dhcp.xml file: {e}")
        raise e from None

    leases = [item for item in found_leases if item["type"] in [SYSTEM_TYPE, BETA_SYSTEM_TYPE]]
    if system_name and len(leases) > 1:
        leases = [item for item in leases if item["name"] == system_name]
    if len(leases) > 1:
        error_message = f"Invalid amount of system leases found on empower pc: {leases}" if system_name \
            else f"Found more than one ip lease for instruments on empower pc, please provide 'system name' to specify filter: {leases}"
        logger.error(error_message)
        raise ValueError(error_message)
    elif not leases:
        error_message = f"No appropriate leases found: {found_leases}"
        logger.error(error_message)
        raise ValueError(error_message)
    return leases[0]


def get_remote_instruments_dhcp_lease(host: str, port: int, username: str, password: str, system_name: str = "") -> Dict[str, str]:
    """
    Utility to return system IP
    :param host: Host IP
    :param port: Port Number
    :param username: Username for the host
    :param password: Password for the host
    :param system_name: Name of the system
    :return: IP
    """

    with SSh(address=host, username=username, password=password, port=port) as ssh:
        remote_file = ssh.get_file_text(DHCP_CONFIG_PATH)
        lease = extract_instruments_dhcp_lease(content="\n".join(remote_file), system_name=system_name)
        return lease


def get_local_instruments_dhcp_lease(system_name: str = "") -> Dict[str, str]:
    """
    Utility to return system IP
    :param system_name: Name of the system
    :return: IP
    """

    with open(DHCP_CONFIG_PATH) as f:
        file_text = f.read()
        lease = extract_instruments_dhcp_lease(content=file_text, system_name=system_name)
        return lease

"""
File_Name: windows_registry_utility.py
Desc:
    Generic class for registry related actions.
    This is Windows only and should be used only for ICS driver testing on Empower machine!

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Catalin Goran" Initial check-in - April 18, 2023
"""

import os
import sys
from logging import Logger
from typing import Union

try:
    import winreg
except ImportError:
    if 'nt' in sys.builtin_module_names:
        raise ImportError('Running a test on Windows and winreg module was not found!')

logger = Logger(os.path.basename(__file__))


def get_registry_key_value(reg_name, key, hkey_type=None):
    try:
        hkey_type = hkey_type or winreg.HKEY_LOCAL_MACHINE
        key = winreg.OpenKey(hkey_type, key)
        value, regtype = winreg.QueryValueEx(key, reg_name)
        winreg.CloseKey(key)
    except Exception as e:
        logger.error(f"Exception on reading value from registry: {e}")
        return None

    return value


def set_registry_key_value(path, name: str, value: Union[str, int], value_type: int, hkey_type=None):
    try:
        hkey_type = hkey_type or winreg.HKEY_LOCAL_MACHINE
        key = winreg.OpenKey(hkey_type, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, value_type, value)
        winreg.CloseKey(key)
    except Exception as e:
        logger.error(f"Exception on reading value from registry: {e}")
        return None

    return value


def is_registry_key_exists(app_key):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, app_key, 0, winreg.KEY_READ) as key:
            return True
    except Exception:
        logger.debug(f"Registry key not found at '{app_key}'.")
        return False


def is_instrument_installed(instrument_name):
    """
    Check if instrument is installed on the system.
    :param instrument_name: Name of the instrument to check.
    :return: True if instrument is installed, False otherwise.
    """
    instrument_registry_key = f"SOFTWARE\\WOW6432Node\\Waters\\Instruments\\InstrumentNames\\{instrument_name}"
    return is_registry_key_exists(instrument_registry_key)

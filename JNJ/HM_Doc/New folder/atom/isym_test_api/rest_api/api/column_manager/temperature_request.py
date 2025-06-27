"""
Desc: This file contains the payload that needs to be sent with a temperature request
"""
from dataclasses import dataclass


@dataclass
class ColumnTemperatureW:
    # The requested sample temperature (deg C)
    targetTemperatureDegC: float = 20.0

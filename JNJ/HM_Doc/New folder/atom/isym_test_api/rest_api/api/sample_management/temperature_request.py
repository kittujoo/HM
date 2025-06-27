"""
Desc: This file contains the payload that needs to be send with a temperature request
"""
from dataclasses import dataclass


@dataclass
class FtnSampleTemperatureW:
    # The requested sample temperature (deg C)
    targetTemperatureDegC: float = 20.0

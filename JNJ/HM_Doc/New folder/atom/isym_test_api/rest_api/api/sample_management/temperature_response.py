"""
Desc: This file contains the response received from a sample temperature get request
"""
from dataclasses import dataclass


@dataclass
class FTNTemperatureResponse:
    currentTemperatureDegC: float
    targetTemperatureDegC: float
    dataModelType: str
    dataModelVersion: int

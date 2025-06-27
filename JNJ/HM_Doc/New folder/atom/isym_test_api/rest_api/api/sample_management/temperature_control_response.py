"""
Desc: This file contains the response received from a sample temperature get request
"""
from dataclasses import dataclass


@dataclass
class FTNTemperatureControlResponse:
    thermalControlState: str
    dataModelType: str
    dataModelVersion: int

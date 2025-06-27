"""
Desc: This file contains the response payload for Delta Pressure reading
"""
from dataclasses import dataclass


@dataclass
class QsmDeltaPressure:
    deltaPressurePsi: float
    deltaMinPressurePsi: float
    deltaMaxPressurePsi: float
    dataModelType: str
    dataModelVersion: int

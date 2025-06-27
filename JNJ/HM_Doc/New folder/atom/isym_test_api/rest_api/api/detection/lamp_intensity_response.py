"""
Desc: This file contains the payload that needs to be received with a TUV Lamp Intensity
"""
from dataclasses import dataclass


@dataclass
class TuvLampIntensityTestResult:
    # Current lamp intensity
    lampIntensityPct: float

    # lampUsageThresholdPerc
    lampUsageThresholdPerc: float

    dataModelType: str
    dataModelVersion: int

"""
Desc: This file contains the payload that needs to be received with a TUV Lamp History
"""
from dataclasses import dataclass
from typing import List


@dataclass
class TuvRepeatLampInformation:
    # Lamp serial number
    serialNumber: str

    # Date when lamp was installed
    installationDate: str

    # Lifetime lamp on minutes
    lampMinutes: float

    # Number of successful ignitions in the lamp's lifetime
    successfulIgnitions: int

    # Number of failed ignitions in the lamp's lifetime
    failedIgnitions: int


@dataclass
class TuvLampHistory:
    # The lamp installation history
    lamps: List[TuvRepeatLampInformation]

    dataModelType: str
    dataModelVersion: int

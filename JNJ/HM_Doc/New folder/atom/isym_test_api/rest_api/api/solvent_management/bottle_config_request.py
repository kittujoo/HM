"""
Desc: This file contains the payload that needs to be sent with a bottle config request
"""
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


@dataclass
class SolventType:
    id: str
    name: str


class Lines(Enum):
    SolventLine_A = 0
    SolventLine_B = 1
    SolventLine_C = 2
    SolventLine_D = 3
    SolventLine_N = 4
    SolventLine_S = 5


@dataclass
class SolventLines:
    solventLine: Lines


@dataclass
class SolventBottle:
    id: str
    displayName: str
    solventType: SolventType
    sizeMl: int
    lowVolumeWarningLevelMl: int
    raiseLowVolumeWarning: bool
    lowVolumeErrorLevelMl: int
    raiseLowVolumeError: bool
    solventExpirationDate: str
    raiseSolventExpirationWarning: bool
    raiseSolventExpirationError: bool
    solventLines: List[SolventLines]


@dataclass
class SolventBottleConfig:
    solventBottle: List[SolventBottle]
    dataModelType: Optional[str] = None
    dataModelVersion: Optional[int] = None


def generate_bottle_config_default_request():
    payload = SolventBottleConfig(
        solventBottle=[
            SolventBottle(
                id="",
                displayName="",
                solventType=SolventType(
                    id="",
                    name=""
                ),
                sizeMl=1000,
                lowVolumeWarningLevelMl=400,
                raiseLowVolumeWarning=False,
                lowVolumeErrorLevelMl=100,
                raiseLowVolumeError=False,
                solventExpirationDate="",
                raiseSolventExpirationWarning=False,
                raiseSolventExpirationError=False,
                solventLines=[
                    SolventLines(
                        solventLine=Lines.SolventLine_A
                    )
                ]
            )
        ]
    )

    return payload


def generate_bottle_config_non_default_request():
    payload = SolventBottleConfig(
        solventBottle=[
            SolventBottle(
                id="A",
                displayName="A",
                solventType=SolventType(
                    id="A",
                    name="A"
                ),
                sizeMl=5000,
                lowVolumeWarningLevelMl=1000,
                raiseLowVolumeWarning=True,
                lowVolumeErrorLevelMl=500,
                raiseLowVolumeError=True,
                solventExpirationDate="2021-12-31T00:00:00.000Z",
                raiseSolventExpirationWarning=True,
                raiseSolventExpirationError=True,
                solventLines=[
                    SolventLines(
                        solventLine=Lines.SolventLine_B
                    )
                ]
            )
        ]
    )

    return payload

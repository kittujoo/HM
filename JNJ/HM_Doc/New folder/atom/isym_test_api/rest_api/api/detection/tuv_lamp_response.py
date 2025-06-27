"""
Desc: This file contains the payload that needs to be received with a TUV Lamp status
"""
from dataclasses import dataclass

from utilities.EnumBase import EnumBase


class LampStateEnum(EnumBase):
    LampState_READY = "LampState_READY"
    LampState_OFF = "LampState_OFF"
    LampState_IGNITE = "LampState_IGNITE"
    LampState_WARMING = "LampState_WARMING"


@dataclass
class LampStatusResponse:
    # Lamp control and status
    lampOn: bool
    # The current lamp state
    lampState: LampStateEnum
    # Time remaining in warming period
    remainingWarmupMin: int
    # Time spent in current state (decimal minutes)
    timeInCurrentStateMin: float
    # Total (all time) lamp has been on (decimal minutes)
    totalOnTimeMin: int

    dataModelType: str
    dataModelVersion: int

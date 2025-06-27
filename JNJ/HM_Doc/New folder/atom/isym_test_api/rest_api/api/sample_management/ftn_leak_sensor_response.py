"""
Desc: This file contains the payload that needs to be received with a FTN Leak Sensor status
"""
from dataclasses import dataclass

from utilities.EnumBase import EnumBase


class LeakStatus(EnumBase):
    LeakState_LEAK = "LeakState_LEAK",
    LeakState_NOLEAK = "LeakState_NOLEAK",
    LeakState_NOTPRESENT = "LeakState_NOTPRESENT",
    LeakState_NOTSUPPORTED = "LeakState_NOTSUPPORTED",
    LeakState_ERROR = "LeakState_ERROR"


@dataclass
class LeakSensorResponse:
    # The targeted device type
    deviceId: str
    # The leak sensor id
    leakSensorId: int
    # True if this leak sensor is enabled
    enabled: bool
    # The leak detected state
    state: LeakStatus

    dataModelType: str
    dataModelVersion: int

"""
Desc: This file contains the payload of a leak sensors response
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List


class LeakState(Enum):
    LeakState_ILLEGAL = 0  # Uninitialized
    LeakState_LEAK = 1  # Leak
    LeakState_NOLEAK = 2  # No leak
    LeakState_NOTPRESENT = 3  # Not present
    LeakState_NOTSUPPORTED = 4  # Not supported
    LeakState_ERROR = 5  # Could not get state


@dataclass
class CommonRepeatLeakSensorStatus:
    # The device id associated with this leak sensor
    deviceId: str = ""

    # The leak sensor id
    leakSensorId: int = 1

    # True if this leak sensor is enabled
    enabled: bool = True

    # The leak detected state
    state: LeakState = LeakState.LeakState_ILLEGAL


@dataclass
class LeakSensorsStatus:
    leakSensors: List[CommonRepeatLeakSensorStatus] = field(default_factory=list)

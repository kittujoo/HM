"""
Desc: This file contains the payload that needs to be sent with a Leak Sensor request
"""
from dataclasses import dataclass


@dataclass
class LeakSensorConfig:
    # The targeted device type
    deviceType: str = "Qsm"
    # The targeted device id, if necessary to distinguish multiples of the same type
    deviceId: str = "Qsm#ORIONQSM"
    # The leak sensor id
    leakSensorId: int = 1
    # True if this leak sensor is enabled
    enabled: bool = False

"""
Desc: This file contains the payload of a leak sensors configuration request
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List


@dataclass
class CommonRepeatLeakSensorConfiguration:
    # The targeted device type
    deviceType: str = ""

    # The targeted device id, if necessary to distinguish multiples of the same type
    deviceId: str = ""

    # The leak sensor id
    leakSensorId: int = 1

    # True if this leak sensor is enabled
    enabled: bool = True


@dataclass
class LeakSensorsConfiguration:
    leakSensors: List[CommonRepeatLeakSensorConfiguration] = field(default_factory=list)


def generate_disable_leak_sensors_configuration_request():
    payload = LeakSensorsConfiguration(
        leakSensors = [
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Chc#ORIONCHC",
                leakSensorId=1,
                enabled=False),
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Ftn#ORIONFTN",
                leakSensorId=1,
                enabled=False
            ),
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Qsm#ORIONQSM",
                leakSensorId=1,
                enabled=False
            ),
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Tuv#ORIONTUV",
                leakSensorId=1,
                enabled=False
            )
        ]
    )
    return payload


def generate_default_enable_leak_sensors_configuration_request():
    payload = LeakSensorsConfiguration(
        leakSensors = [
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Chc#ORIONCHC",
                leakSensorId=1,
                enabled=True),
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Ftn#ORIONFTN",
                leakSensorId=1,
                enabled=True
            ),
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Qsm#ORIONQSM",
                leakSensorId=1,
                enabled=True
            ),
            CommonRepeatLeakSensorConfiguration(
                deviceType="",
                deviceId="Tuv#ORIONTUV",
                leakSensorId=1,
                enabled=True
            )
        ]
    )
    return payload

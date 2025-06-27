"""
Desc: This file contains the payload for vent valve request
"""
from dataclasses import dataclass
from enum import Enum


class VentValvePosition(Enum):
    VentValvePosition_ILLEGAL = 0
    VentValvePosition_WASTE = 1
    VentValvePosition_SYSTEM = 2
    VentValvePosition_BLOCKED = 3
    VentValvePosition_UNKNOWN = 9999


@dataclass
class QsmVentValveW:
    position: VentValvePosition


@dataclass
class QsmMetaVentValve:
    valvePosition: QsmVentValveW
    waitForPressure: bool
    pressureThresholdPsi: float
    resumeFlow: bool


def generate_default_vent_valve_request(vent_valve_position):
    payload = QsmMetaVentValve(
        valvePosition=QsmVentValveW(
            position=vent_valve_position
        ),
        waitForPressure=True,
        pressureThresholdPsi=100.0,
        resumeFlow=False
    )
    return payload

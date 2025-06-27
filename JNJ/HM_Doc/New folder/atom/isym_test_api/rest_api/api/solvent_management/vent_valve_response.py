"""
Desc: This file contains the response payload for Vent Valve reading
"""
from dataclasses import dataclass
from enum import Enum

from isym_test_api.rest_api.api.solvent_management.vent_valve_request import VentValvePosition


class VentValveState(Enum):
    VentValveState_ILLEGAL = 0
    VentValveState_LOST = 1
    VentValveState_ERROR = 2
    VentValveState_IDLE = 3
    VentValveState_MOVING = 4


@dataclass
class QsmVentValveR:
    position: VentValvePosition
    state: VentValveState
    dataModelType: str
    dataModelVersion: int

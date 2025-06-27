"""
Desc: This file contains the response payload for Inject Valve reading
"""
from dataclasses import dataclass
from enum import Enum

from isym_test_api.rest_api.api.sample_management.inject_valve_request import InjectValvePosition


class InjectValveState(Enum):
    InjectValveState_ILLEGAL = 0
    InjectValveState_LOST = 1
    InjectValveState_ERROR = 2
    InjectValveState_IDLE = 3
    InjectValveState_MOVING = 4


@dataclass
class FtnInjectValveR:
    position: InjectValvePosition
    state: InjectValveState
    dataModelType: str
    dataModelVersion: int

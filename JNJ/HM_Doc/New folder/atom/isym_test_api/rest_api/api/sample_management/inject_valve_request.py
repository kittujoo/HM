"""
Desc: This file contains the payload for inject valve request
"""

from dataclasses import dataclass
from enum import Enum


class InjectValvePosition(Enum):
    InjectValvePosition_ILLEGAL = 0
    InjectValvePosition_BLOCK = 1
    InjectValvePosition_LOAD = 2
    InjectValvePosition_INJECT = 3
    InjectValvePosition_UNKNOWN = 9999


@dataclass
class FtnInjectValveRequest:
    position: InjectValvePosition


def generate_default_inject_valve_request(position_name):
    payload = FtnInjectValveRequest(
        position=position_name
    )
    return payload


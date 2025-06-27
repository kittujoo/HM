"""
Desc: This file contains the payload that needs to be send with a temperature request
"""
from dataclasses import dataclass
from enum import Enum


class ThermalControlState(Enum):
    ThermalControlState_ILLEGAL = 0  # Uninitialized
    ThermalControlState_OFF = 1  # Regulated thermal control off
    ThermalControlState_ON = 2  # Regulated thermal control on
    ThermalControlState_MANUAL = 3  # Manual thermal control


@dataclass
class ChcThermalControlState:
    # Thermal control state
    thermalControlState: ThermalControlState = ThermalControlState.ThermalControlState_OFF

"""
Desc: This file contains the payload that needs to be received with a TUV Lamp Request
"""
from dataclasses import dataclass


@dataclass
class LampRequest:
    # Lamp control and status
    lampOn: bool = True

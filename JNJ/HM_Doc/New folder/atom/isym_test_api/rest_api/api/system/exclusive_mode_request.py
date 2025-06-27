"""
Desc: This file contains the payload that needs to be send with an exclusivemode request
"""
from dataclasses import dataclass


@dataclass
class ExclusiveModeRequest:
    exclusiveMode: bool
    requestor: str

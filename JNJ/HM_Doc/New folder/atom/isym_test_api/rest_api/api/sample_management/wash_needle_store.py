"""
Desc: This file contains the response received from a wash needle store
"""
from dataclasses import dataclass


@dataclass
class FTNWashNeedleStore:
    # The requested wash duration second
    washDurationSec: int
    dataModelType: str
    dataModelVersion: int

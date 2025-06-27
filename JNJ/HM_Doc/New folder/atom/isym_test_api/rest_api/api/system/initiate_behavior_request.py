"""
Desc: This file contains the request to initiate behavior request
"""

from dataclasses import dataclass

@dataclass
class InitiateBehaviorRequest:
    context: str = ""

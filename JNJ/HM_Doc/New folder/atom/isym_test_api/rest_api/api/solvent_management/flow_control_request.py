"""
Desc: This file contains the payload that needs to be sent with a flow request
"""
from dataclasses import dataclass


@dataclass
class SolvFlowControlW:
    # Flowing (current non-zero) or not
    flowOn: bool = False

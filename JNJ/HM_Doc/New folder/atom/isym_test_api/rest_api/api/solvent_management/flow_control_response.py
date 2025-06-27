"""
Desc: This file contains the payload that needs to be sent with a flow response
"""
from dataclasses import dataclass


@dataclass
class SolvFlowControlR:
    """
    Class construct the QSM Flow Control Response inheriting from BaseResponse class.
    """
    flowOn: bool
    currentMlPerMin: float
    targetMlPerMin: float
    lastGoodMlPerMin: float
    dataModelType: str
    dataModelVersion: int

"""
Desc: This file contains the payload that needs to be sent with a full flow control request
"""
from dataclasses import dataclass


@dataclass
class SolvFullFlowControlW:

    # The requested flow rate (mL/min)
    flowRateTargetMlPerMin: float = 1.0

    # The % composition of solvent A
    solventAPct: float = 100.0

    # The % composition of solvent B
    solventBPct: float = 0.0

    # The % composition of solvent C
    solventCPct: float = 0.0

    # The % composition of solvent D
    solventDPct: float = 0.0

    # Ramp rate to use on flow changes (mL/min/sec)
    flowRampRateMlPerMinPerSec: float = 0.066667


def generate_default_full_flow_control_request():
    payload = SolvFullFlowControlW(
        flowRateTargetMlPerMin=1.5,
        solventAPct=50,
        solventBPct=50,
        solventCPct=0,
        solventDPct=0,
        flowRampRateMlPerMinPerSec=0.25
    )
    return payload

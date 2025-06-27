"""
Desc: This file contains the payload of a full flow control response
"""
from dataclasses import dataclass


# The SolvFullFlowControlR payload
@dataclass
class SolvFullFlowControlR:

    # Flowing (current non-zero) or not
    flowOn: bool = False

    # The current flow rate (mL/min)
    flowRateCurrentMlPerMin: float = 0.0

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

    # The last known flow rate to resume to (mL/min)
    lastGoodMlPerMin: float = 1.0

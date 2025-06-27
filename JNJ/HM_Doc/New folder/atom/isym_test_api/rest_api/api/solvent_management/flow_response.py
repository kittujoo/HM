"""
Desc: This file contains the payload that needs to be sent with a flow request
"""
from dataclasses import dataclass


@dataclass
class SolvFlowRateAndCompositionR:
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

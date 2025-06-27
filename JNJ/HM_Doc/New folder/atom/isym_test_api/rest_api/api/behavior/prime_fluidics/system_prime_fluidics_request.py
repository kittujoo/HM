"""
Desc: This file contains the payload that needs to be send with system prime fluidics request
"""
from dataclasses import dataclass


@dataclass
class SolvFlowRateAndCompositionMetadata:
    flowRateTargetMlPerMin: float
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float


@dataclass
class SystemPrimeFluidicsRequest:
    primeCycles: int
    qsm1: SolvFlowRateAndCompositionMetadata


def generate_default_prime_fluidics_request():
    payload = SystemPrimeFluidicsRequest(
        primeCycles=5,
        qsm1=SolvFlowRateAndCompositionMetadata(
            flowRateTargetMlPerMin=1.0,
            solventAPct=100.0,
            solventBPct=0.0,
            solventCPct=0.0,
            solventDPct=0.0
        )
    )
    return payload

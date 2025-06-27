"""
Desc: This file contains the payload that needs to be sent with a prime pump request
"""
from dataclasses import dataclass
from enum import Enum
from typing import List

from isym_test_api.rest_api.api.behavior.metering_pump_leak.metering_pump_leak_request import SolvFlowRateAndCompositionW


class PrimeType(Enum):
    PrimeType_ILLEGAL = 0
    PrimeType_BYLINE = 1
    PrimeType_BYCOMPOSITION = 2
    PrimeType_EQUILIBRATE = 3


@dataclass
class QsmRepeatPrimeStep:
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float
    primeDurationMin: float
    flowRateMlPerMin: float
    primeType: PrimeType



@dataclass
class QsmMetaPrimePump:
    steps: List[QsmRepeatPrimeStep]
    finalConditions: SolvFlowRateAndCompositionW


def generate_default_prime_pump_request():
    payload = QsmMetaPrimePump(
        steps=[
            QsmRepeatPrimeStep(
                solventAPct=100.0,
                solventBPct=0.0,
                solventCPct=0.0,
                solventDPct=0.0,
                primeDurationMin=2.0,
                flowRateMlPerMin=10.0,
                primeType=PrimeType.PrimeType_BYLINE
            )
        ],
        finalConditions=SolvFlowRateAndCompositionW(
            flowRateTargetMlPerMin=1.0,
            solventAPct=100.0,
            solventBPct=0.0,
            solventCPct=0.0,
            solventDPct=0.0
        )
    )
    return payload

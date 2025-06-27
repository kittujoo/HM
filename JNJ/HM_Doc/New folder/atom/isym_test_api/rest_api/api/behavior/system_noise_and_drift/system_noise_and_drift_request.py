"""
Desc: This file contains the payload that needs to be send with an method request
"""
from dataclasses import dataclass
from enum import Enum


class FilterBehavior(Enum):
    FilterBehavior_ILLEGAL = 0
    FilterBehavior_NOOPERATIONFILTER = 1
    FilterBehavior_LEGACYHAMMINGFILTER = 2


@dataclass
class TuvFilterBehavior:
    filterBehavior: FilterBehavior


class DataRate(Enum):
    DataRate_ILLEGAL = 0
    DataRate_1HZ = 1
    DataRate_2HZ = 2
    DataRate_5HZ = 5
    DataRate_10HZ = 10
    DataRate_20HZ = 20
    DataRate_40HZ = 40
    DataRate_80HZ = 80
    DataRate_160HZ = 160


@dataclass
class TuvFilterParameters:
    dataRateHz: DataRate
    filterTimeConstantSec: float


@dataclass
class TuvNoiseAndDrift:
    wavelengthA: float
    filterParameters: TuvFilterParameters
    filterBehavior: TuvFilterBehavior


@dataclass
class SolvFlowRateAndCompositionW:
    flowRateTargetMlPerMin: float
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float


@dataclass
class SystemTuvNoiseAndDriftRequest:
    qsm1: SolvFlowRateAndCompositionW
    tuv1: TuvNoiseAndDrift


def generate_default_system_tuv_noid_and_drift_request():
    payload = SystemTuvNoiseAndDriftRequest(
        qsm1=SolvFlowRateAndCompositionW(
            flowRateTargetMlPerMin=1.0,
            solventAPct=100.0,
            solventBPct=0.0,
            solventCPct=0.0,
            solventDPct=0.0,
        ),
        tuv1=TuvNoiseAndDrift(
            wavelengthA=190.0,
            filterParameters=TuvFilterParameters(
                dataRateHz=DataRate.DataRate_10HZ.name,
                filterTimeConstantSec=0.2,
            ),
            filterBehavior=TuvFilterBehavior(
                filterBehavior=FilterBehavior.FilterBehavior_NOOPERATIONFILTER.name
            )
        )
    )
    return payload

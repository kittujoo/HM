from dataclasses import dataclass


@dataclass
class SolvFlowRateAndCompositionW:
    flowRateTargetMlPerMin: float
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float


@dataclass
class MeteringPumpLeakStoreResponse:
    includePrime: bool
    qsm1: SolvFlowRateAndCompositionW
    targetPressurePsi: float
    dataModelType: str
    dataModelVersion: int

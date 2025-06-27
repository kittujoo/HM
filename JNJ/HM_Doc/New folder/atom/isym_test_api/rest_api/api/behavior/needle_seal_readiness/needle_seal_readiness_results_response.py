from dataclasses import dataclass


@dataclass
class SolvFlowRateAndCompositionW:
    flowRateTargetMlPerMin: float
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float


@dataclass
class NeedleSealReadinessResultResponse:
    result: str
    pressureDifferencePsi: float
    flowSettings: SolvFlowRateAndCompositionW
    dataModelType: str
    dataModelVersion: int

from dataclasses import dataclass


@dataclass
class MeteringPumpLeakResultResponse:
    volumeCompressionul: float
    leakRateulPerMin: float
    leakTestPassed: bool
    dataModelType: str
    dataModelVersion: int

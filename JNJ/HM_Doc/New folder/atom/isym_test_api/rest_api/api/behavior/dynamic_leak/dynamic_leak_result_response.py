from dataclasses import dataclass
from typing import List


@dataclass
class LeakStatus:
    leakRate: int
    plungerSelection: str
    compressResult: str
    monitorResult: str
    compressAttempts: int
    pressureMaxPsi: int
    strokeForCompressPct: int
    volumeForCompressMl: float
    leakTestPassed: bool


@dataclass
class DynamicLeakResultResponse:
    results: List[LeakStatus]
    dataModelType: str
    dataModelVersion: int

from dataclasses import dataclass
from typing import List, Any


@dataclass
class OperationStatus:
    state: str
    name: str
    resourceKey: str
    resourceText: str
    hasTimeRemainingSec: bool
    timeRemainingSec: int
    hasPercentageComplete: bool
    percentComplete: int


@dataclass
class MeteringPumpLeakStatusResponse:
    state: str
    category: str
    instanceId: str
    uniqueName: str
    status: str
    progress: List[Any]
    operationStatus: List[OperationStatus]
    resourceKey: str
    resourceText: str
    dataModelType: str
    dataModelVersion: int

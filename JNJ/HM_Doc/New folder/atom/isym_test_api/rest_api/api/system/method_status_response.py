from dataclasses import dataclass
from typing import List, Dict


@dataclass
class MethodStatusResponse:
    state: str
    category: str
    instanceId: str
    uniqueName: str
    status: str
    progress: List[Dict]
    operationStatus: List[Dict]
    resourceKey: str
    resourceText: str
    dataModelType: str
    dataModelVersion: int

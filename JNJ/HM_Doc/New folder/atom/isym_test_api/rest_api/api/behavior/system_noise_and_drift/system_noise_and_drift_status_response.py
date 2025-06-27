from dataclasses import dataclass


@dataclass
class SystemNoiseAndDriftStatusResponse:
    state: str
    category: str
    instanceId: str
    uniqueName: str
    status: str
    progress: list
    operationStatus: list
    resourceKey: str
    resourceText: str
    dataModelType: str
    dataModelVersion: int

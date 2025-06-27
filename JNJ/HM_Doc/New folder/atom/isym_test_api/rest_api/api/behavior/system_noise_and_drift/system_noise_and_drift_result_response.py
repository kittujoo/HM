from dataclasses import dataclass


@dataclass
class SystemNoiseAndDriftResultResponse:
    drift: float
    noise: float
    dataModelType: str
    dataModelVersion: int

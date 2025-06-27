from dataclasses import dataclass


@dataclass
class AmbientTemperatureResponse:
    currentAmbientTemperatureDegC: float
    dataModelType: str
    dataModelVersion: int

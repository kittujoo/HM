from dataclasses import dataclass


@dataclass
class ExclusiveModeResponse:
    exclusiveMode: bool
    owner: str
    dataModelType: str
    dataModelVersion: int

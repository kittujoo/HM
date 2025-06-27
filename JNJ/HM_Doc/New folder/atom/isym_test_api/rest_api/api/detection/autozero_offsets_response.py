from dataclasses import dataclass


@dataclass
class TuvAutoZeroOffsets:
    # The auto zero offset for wavelength A
    autoZeroOffsetA: float
    autoZeroOffsetB: float
    dataModelType: str
    dataModelVersion: int

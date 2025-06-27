from enum import Enum
from dataclasses import dataclass


class SolventLine(Enum):
    SolventLine_ILLEGAL = 0  # Uninitialized
    SolventLine_A = 1  # Solvent line A
    SolventLine_B = 2  # Solvent line B
    SolventLine_C = 3  # Solvent line C
    SolventLine_D = 4  # Solvent line D
    SolventLine_N = 5  # Needle wash solvent line
    SolventLine_S = 6  # Seal wash solvent line


@dataclass
class SystemLeakTest:
    # Whether to test the accumulator for leaks
    testAccumulator: bool = True
    # Target pressure for accumulator test
    accumulatorTargetPressurePsi: float = 9500.0
    # Whether to test the primary for leaks
    testPrimary: bool = True
    # Target pressure for primary test
    primaryTargetPressurePsi: float = 7500.0
    # Which solvent line to use
    solventLine: SolventLine = SolventLine.SolventLine_A
    # Whether to perform a quick prime on the solvent line
    includePrime: bool = True
    # Whether to include the needle and seal in the leak test
    includeNeedleAndSeal: bool = True
    # Whether to include the column in the leak test
    includeColumn: bool = True

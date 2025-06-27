from dataclasses import dataclass


@dataclass
class StartColumnRequest:
    runTimeMin: float = 1.0

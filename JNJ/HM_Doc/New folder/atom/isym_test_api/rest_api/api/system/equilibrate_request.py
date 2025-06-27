from dataclasses import dataclass

@dataclass
class StartEquilibratingRequest():
    runTimeMin: float


def generate_default_equilibrating_request():
    payload = (StartEquilibratingRequest(
        runTimeMin=1.0,
    )
    )
    return payload

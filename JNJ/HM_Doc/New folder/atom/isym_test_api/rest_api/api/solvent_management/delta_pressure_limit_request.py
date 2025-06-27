"""
Desc: This file contains the payload for delta pressure limit request/response
"""
from dataclasses import dataclass


@dataclass
class QsmDeltaPressureLimit:
    deltaPressureLimitPsi: float


def generate_delta_pressure_limit_request(delta_pressure_limit: float = 5.0):
    payload = QsmDeltaPressureLimit(
            deltaPressureLimitPsi=delta_pressure_limit
    )
    return payload

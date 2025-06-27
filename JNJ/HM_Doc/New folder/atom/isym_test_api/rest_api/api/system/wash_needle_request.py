from dataclasses import dataclass


@dataclass
class WashNeedleRequest:
    primeCycles: int


def generate_default_system_wash_needle():
    payload = WashNeedleRequest(
        primeCycles=10)
    return payload

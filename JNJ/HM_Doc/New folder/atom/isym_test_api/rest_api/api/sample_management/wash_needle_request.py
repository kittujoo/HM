"""
Desc: This file contains the payload that needs to be sent with a wash needle request
"""
from dataclasses import dataclass


@dataclass
class FTNWashNeedleRequest:
    # The requested wash duration
    washDurationSec: int = 10


@dataclass
class FTNWashNeedlePrimeCycleRequest:
    # The requested prime cycle
    primeCycles: int = 10


def generate_default_wash_needle_request():
    # Function to generate default wash needle wash duration payload
    return FTNWashNeedleRequest()


def generate_default_prime_cycle_request():
    # Function to generate default wash needle prime cycle payload
    return FTNWashNeedlePrimeCycleRequest()

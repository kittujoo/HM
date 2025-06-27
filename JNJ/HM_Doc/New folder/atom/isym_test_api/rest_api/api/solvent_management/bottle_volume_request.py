"""
Desc: This file contains the payload that needs to be sent with a bottle volume request
"""
from dataclasses import dataclass
from typing import List


@dataclass
class SolventBottleInfo:
    id: str
    volumeMl: int


@dataclass
class SolventBottleVolume:
    solventBottleVolume: List[SolventBottleInfo]


def generate_bottle_volume_request():
    payload = SolventBottleVolume(
        solventBottleVolume=[
            SolventBottleInfo(
                id="",
                volumeMl=1000
            )
        ]
    )

    return payload


def generate_bottle_volume_non_default_request():
    payload = SolventBottleVolume(
        solventBottleVolume=[
            SolventBottleInfo(
                id="A",
                volumeMl=5000
            )
        ]
    )

    return payload

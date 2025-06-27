"""
Desc: This file contains the payload and data model that needs to be send and received with System Sample Queue request
"""
from dataclasses import dataclass
from typing import List


@dataclass
class SystemRepeatSampleInjection:
    injections: int
    sampleLocation: str
    sampleVolumeUl: float


@dataclass
class SystemSampleQueue:
    sampleInjections: List[SystemRepeatSampleInjection]
    samplesRemainingInSampleSet: int
    samplesRemainingInQueue: int
    injectionsRemainingInSampleSet: int
    injectionsRemainingInQueue: int
    additionalInfo: bool
    timeRemainingInSampleSet: float
    timeRemainingInQueue: float
    injectionsCompletedInQueue: int


def generate_default_set_system_sample_queue_request():
    payload = SystemSampleQueue(
        sampleInjections=[
            SystemRepeatSampleInjection(
                injections=2,
                sampleLocation="1:A,1",
                sampleVolumeUl=0.1
            )
        ],
        samplesRemainingInSampleSet=2,
        samplesRemainingInQueue=5,
        injectionsRemainingInSampleSet=1,
        injectionsRemainingInQueue=1,
        additionalInfo=False,
        timeRemainingInSampleSet=0.0,
        timeRemainingInQueue=0.0,
        injectionsCompletedInQueue=2,
    )
    return payload

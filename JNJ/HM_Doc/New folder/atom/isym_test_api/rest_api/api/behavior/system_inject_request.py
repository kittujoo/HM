"""
Desc: This file contains the payload that needs to be sent with a post method request
"""
from dataclasses import dataclass


@dataclass
class SystemInjectMetadataRequest:
    sampleLocation: str
    sampleVolumeUl: float
    runTimeMin: float
    includeSampleInfo: bool
    sampleName: str
    currentReplicate: int
    totalReplicates: int


def generate_default_system_injection():
    payload = SystemInjectMetadataRequest(
        sampleLocation="A1",
        sampleVolumeUl=2.0,
        runTimeMin=1.0,
        includeSampleInfo=False,
        sampleName="Sample",
        currentReplicate=1,
        totalReplicates=1)
    return payload

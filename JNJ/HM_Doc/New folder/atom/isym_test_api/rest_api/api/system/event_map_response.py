"""
Desc: This file contains the response received as an Event List
"""
from dataclasses import dataclass
from typing import List


@dataclass
class EventDict:
    publicTopic: str
    internalTopic: str


@dataclass
class EventMap:
    events: List[EventDict]
    dataModelType: str
    dataModelVersion: int

"""
Desc: This file contains the response received as a behavior status
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List

from marshmallow import fields


class BehaviorState(Enum):
    BehaviorState_ILLEGAL = 0  # Uninitialized
    BehaviorState_INACTIVE = 1  # Inactive
    BehaviorState_INITIATED = 2  # Initiated
    BehaviorState_SUBMITTED = 3  # Submitted
    BehaviorState_ACTIVE = 4  # Active
    BehaviorState_INTERRUPTED = 5  # Interrupted
    BehaviorState_COMPLETE = 6  # Complete
    BehaviorState_ABORTING = 7  # Aborting
    BehaviorState_ABORTED = 8  # Aborted
    BehaviorState_TERMINATED = 9  # Terminated


class BehaviorGroup(Enum):
    BehaviorGroup_ILLEGAL = 0  # Uninitialized
    BehaviorGroup_SETUP = 1  # Setup
    BehaviorGroup_MAINTENANCE = 2  # Maintenance
    BehaviorGroup_DIAGNOSTIC = 3  # Diagnostic
    BehaviorGroup_ISSUERESPONSE = 4  # Issue response


@dataclass
class TimeRemaining:
    # Value is not changing
    paused: bool = True

    # The current value, if available
    value: float = 0.0


@dataclass
class PercentCounter:
    # Value is not changing
    paused: bool = True

    # The current value, if available
    value: float = 0.0


@dataclass
class SystemRepeatProgressMessage:
    key: str = ""
    _str: str = fields.String(data_key="str", dump_default="")


@dataclass
class SystemRepeatChildOperationStatus:
    # The behavior state
    state: BehaviorState = BehaviorState.BehaviorState_ILLEGAL

    # The operation name
    name: str = ""

    # The operation resource key
    resourceKey: str = ""

    # Resource text in English
    resourceText: str = ""

    # Whether timeRemainingSec is used
    hasTimeRemainingSec: bool = False

    # TODO: An optional countdown of time remaining to completion
    timeRemainingSec: int = 0

    # Whether percentComplete is used
    hasPercentageComplete: bool = False

    # The current value, if available
    percentComplete: int = 0


@dataclass
class BehaviorStatus:
    # The behavior state
    state: BehaviorState = BehaviorState.BehaviorState_ILLEGAL

    # The behavior group
    category: BehaviorGroup = BehaviorGroup.BehaviorGroup_ILLEGAL

    # The unique activity id, if running
    instanceId: str = ""

    # The unique name of the activity, whether running or not
    uniqueName: str = ""

    # TODO: Placeholder for runtime progress (etc?)
    status: str = ""

    # TODO: An optional countdown of time remaining to completion
    timeRemaining: TimeRemaining = field(default_factory=TimeRemaining, metadata={"allow_none": True})

    # TODO: An optional countup of percent completion
    percentComplete: PercentCounter = field(default_factory=PercentCounter, metadata={"allow_none": True})
    progress: List[SystemRepeatProgressMessage] = field(default_factory=list, metadata={"allow_none": True})
    operationStatus: List[SystemRepeatChildOperationStatus] = field(default_factory=list, metadata={"allow_none": True})

    # The operation resource key
    resourceKey: str = ""

    # Resource text in English
    resourceText: str = ""

"""
Desc: This file contains the payload that needs to be received with a TUV Lamp History
"""
from dataclasses import dataclass
from enum import Enum


class CounterType(Enum):
    # Zero value, required by proto3
    CounterType_ILLEGAL = 0

    # An integer counter
    CounterType_INT = 1

    # A 32-bit float counter
    CounterType_FLOAT = 2

    # An ISO-8601 date string
    CounterType_DATE = 3


@dataclass
class UsageCounterValue:
    # Indicates data type of the counter
    counterType: CounterType

    # The counter value as an integer
    valueInt: int

    # The counter value as a float
    valueFloat: float

    # The counter float value precision
    precision: int

    # The counter value as an ISO-8601 date string
    valueDate: str


@dataclass
class UsageCounter:
    # The registered counter name, i.e. the string representation of the enum value
    counterName: str

    # The registered source of the counter, e.g. Tuv#123456
    registrant: str

    # The resource id for localization of counter description
    labelKey: str

    # The raw English counter description to use if not localized
    labelText: str

    # The resource id for localization of counter units
    unitsKey: str

    # The raw English units text to use if not localized
    unitsText: str

    # The counter value as an integer, float or date
    counterValue: UsageCounterValue

    # Direction of change; if True, the counter decreases over time
    decrementing: bool

    # Indicates that the tracked counter is resettable by user
    resettable: bool

    # The threshold defined to elicit a WARNING health issue
    warningLimit: UsageCounterValue

    # If true, monitor will raise issue if warning threshold is crossed
    warningEnabled: bool

    # True if current value has crossed the warning threshold (enabled or not)
    warningThresholdMet: bool

    # The threshold defined to elicit an ERROR health issue
    errorLimit: UsageCounterValue

    # If true, monitor will raise issue if error threshold is crossed
    errorEnabled: bool

    # True if current value has crossed the error threshold (enabled or not)
    errorThresholdMet: bool

    dataModelType: str
    dataModelVersion: int

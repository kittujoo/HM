from dataclasses import dataclass
from enum import Enum
from typing import List, Any, Dict


class DeviceType(Enum):
    DeviceType_GWY = "DeviceType_GWY",
    DeviceType_CHC = "DeviceType_CHC",
    DeviceType_FTN = "DeviceType_FTN",
    DeviceType_QSM = "DeviceType_QSM"
    DeviceType_TUV = "DeviceType_TUV"


class DeviceCategory(Enum):
    DeviceGroup_ACCESSORY = "DeviceGroup_ACCESSORY"
    DeviceGroup_COLUMN = "DeviceGroup_COLUMN"
    DeviceGroup_AUTOSAMPLER = "DeviceGroup_AUTOSAMPLER"
    DeviceGroup_PUMP = "DeviceGroup_PUMP"
    DeviceGroup_DETECTOR = "DeviceGroup_DETECTOR"


@dataclass
class SystemSettings:
    systemName: str
    dwellVolumeml: float
    tubingKit: str


@dataclass
class DeviceInfo:
    id: str
    deviceType: DeviceType
    category: DeviceCategory
    address: str
    serialNumber: str
    qualifierType: str
    qualifierData: str


@dataclass
class Device:
    role: str
    info: DeviceInfo


@dataclass
class System:
    devices: List[Device]
    triggerOwnerId: str
    validated: bool


@dataclass
class Wrapper:
    role: str
    payloadType: str
    data: Dict[str, Any]


@dataclass
class Config:
    wrappers: List[Wrapper]


@dataclass
class SystemConfigurationResponse:
    system: System
    config: Config
    softwareVersion: str
    serialNumber: str
    systemsettings: SystemSettings
    dataModelType: str
    dataModelVersion: int

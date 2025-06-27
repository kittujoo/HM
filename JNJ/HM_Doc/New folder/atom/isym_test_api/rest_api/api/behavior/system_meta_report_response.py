"""
Desc: This file contains the response received from a system meta report get request
"""
from dataclasses import dataclass
from enum import Enum
from typing import List
from typing import Optional


@dataclass
class QsmMetaPostRunReportMetadata:
    deviceType: str
    systemPressureAverage: float
    systemPressureMin: float
    systemPressureMax: float


@dataclass
class FtnMetaPostRunReportMetadata:
    deviceType: str
    extensionLoopVolume: float
    needleVolume: float
    sampleTemperatureAverage: float
    sampleTemperatureMin: float
    sampleTemperatureMax: float


@dataclass
class ChcMetaPostRunReportMetadata:
    deviceType: str
    columnTemperatureAverage: float
    columnTemperatureMin: float
    columnTemperatureMax: float
    columnTagScanned: bool
    columnType: str
    columnSerialNumber: str
    columnPartNumber: str
    columnGTIN: str


class SourceType(Enum):
    SourceType_ILLEGAL = 0
    SourceType_SYSTEM = 1
    SourceType_HEALTH = 2
    SourceType_GWY = 3
    SourceType_TUV = 4
    SourceType_QSM = 5
    SourceType_FTN = 6
    SourceType_CHC = 7


@dataclass
class EventCategory(Enum):
    EventCategory_ILLEGAL = 0
    EventCategory_NONSPECIFIC = 1
    EventCategory_DEVICE = 2
    EventCategory_CONFIGURATION = 3
    EventCategory_HEALTH = 4
    EventCategory_QUALIFICATION = 5
    EventCategory_MAINTENANCE = 6
    EventCategory_CALIBRATION = 7
    EventCategory_OPERATION = 8
    EventCategory_SECURITY = 9
    EventCategory_MANAGEMENT = 10
    EventCategory_CLIENT = 11
    EventCategory_USER = 12


@dataclass
class IssueGroup(Enum):
    IssueGroup_ILLEGAL = 0
    IssueGroup_UNASSIGNED = 1
    IssueGroup_QUALIFICATION = 2
    IssueGroup_MAINTENANCE = 3
    IssueGroup_LEAK = 4
    IssueGroup_SENSOR = 5
    IssueGroup_COMMUNICATION = 6
    IssueGroup_POWER = 7
    IssueGroup_ACTIVITY = 8
    IssueGroup_COLUMN = 9
    IssueGroup_SOLVENT = 10
    IssueGroup_CONSUMABLE = 11


class Severity(Enum):
    Severity_ILLEGAL = 0
    Severity_ERROR = 3
    Severity_WARNING = 4
    Severity_INFO = 5


class FlowCellType(Enum):
    FlowCellType_ILLEGAL = 0
    FlowCellType_UNPROGRAMMED = 1
    FlowCellType_LG = 2
    FlowCellType_TS = 3


@dataclass
class TuvMetaPostRunReportMetadata:
    deviceType: str
    lampOn: bool
    lampMinutes: float
    lampSerialNumber: str
    flowCellType: FlowCellType
    flowCellPathLength: float
    flowCellVolume: float
    flowCellSerialNumber: str
    flowCellPartNumber: str


@dataclass
class CommonMetaParameterMetadata:
    paramType: str
    paramData: str


@dataclass
class CommonMetaMessageArgsMetadata:
    params: List[CommonMetaParameterMetadata]


@dataclass
class CommonMetaMessageMetadata:
    resourceId: str
    fmt8bit: str
    source: str
    argList: Optional[CommonMetaMessageArgsMetadata]
    formatted: str


@dataclass
class EventDetailMetadata:
    payloadType: str
    data: str


@dataclass
class CommonMetaEventMetadata:
    id: int
    timestamp: str
    message: CommonMetaMessageMetadata
    context: str
    sourceType: SourceType
    category: EventCategory
    issueGroup: IssueGroup
    eventTag: str
    issueId: str
    auditable: bool
    severity: Severity
    detail: Optional[EventDetailMetadata]


@dataclass
class SystemMetaAlarmRecordListMetadata:
    alarm: List[CommonMetaEventMetadata]


@dataclass
class SystemMetaSampleSetPreRunChecksMetadata:
    mobilePhaseExpiration: bool
    qualExpiration: bool
    pmExpiration: bool
    columnPresent: bool
    columnType: bool
    platesPresent: bool
    plateTypes: bool
    vialsPresent: bool


@dataclass
class SystemMetaSampleSetRunChecksMetadata:
    mobilePhaseLevels: bool
    washSolventLevels: bool


@dataclass
class SystemMetaPostRunReportSettingsMetadata:
    dataModelRevision: int
    sampleSetPreRunChecks: SystemMetaSampleSetPreRunChecksMetadata
    sampleSetRunChecks: SystemMetaSampleSetRunChecksMetadata


@dataclass
class SystemMetaPostRunReportMetadata:
    dataModelRevision: int
    systemSerialNumber: str
    systemSoftwareVersion: str
    acquisitionStartTime: str
    acquisitionEndTime: str
    qsm1: QsmMetaPostRunReportMetadata
    ftn1: FtnMetaPostRunReportMetadata
    chc1: ChcMetaPostRunReportMetadata
    tuv1: TuvMetaPostRunReportMetadata
    alarms: SystemMetaAlarmRecordListMetadata
    settings: SystemMetaPostRunReportSettingsMetadata


class ReportType(Enum):
    ReportType_ILLEGAL = 0
    ReportType_PostRun = 1


@dataclass
class SystemMetaReportHeaderMetadata:
    dataModelRevision: int
    reportType: ReportType


class ConfigDeviceType(Enum):
    ConfigDeviceType_ILLEGAL = 0
    ConfigDeviceType_QSM = 1
    ConfigDeviceType_FTN = 2
    ConfigDeviceType_CHC = 3
    ConfigDeviceType_TUV = 4


@dataclass
class SystemRepeatDeviceConfigWrapperMetadata:
    module: str
    deviceType: ConfigDeviceType
    config: str


class TubingKit(Enum):
    TubingKit_ILLEGAL = 0
    TubingKit_Standard = 1
    TubingKit_HighFlow = 2


@dataclass
class SystemSettingsMetadata:
    dwellVolumeml: float
    tubingKit: TubingKit


@dataclass
class SystemMetaConfigurationMetadata:
    modules: SystemRepeatDeviceConfigWrapperMetadata
    softwareVersion: str
    serialNumber: str
    system: SystemSettingsMetadata


@dataclass
class SystemMetaReportResponse:
    dataModelRevision: int
    systemReportHeader: SystemMetaReportHeaderMetadata = None
    postRun: SystemMetaPostRunReportMetadata = None
    systemConfiguration: SystemMetaConfigurationMetadata = None

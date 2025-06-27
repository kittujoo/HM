"""
Desc: This file contains the payload that needs to be sent with a method request
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Any


class MethodType(Enum):
    MethodType_ILLEGAL = 0
    MethodType_Acquisition = 1
    MethodType_Startup = 2
    MethodType_Shutdown = 3


@dataclass
class GwyMetaDiagChannels:
    ambientTemperatureChannelEnable: bool


@dataclass
class GwyMetaAcquisitionMethod:
    deviceType: str
    diagChannels: GwyMetaDiagChannels


@dataclass
class QsmMetaDiagChannels:
    compositionAChannelEnable: bool
    compositionBChannelEnable: bool
    compositionCChannelEnable: bool
    compositionDChannelEnable: bool
    flowRateChannelEnable: bool
    systemPressureChannelEnable: bool
    degasserPressureChannelEnable: bool
    accumulatorPressureChannelEnable: bool
    primaryPressureChannelEnable: bool


class GradientStartInjectionOffsetType(Enum):
    GradientStartInjectionOffsetType_ILLEGAL = 0
    GradientStartInjectionOffsetType_ATINJECTION = 1
    GradientStartInjectionOffsetType_BEFOREINJECTION = 2
    GradientStartInjectionOffsetType_AFTERINJECTION = 3


class GradientCurve(Enum):
    GradientCurve_ILLEGAL = 0
    GradientCurve_CURVE1 = 1
    GradientCurve_CURVE2 = 2
    GradientCurve_CURVE3 = 3
    GradientCurve_CURVE4 = 4
    GradientCurve_CURVE5 = 5
    GradientCurve_CURVE6 = 6
    GradientCurve_CURVE7 = 7
    GradientCurve_CURVE8 = 8
    GradientCurve_CURVE9 = 9
    GradientCurve_CURVE10 = 10
    GradientCurve_CURVE11 = 11


@dataclass
class QsmRepeatGradientSegment:
    timeMin: float
    flowRateMlPerMin: float
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float
    curve: GradientCurve


@dataclass
class QsmGradientTable:
    offsetType: GradientStartInjectionOffsetType
    offsetVolumeUl: float
    segments: List[QsmRepeatGradientSegment]


@dataclass
class QsmPressureLimit:
    lowPressureLimitPsi: float
    highPressureLimitPsi: float


@dataclass
class SolventType:
    id: str = ""
    name: str = ""


@dataclass
class QsmMetaSolvents:
    solventLineA: SolventType
    solventLineB: SolventType
    solventLineC: SolventType
    solventLineD: SolventType


@dataclass
class QsmStrokeVolume:
    strokeVolumeUL: float


@dataclass
class QsmMetaAcquisitionMethod:
    deviceType: str
    diagChannels: QsmMetaDiagChannels
    flowRampPeriodMin: float
    gradient: QsmGradientTable
    pressureLimits: QsmPressureLimit
    solvents: QsmMetaSolvents
    sealWashPeriodMin: float
    strokeVolume: QsmStrokeVolume


@dataclass
class FtnMetaDiagChannels:
    samplePressureChannelEnable: bool
    sampleTemperatureChannelEnable: bool


@dataclass
class FtnSampleTemperatureW:
    targetTemperatureDegC: float


@dataclass
class SampSampleTemperatureW:
    sampleTemperature: FtnSampleTemperatureW
    temperatureControlled: bool


@dataclass
class FtnMetaSolvents:
    needleWashSolvent: SolventType
    sealWashSolvent: SolventType


@dataclass
class FtnMetaAcquisitionMethod:
    deviceType: str
    diagChannels: FtnMetaDiagChannels
    needleWashSec: float
    drawRateULPerMin: float
    aspirationDistanceFromSampleLocationBottomMM: float
    vialAndWellBottomSense: bool
    sampleTemperature: SampSampleTemperatureW
    sampleTemperatureThresholdEnable: bool
    sampleTemperatureThresholdDegC: float
    solvents: FtnMetaSolvents


class WavelengthMode(Enum):
    WavelengthMode_ILLEGAL = 0
    WavelengthMode_SINGLE = 1
    WavelengthMode_DUAL = 2


class DataRate(Enum):
    DataRate_ILLEGAL = 0
    DataRate_1HZ = 1
    DataRate_2HZ = 2
    DataRate_5HZ = 5
    DataRate_10HZ = 10
    DataRate_20HZ = 20
    DataRate_40HZ = 40
    DataRate_80HZ = 80
    DataRate_160HZ = 160


@dataclass
class TuvFilterParameters:
    dataRateHz: DataRate
    filterTimeConstantSec: float


class AutoZeroBehavior(Enum):
    AutoZeroBehavior_ILLEGAL = 0
    AutoZeroBehavior_NOOPERATIONAUTOZERO = 1
    AutoZeroBehavior_OFFSETTOZERO = 2
    AutoZeroBehavior_MAINTAINBASELINE = 3


class FilterBehavior(Enum):
    FilterBehavior_ILLEGAL = 0
    FilterBehavior_NOOPERATIONFILTER = 1
    FilterBehavior_LEGACYHAMMINGFILTER = 2


@dataclass
class TuvDataProcessingBehaviors:
    autoZeroOnInjectStart: bool
    autoZeroOnWavelengthChange: AutoZeroBehavior
    filterBehavior: FilterBehavior


class EventType(Enum):
    EventType_ILLEGAL = 0
    EventType_AUTOZERO = 1
    EventType_WAVELENGTHA = 2
    EventType_WAVELENGTHB = 3
    EventType_LAMP = 4


@dataclass
class TuvRepeatTimedEvent:
    timeMin: float
    eventType: EventType
    parameter1: float


@dataclass
class TuvTimedEvents:
    events: List[Any]


@dataclass
class TuvDataAcquisitionSettings:
    wavelengthMode: WavelengthMode
    wavelengthA: float
    wavelengthB: float
    filterParameters: TuvFilterParameters
    dataProcessingBehaviors: TuvDataProcessingBehaviors
    timedEvents: TuvTimedEvents = field(default_factory=TuvTimedEvents)


@dataclass
class DetLampW:
    lampOn: bool


@dataclass
class TuvMetaAcquisitionMethod:
    deviceType: str
    dataAcquisitionSettings: TuvDataAcquisitionSettings
    lampOn: DetLampW


@dataclass
class ChcMetaDiagChannels:
    columnTemperatureChannelEnable: bool


@dataclass
class ChcColumnTemperatureW:
    targetTemperatureDegC: float


@dataclass
class SepColumnTemperatureW:
    columnTemperature: ChcColumnTemperatureW
    temperatureControlled: bool


@dataclass
class ColumnType:
    id: str
    name: str


@dataclass
class ChcMetaAcquisitionMethod:
    deviceType: str
    diagChannels: ChcMetaDiagChannels
    columnTemperature: SepColumnTemperatureW
    columnTemperatureThresholdEnable: bool
    columnTemperatureThresholdDegC: float
    columnType: ColumnType


@dataclass
class SystemMetaAcquisitionMethod:
    gwy: GwyMetaAcquisitionMethod
    qsm1: QsmMetaAcquisitionMethod
    ftn1: FtnMetaAcquisitionMethod
    tuv1: TuvMetaAcquisitionMethod
    chc1: ChcMetaAcquisitionMethod


@dataclass
class SystemMetaMethodHeader:
    dataModelRevision: int
    methodType: MethodType
    comment: str


@dataclass
class SystemMetaMethodRequest:
    systemMethodHeader: SystemMetaMethodHeader
    methodName: str
    acquisition: SystemMetaAcquisitionMethod


def generate_default_system_meta_method_request():
    payload = SystemMetaMethodRequest(
        systemMethodHeader=SystemMetaMethodHeader(
            dataModelRevision=1,
            methodType=MethodType.MethodType_Acquisition,
            comment=""
        ),
        methodName="",
        acquisition=SystemMetaAcquisitionMethod(
            gwy=GwyMetaAcquisitionMethod(
                deviceType="Gwy",
                diagChannels=GwyMetaDiagChannels(
                    ambientTemperatureChannelEnable=False
                )
            ),
            qsm1=QsmMetaAcquisitionMethod(
                deviceType="Qsm",
                diagChannels=QsmMetaDiagChannels(
                    compositionAChannelEnable=False,
                    compositionBChannelEnable=False,
                    compositionCChannelEnable=False,
                    compositionDChannelEnable=False,
                    flowRateChannelEnable=False,
                    systemPressureChannelEnable=False,
                    degasserPressureChannelEnable=False,
                    accumulatorPressureChannelEnable=False,
                    primaryPressureChannelEnable=False
                ),
                flowRampPeriodMin=0.066667,
                gradient=QsmGradientTable(
                    offsetType=GradientStartInjectionOffsetType.GradientStartInjectionOffsetType_ATINJECTION,
                    offsetVolumeUl=0.0,
                    segments=[QsmRepeatGradientSegment(
                        timeMin=0.0,
                        flowRateMlPerMin=1.0,
                        solventAPct=100.0,
                        solventBPct=0.0,
                        solventCPct=0.0,
                        solventDPct=0.0,
                        curve=GradientCurve.GradientCurve_CURVE6
                    )]
                ),
                pressureLimits=QsmPressureLimit(
                    lowPressureLimitPsi=0.0,
                    highPressureLimitPsi=10000.0
                ),
                solvents=QsmMetaSolvents(
                    solventLineA=SolventType(id="", name=""),
                    solventLineB=SolventType(id="", name=""),
                    solventLineC=SolventType(id="", name=""),
                    solventLineD=SolventType(id="", name="")
                ),
                sealWashPeriodMin=5.0,
                strokeVolume=QsmStrokeVolume(
                    strokeVolumeUL=132.0
                )
            ),
            ftn1=FtnMetaAcquisitionMethod(
                deviceType="Ftn",
                diagChannels=FtnMetaDiagChannels(
                    samplePressureChannelEnable=False,
                    sampleTemperatureChannelEnable=False
                ),
                needleWashSec=6.0,
                drawRateULPerMin=100,
                aspirationDistanceFromSampleLocationBottomMM=4,
                vialAndWellBottomSense=False,
                sampleTemperature=SampSampleTemperatureW(
                    sampleTemperature=FtnSampleTemperatureW(targetTemperatureDegC=20.0),
                    temperatureControlled=False
                ),
                sampleTemperatureThresholdEnable=False,
                sampleTemperatureThresholdDegC=5.0,
                solvents=FtnMetaSolvents(
                    needleWashSolvent=SolventType(id="", name=""),
                    sealWashSolvent=SolventType(id="", name="")
                )
            ),
            tuv1=TuvMetaAcquisitionMethod(
                deviceType="Tuv",
                dataAcquisitionSettings=TuvDataAcquisitionSettings(
                    wavelengthMode=WavelengthMode.WavelengthMode_SINGLE,
                    wavelengthA=254.0,
                    wavelengthB=230.0,
                    filterParameters=TuvFilterParameters(
                        dataRateHz=DataRate.DataRate_10HZ,
                        filterTimeConstantSec=0.2,
                    ),
                    dataProcessingBehaviors=TuvDataProcessingBehaviors(
                        autoZeroOnInjectStart=True,
                        autoZeroOnWavelengthChange=AutoZeroBehavior.AutoZeroBehavior_MAINTAINBASELINE,
                        filterBehavior=FilterBehavior.FilterBehavior_NOOPERATIONFILTER
                    ),
                    timedEvents=TuvTimedEvents(events=[])
                ),
                lampOn=DetLampW(lampOn=True)
            ),
            chc1=ChcMetaAcquisitionMethod(
                deviceType="Chc",
                diagChannels=ChcMetaDiagChannels(
                    columnTemperatureChannelEnable=False
                ),
                columnTemperature=SepColumnTemperatureW(
                    columnTemperature=ChcColumnTemperatureW(
                        targetTemperatureDegC=30.0
                    ),
                    temperatureControlled=False
                ),
                columnTemperatureThresholdEnable=False,
                columnTemperatureThresholdDegC=5.0,
                columnType=ColumnType(id="00195008060078",
                                      name="XBridge BEH C18, 130A, 3.50um, 4.6mm X 50mm +eConnect")
            )
        )
    )
    return payload

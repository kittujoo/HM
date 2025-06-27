"""
Desc: This file contains the payload that needs to be sent with a meta setting request
"""
import json
from dataclasses import dataclass
from typing import List
from isym_test_api.rest_api.api.behavior.system_meta_method_request import (AutoZeroBehavior, ChcColumnTemperatureW, ChcMetaAcquisitionMethod,
                                                                            ChcMetaDiagChannels,
                                                                            ColumnType, DataRate, DetLampW, FilterBehavior, FtnMetaAcquisitionMethod,
                                                                            FtnMetaDiagChannels,
                                                                            FtnMetaSolvents, FtnSampleTemperatureW, GradientCurve, GwyMetaAcquisitionMethod,
                                                                            GwyMetaDiagChannels,
                                                                            QsmGradientTable, QsmMetaAcquisitionMethod, QsmMetaDiagChannels, QsmMetaSolvents,
                                                                            QsmPressureLimit,
                                                                            QsmRepeatGradientSegment, QsmStrokeVolume, SampSampleTemperatureW,
                                                                            SepColumnTemperatureW, SolventType,
                                                                            SystemMetaAcquisitionMethod, SystemMetaMethodHeader, TuvDataAcquisitionSettings,
                                                                            TuvDataProcessingBehaviors,
                                                                            TuvFilterParameters, TuvMetaAcquisitionMethod, TuvTimedEvents, WavelengthMode,
                                                                            MethodType, GradientStartInjectionOffsetType)


@dataclass
class Name:
    argName: str
    key: str


@dataclass
class Description:
    argName: str
    key: str


@dataclass
class Value:
    paramType: str
    paramData: str


@dataclass
class MetaSettingRequest:
    key: str
    source: str
    group: str
    scope: int
    name: Name
    description: Description
    value: Value


@dataclass
class SampleLine:
    lineNumber: int
    injections: int
    injectionVolumeUl: float
    sampleLocation: str
    methodName: str
    columnPosition: int
    runTimeMin: float
    methodParameters: str


@dataclass
class Method:
    systemMethodHeader: SystemMetaMethodHeader
    methodName: str
    acquisition: SystemMetaAcquisitionMethod


@dataclass
class InstrumentMethods:
    name: str
    method: Method


@dataclass
class PlateList:
    plateNumber: int
    plateName: str
    numberOfRows: int
    numberOfColumns: int
    coordinateOrder: str
    sequenceOrder: str
    sequenceType: str
    vialDepthMM: float
    vialDiameterMM: float
    rowSpacingMM: float
    columnSpacingMM: float
    topLeftVialXoffsetMM: float
    topLeftVialYoffsetMM: float
    plateDimensionXMM: float
    plateDimensionYMM: float
    plateDimensionZMM: float
    rowOffsetType: str
    rowOffsetMM: float
    columnOffsetType: str
    columnOffsetMM: float
    plateOrigin: str


@dataclass
class PlateConfiguration:
    plateList: List[PlateList]


@dataclass
class ValidateSampleSetRequest:
    sampleLine: List[SampleLine]
    instrumentMethods: List[InstrumentMethods]
    plateConfiguration: PlateConfiguration


def generate_prerun_checks_request(mobile_phase_expiration=False,
                                   qual_expiration=False,
                                   pm_expiration=False,
                                   column_present=False,
                                   column_type=False,
                                   plates_present=False,
                                   plate_types=False,
                                   vials_present=False):
    payload = MetaSettingRequest(
        key="cs_samplesetprerun_checks",
        source="",
        group="",
        scope=0,
        name=Name(
            argName="",
            key=""),
        description=Description(
            argName="",
            key=""
        ),
        value=Value(
            paramType="COMMONMETA_JSONPARAM",
            paramData=json.dumps(
                {
                    "payloadType": "SYSTEMMETA_SAMPLESETPRERUNCHECKS",
                    "property": {
                        "propertyType": "PropertyType_STRING",
                        "str": json.dumps(
                            {
                                "mobilePhaseExpiration": mobile_phase_expiration,
                                "qualExpiration": qual_expiration,
                                "pmExpiration": pm_expiration,
                                "columnPresent": column_present,
                                "columnType": column_type,
                                "platesPresent": plates_present,
                                "plateTypes": plate_types,
                                "vialsPresent": vials_present
                            })
                    }
                }
            )
        )
    )

    return payload


def generate_run_checks_request(mobile_phase_levels=False,
                                wash_solvent_levels=False):
    payload = MetaSettingRequest(
        key="cs_samplesetrun_checks",
        source="",
        group="",
        scope=0,
        name=Name(
            argName="",
            key=""),
        description=Description(
            argName="",
            key=""
        ),
        value=Value(
            paramType="COMMONMETA_JSONPARAM",
            paramData=json.dumps(
                {
                    "payloadType": "SYSTEMMETA_SAMPLESETRUNCHECKS",
                    "property": {
                        "propertyType": "PropertyType_STRING",
                        "str": json.dumps(
                            {
                                "mobilePhaseLevels": mobile_phase_levels,
                                "washSolventLevels": wash_solvent_levels,
                            })
                    }
                }
            )
        )
    )

    return payload


def generate_validate_sample_set_on_submit_request():
    payload = ValidateSampleSetRequest(
        sampleLine=[
            SampleLine(
                lineNumber=1,
                injections=1,
                injectionVolumeUl=1.0,
                sampleLocation="1:A,1",
                methodName="method1",
                columnPosition=1,
                runTimeMin=1.0,
                methodParameters=""
            ),
            SampleLine(
                lineNumber=2,
                injections=1,
                injectionVolumeUl=1.0,
                sampleLocation="2:B,2",
                methodName="method2",
                columnPosition=1,
                runTimeMin=1.0,
                methodParameters=""
            ),
            SampleLine(
                lineNumber=3,
                injections=1,
                injectionVolumeUl=1.0,
                sampleLocation="3:C,3",
                methodName="method3",
                columnPosition=1,
                runTimeMin=1.0,
                methodParameters=""
            )
        ],
        instrumentMethods=[
            InstrumentMethods(
                name="method1",
                method=Method(
                    systemMethodHeader=SystemMetaMethodHeader(
                        dataModelRevision=0,
                        methodType=MethodType.MethodType_Acquisition,
                        comment=""),
                    methodName="method1",
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
                                    curve=GradientCurve.GradientCurve_CURVE1
                                ),
                                    QsmRepeatGradientSegment(
                                        timeMin=1.0,
                                        flowRateMlPerMin=2.0,
                                        solventAPct=100.0,
                                        solventBPct=0.0,
                                        solventCPct=0.0,
                                        solventDPct=0.0,
                                        curve=GradientCurve.GradientCurve_CURVE6
                                    ),
                                    QsmRepeatGradientSegment(
                                        timeMin=2.0,
                                        flowRateMlPerMin=0.0,
                                        solventAPct=100.0,
                                        solventBPct=0.0,
                                        solventCPct=0.0,
                                        solventDPct=0.0,
                                        curve=GradientCurve.GradientCurve_CURVE6
                                    )
                                ]
                            ),
                            pressureLimits=QsmPressureLimit(
                                lowPressureLimitPsi=0.0,
                                highPressureLimitPsi=10000.0
                            ),
                            solvents=QsmMetaSolvents(
                                solventLineA=SolventType(),
                                solventLineB=SolventType(),
                                solventLineC=SolventType(),
                                solventLineD=SolventType()
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
                                sampleTemperature=FtnSampleTemperatureW(targetTemperatureDegC=10.0),
                                temperatureControlled=False
                            ),
                            sampleTemperatureThresholdEnable=False,
                            sampleTemperatureThresholdDegC=5.0,
                            solvents=FtnMetaSolvents(
                                needleWashSolvent=SolventType(),
                                sealWashSolvent=SolventType()
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
                                timedEvents=TuvTimedEvents([])
                            ),
                            lampOn=DetLampW(lampOn=True)
                        ),
                        chc1=ChcMetaAcquisitionMethod(
                            deviceType="Chc",
                            diagChannels=ChcMetaDiagChannels(
                                columnTemperatureChannelEnable=False
                            ),
                            columnTemperature=SepColumnTemperatureW(
                                columnTemperature=ChcColumnTemperatureW(targetTemperatureDegC=30.0),
                                temperatureControlled=False
                            ),
                            columnTemperatureThresholdEnable=False,
                            columnTemperatureThresholdDegC=5.0,
                            columnType=ColumnType(id="", name="")
                        )
                    )
                )
            ),
            InstrumentMethods(
                name="method2",
                method=Method(
                    systemMethodHeader=SystemMetaMethodHeader(
                        dataModelRevision=0,
                        methodType=MethodType.MethodType_Acquisition,
                        comment=""),
                    methodName="method2",
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
                                    flowRateMlPerMin=0.0,
                                    solventAPct=100.0,
                                    solventBPct=0.0,
                                    solventCPct=0.0,
                                    solventDPct=0.0,
                                    curve=GradientCurve.GradientCurve_CURVE1
                                )]
                            ),
                            pressureLimits=QsmPressureLimit(
                                lowPressureLimitPsi=0.0,
                                highPressureLimitPsi=10000.0
                            ),
                            solvents=QsmMetaSolvents(
                                solventLineA=SolventType(),
                                solventLineB=SolventType(),
                                solventLineC=SolventType(),
                                solventLineD=SolventType()
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
                                sampleTemperature=FtnSampleTemperatureW(targetTemperatureDegC=10.0),
                                temperatureControlled=False
                            ),
                            sampleTemperatureThresholdEnable=False,
                            sampleTemperatureThresholdDegC=5.0,
                            solvents=FtnMetaSolvents(
                                needleWashSolvent=SolventType(),
                                sealWashSolvent=SolventType()
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
                                timedEvents=TuvTimedEvents([])
                            ),
                            lampOn=DetLampW(lampOn=True)
                        ),
                        chc1=ChcMetaAcquisitionMethod(
                            deviceType="Chc",
                            diagChannels=ChcMetaDiagChannels(
                                columnTemperatureChannelEnable=False
                            ),
                            columnTemperature=SepColumnTemperatureW(
                                columnTemperature=ChcColumnTemperatureW(targetTemperatureDegC=30.0),
                                temperatureControlled=False
                            ),
                            columnTemperatureThresholdEnable=False,
                            columnTemperatureThresholdDegC=5.0,
                            columnType=ColumnType(id="", name="")
                        )
                    )
                )
            ),
            InstrumentMethods(
                name="method3",
                method=Method(
                    systemMethodHeader=SystemMetaMethodHeader(
                        dataModelRevision=0,
                        methodType=MethodType.MethodType_Acquisition,
                        comment=""),
                    methodName="method3",
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
                                    curve=GradientCurve.GradientCurve_CURVE1
                                ),
                                    QsmRepeatGradientSegment(
                                        timeMin=1.0,
                                        flowRateMlPerMin=2.0,
                                        solventAPct=100.0,
                                        solventBPct=0.0,
                                        solventCPct=0.0,
                                        solventDPct=0.0,
                                        curve=GradientCurve.GradientCurve_CURVE6
                                    ),
                                    QsmRepeatGradientSegment(
                                        timeMin=2.0,
                                        flowRateMlPerMin=3.0,
                                        solventAPct=100.0,
                                        solventBPct=0.0,
                                        solventCPct=0.0,
                                        solventDPct=0.0,
                                        curve=GradientCurve.GradientCurve_CURVE6
                                    )
                                ]
                            ),
                            pressureLimits=QsmPressureLimit(
                                lowPressureLimitPsi=0.0,
                                highPressureLimitPsi=10000.0
                            ),
                            solvents=QsmMetaSolvents(
                                solventLineA=SolventType(),
                                solventLineB=SolventType(),
                                solventLineC=SolventType(),
                                solventLineD=SolventType()
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
                                sampleTemperature=FtnSampleTemperatureW(targetTemperatureDegC=10.0),
                                temperatureControlled=False
                            ),
                            sampleTemperatureThresholdEnable=False,
                            sampleTemperatureThresholdDegC=5.0,
                            solvents=FtnMetaSolvents(
                                needleWashSolvent=SolventType(),
                                sealWashSolvent=SolventType()
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
                                timedEvents=TuvTimedEvents([])
                            ),
                            lampOn=DetLampW(lampOn=True)
                        ),
                        chc1=ChcMetaAcquisitionMethod(
                            deviceType="Chc",
                            diagChannels=ChcMetaDiagChannels(
                                columnTemperatureChannelEnable=False
                            ),
                            columnTemperature=SepColumnTemperatureW(
                                columnTemperature=ChcColumnTemperatureW(targetTemperatureDegC=30.0),
                                temperatureControlled=False
                            ),
                            columnTemperatureThresholdEnable=False,
                            columnTemperatureThresholdDegC=5.0,
                            columnType=ColumnType(id="", name="")
                        )
                    )
                )
            )],
        plateConfiguration=PlateConfiguration([
            PlateList(
                plateNumber=1,
                plateName="",
                numberOfRows=6,
                numberOfColumns=8,
                coordinateOrder="RowColumnPriority_ROWFIRST",
                sequenceOrder="RowColumnPriority_ROWFIRST",
                sequenceType="SequenceType_DISCONTINUOUS",
                vialDepthMM=32.0,
                vialDiameterMM=10.0,
                rowSpacingMM=14.0,
                columnSpacingMM=14.0,
                topLeftVialXoffsetMM=15.0,
                topLeftVialYoffsetMM=8.3,
                plateDimensionXMM=128.0,
                plateDimensionYMM=86.0,
                plateDimensionZMM=38.3,
                rowOffsetType="OffsetType_NONE",
                rowOffsetMM=0.0,
                columnOffsetType="OffsetType_NONE",
                columnOffsetMM=0.0,
                plateOrigin="PlateOrigin_TOPLEFT"
            ),
            PlateList(
                plateNumber=2,
                plateName="",
                numberOfRows=6,
                numberOfColumns=8,
                coordinateOrder="RowColumnPriority_ROWFIRST",
                sequenceOrder="RowColumnPriority_ROWFIRST",
                sequenceType="SequenceType_DISCONTINUOUS",
                vialDepthMM=32.0,
                vialDiameterMM=10.0,
                rowSpacingMM=14.0,
                columnSpacingMM=14.0,
                topLeftVialXoffsetMM=15.0,
                topLeftVialYoffsetMM=8.3,
                plateDimensionXMM=128.0,
                plateDimensionYMM=86.0,
                plateDimensionZMM=38.3,
                rowOffsetType="OffsetType_NONE",
                rowOffsetMM=0.0,
                columnOffsetType="OffsetType_NONE",
                columnOffsetMM=0.0,
                plateOrigin="PlateOrigin_TOPLEFT"
            ),
            PlateList(
                plateNumber=3,
                plateName="",
                numberOfRows=6,
                numberOfColumns=8,
                coordinateOrder="RowColumnPriority_ROWFIRST",
                sequenceOrder="RowColumnPriority_ROWFIRST",
                sequenceType="SequenceType_DISCONTINUOUS",
                vialDepthMM=32.0,
                vialDiameterMM=10.0,
                rowSpacingMM=14.0,
                columnSpacingMM=14.0,
                topLeftVialXoffsetMM=15.0,
                topLeftVialYoffsetMM=8.3,
                plateDimensionXMM=128.0,
                plateDimensionYMM=86.0,
                plateDimensionZMM=38.3,
                rowOffsetType="OffsetType_NONE",
                rowOffsetMM=0.0,
                columnOffsetType="OffsetType_NONE",
                columnOffsetMM=0.0,
                plateOrigin="PlateOrigin_TOPLEFT"
            )
        ])
    )

    return payload

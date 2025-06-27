import os
import re

from glom import assign, delete, glom
from pathlib import Path
from pytest_bdd import scenarios, when
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.system_meta_method_request import (
    generate_default_system_meta_method_request, QsmRepeatGradientSegment,
    GradientCurve, GradientStartInjectionOffsetType, QsmMetaDiagChannels,
    QsmPressureLimit, QsmMetaSolvents, SolventType,
    GwyMetaAcquisitionMethod, GwyMetaDiagChannels, QsmMetaAcquisitionMethod,
    QsmGradientTable, QsmStrokeVolume, SystemMetaMethodHeader, MethodType,
    TuvMetaAcquisitionMethod, TuvDataAcquisitionSettings, WavelengthMode,
    TuvFilterParameters, DataRate, TuvDataProcessingBehaviors, AutoZeroBehavior,
    FilterBehavior, TuvTimedEvents, DetLampW, ChcMetaAcquisitionMethod,
    ChcMetaDiagChannels, SepColumnTemperatureW, ChcColumnTemperatureW, ColumnType,
    FtnMetaAcquisitionMethod, SampSampleTemperatureW, FtnMetaDiagChannels,
    FtnSampleTemperatureW, FtnMetaSolvents)
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from utilities.convertion_utilities import parse_string_to_obj
from utilities.datatables.headless_datatable import headlesstable
from utilities.datatables.vertical_list import verticallist
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_method_payload_validation.feature',
              '../features/isym_setmethod_test.feature')


@when('the gradient method data is sent with non default values')
def send_non_default_values(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = generate_default_system_meta_method_request()
    payload.systemMethodHeader = SystemMetaMethodHeader(
        dataModelRevision=1,
        methodType=MethodType.MethodType_Shutdown,
        comment="Testing"
    )
    payload.acquisition.gwy = GwyMetaAcquisitionMethod(
        deviceType="Gwy123",
        diagChannels=GwyMetaDiagChannels(
            ambientTemperatureChannelEnable=True
        )
    )
    payload.acquisition.qsm1 = QsmMetaAcquisitionMethod(
        deviceType="Qsm123",
        diagChannels=QsmMetaDiagChannels(
            compositionAChannelEnable=True,
            compositionBChannelEnable=True,
            compositionCChannelEnable=True,
            compositionDChannelEnable=True,
            flowRateChannelEnable=True,
            systemPressureChannelEnable=True,
            degasserPressureChannelEnable=True,
            accumulatorPressureChannelEnable=True,
            primaryPressureChannelEnable=True
        ),
        flowRampPeriodMin=0.4,
        gradient=QsmGradientTable(
            offsetType=GradientStartInjectionOffsetType.GradientStartInjectionOffsetType_BEFOREINJECTION,
            offsetVolumeUl=100.0,
            segments=[QsmRepeatGradientSegment(
                timeMin=500.0,
                flowRateMlPerMin=5.0,
                solventAPct=25.0,
                solventBPct=25.0,
                solventCPct=25.0,
                solventDPct=25.0,
                curve=GradientCurve.GradientCurve_CURVE2
            )]
        ),
        pressureLimits=QsmPressureLimit(
            lowPressureLimitPsi=4000.0,
            highPressureLimitPsi=7000.0
        ),
        solvents=QsmMetaSolvents(
            solventLineA=SolventType(id="solvent_12", name="SolventE"),
            solventLineB=SolventType(id="solvent_13", name="SolventF"),
            solventLineC=SolventType(id="solvent_14", name="SolventG"),
            solventLineD=SolventType(id="solvent_15", name="SolventH")
        ),
        sealWashPeriodMin=50.0,
        strokeVolume=QsmStrokeVolume(
            strokeVolumeUL=100.0
        )
    )
    payload.acquisition.tuv1 = TuvMetaAcquisitionMethod(
        deviceType="TuvTest",
        dataAcquisitionSettings=TuvDataAcquisitionSettings(
            wavelengthMode=WavelengthMode.WavelengthMode_SINGLE,
            wavelengthA=274.0,
            wavelengthB=210.0,
            filterParameters=TuvFilterParameters(
                dataRateHz=DataRate.DataRate_1HZ,
                filterTimeConstantSec=0.4,
            ),
            dataProcessingBehaviors=TuvDataProcessingBehaviors(
                autoZeroOnInjectStart=False,
                autoZeroOnWavelengthChange=AutoZeroBehavior.AutoZeroBehavior_MAINTAINBASELINE,
                filterBehavior=FilterBehavior.FilterBehavior_NOOPERATIONFILTER
            ),
            timedEvents=TuvTimedEvents(events=[])
        ),
        lampOn=DetLampW(lampOn=False)
    )
    payload.acquisition.chc1 = ChcMetaAcquisitionMethod(
        deviceType="Chc123",
        diagChannels=ChcMetaDiagChannels(
            columnTemperatureChannelEnable=True
        ),
        columnTemperature=SepColumnTemperatureW(
            columnTemperature=ChcColumnTemperatureW(
                targetTemperatureDegC=75.0
            ),
            temperatureControlled=True
        ),
        columnTemperatureThresholdEnable=True,
        columnTemperatureThresholdDegC=8.0,
        columnType=ColumnType(id="Column_Type",
                              name="Column_Value")
    )
    payload.acquisition.ftn1 = FtnMetaAcquisitionMethod(
        deviceType="Ftn_1",
        diagChannels=FtnMetaDiagChannels(
            samplePressureChannelEnable=True,
            sampleTemperatureChannelEnable=True
        ),
        needleWashSec=10.0,
        drawRateULPerMin=75.0,
        aspirationDistanceFromSampleLocationBottomMM=15,
        vialAndWellBottomSense=True,
        sampleTemperature=SampSampleTemperatureW(
            sampleTemperature=FtnSampleTemperatureW(targetTemperatureDegC=15.0),
            temperatureControlled=True
        ),
        sampleTemperatureThresholdEnable=True,
        sampleTemperatureThresholdDegC=3.0,
        solvents=FtnMetaSolvents(
            needleWashSolvent=SolventType(id="solvent_1", name="SolventA"),
            sealWashSolvent=SolventType(id="solvent_2", name="SolventB")
        )
    )
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload)


@when('the gradient method data is sent with new payload')
def send_custom_method_payload(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver, context):
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=context['payload'])


@when(headlesstable('the method data is sent with next properties:'))
def modify_solvent_property(context, table, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = as_dict(generate_default_system_meta_method_request())
    for prop, value in table.data:
        value = parse_string_to_obj(value)
        assign(payload, prop, value)
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload)


@when(verticallist('the method data is sent with missing properties:'))
def remove_segment_property(context, table, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = as_dict(generate_default_system_meta_method_request())
    for prop in table.data:
        delete(payload, prop)
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload)


@when('the incorrect method data is sent')
def request_method_invalid_payload(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = generate_default_system_meta_method_request()
    payload.systemMethodHeader.dataModelRevision = "test"
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload)


@when(cfparse('the gradient method data is sent with "{count:d}" segment data'))
def add_multiple_segments(context, count, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = as_dict(generate_default_system_meta_method_request())
    segments = glom(payload, "acquisition.qsm1.gradient.segments")
    segments.extend(segments * (count - 1))
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload)


@when(cfparse('the method data is sent with missing "{property_name}" property'))
def remove_property(context, property_name, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload_as_dict = as_dict(generate_default_system_meta_method_request())
    delete(payload_as_dict, property_name)
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload_as_dict)


@when('the method data is sent with "<property_name>" = "<value>" property')
@when(cfparse('the method data is sent with "{property_name}" = "{value}" property'))
def add_property(context, property_name, value, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    value = parse_string_to_obj(value)
    payload_as_dict = as_dict(generate_default_system_meta_method_request())
    if re.search(r"acquisition\.qsm1\.gradient\.segments\.(-?[0-9]+)\.flowRateMlPerMin", property_name) and isinstance(value, float) and value > 5.0:
        # if the flow rate goes more than 5.0 then the pressure should be decreased and the maximum allowed pressure should be 4000
        assign(payload_as_dict, "acquisition.qsm1.pressureLimits.highPressureLimitPsi", 4000.0)
    elif property_name == "acquisition.tuv1.dataAcquisitionSettings.wavelengthMode" and value == "WavelengthMode_DUAL":
        # The data rate depends on the wavelength mode. Default is 10Hz with a maximum of 160Hz and for DUAL mode should be a maximum of 2Hz.
        assign(payload_as_dict, "acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz", "DataRate_1HZ")
    assign(payload_as_dict, property_name, value)
    context['api_response'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=payload_as_dict)

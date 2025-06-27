"""
File_Name: logs.py
Desc: This file contains the constants used in Logs screen
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Harshita Raviraj" Initial Check-in 11/04/2023

"""
from selenium.webdriver.support.color import Color


class LogsScreenConstants:
    Category = "Information / maintenance"
    Source = "EventLoggerService"
    User = "USER"
    EventType = "AuditEventType_GENERIC"
    PageNumber = 'Page {} of '
    MaxCharAllowedLabel = '100/100 characters'
    SystemLeakTestSource = "SystemLeakTest"
    WorkFlowCategory = "operation"
    MaxChar = 100
    Red = Color(255, 82, 82, 1)


class NeedleSealLogConstants:
    Category = "Warning / operation"
    Source = "SystemNeedleSealReadiness"


class CalibrateWavelengthLogConstants:
    Category = "Information / operation"
    AbortCategory = "Warning / operation"
    Source = "TuvVerifyWavelengthCalibration"


class VerifyCalibrateWavelengthLogConstants:
    Category = "Information / operation"
    Source = "SystemTuvVerifyWavelengthCalibration"


class NoiseDriftConstants:
    Category = "Information / operation"
    AbortCategory = "Warning / operation"
    Source = "SystemTuvNoiseAndDrift"


class LogTableHeaders:
    date_and_time = "Date and Time"
    category = "Category"
    source = "Source"


class LogCategories:
    information_maintenance = "Information / maintenance"
    information_operation = "Information / operation"


class LogSources:
    errors = "Errors"
    service = "EventLoggerService"


class SampleTemperatureLogConstants:
    Category = "Information / operation"
    AbortCategory = "Warning / operation"
    Source = "FtnHeaterCoolerTest"


class CalibrateAxesLogConstants:
    Category = "Information / operation"
    ZSource = "FtnCalibrateNeedle"
    ZpSource = "FtnCalibrateTopOfPlateSensor"


class ColumnCompartmentTemperatureLogConstants:
    Category = "Information / operation"
    AbortCategory = "Warning / operation"
    Source = "ChcHeaterCoolerTest"



class SampleMeteringPumpLogConstants:
    Source = "SystemMeteringPumpLeakTest"
    WorkFlowCategory = "operation"
    WarningCategory = "Warning / operation"

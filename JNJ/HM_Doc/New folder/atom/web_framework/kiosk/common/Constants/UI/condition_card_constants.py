"""
File_Name: condition_card_constants.py
Desc: This file contains the constants of all the  condition cards
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 03/10/2020
__modified__ = "Sharmila vairamani" Added constants for title icon status and units- 09/03/2020
__modified__ = "Sharmila Vairamani" changed the  duration for max temperature  - 09/28/2020
__modified__ = "Sharmila Vairamani"  Added atrribute NoSetpointTemperatureMessage  - 09/28/2020
__modified__= "Sharmila Vairamani" Changed "FinalTitleIconColorCode" constant value - 02/26/2021
__modified__= "Sharmila Vairamani" Added "TemperatureUnits" constant value - 03/10/2021
--modified__ = "Sharmila Vairamani" Changed classname and TemperatureUnits - 04/05/2021
__modified__ = "Sharmila Vairamani" Added RoomTemperatureConditionCardConstants - 04/19/2021
__modified__ "sharmila Vairamani" Added TUVConditionCardConstants - 05/20/2021
__modified__ "sharmila Vairamani" Added min and max absorbance value - 05/26/2021
__modified__ "sharmila Vairamani" Added min and max FinalTitleIconColorCode value - 06/28/2021
__modified__ "Sharmila Vairamani" Added constants for the column card - 09/24/2021
__modified__ = "Tyler Prada" ambient temperature conversion - 10/1/21
__modified__= "Sharmila Vairamani" Added FlowConditionCardConstants - 03/23/2022
__modified__ = "Sharmila Vairamani" Added FlowConditionCardConstants 03/24/2022
__modified__ = "Tyler Prada" Added more mobile phase const 6/20/23
"""


class TemperatureConditionCardConstants:
    HeatingOnMessage = "HEATING IS ON"
    CoolingOnMessage = "COOLING IS ON"
    SetPointMessage = "SETPOINT REACHED"
    NoSetPointMessage = "NO SETPOINT"
    MaxTimeToReachTemperature = 1800
    FinalTitleIconColorCode = "195, 195, 195"
    CurrentTemperatureUnits = "Current (°C)"
    SetpointTemperatureUnits = "Setpoint (°C)"
    TitleIconWarmStatus = "ics-img-warm"
    TitleIconCoolStatus = "ics-img-cool"
    NoSetpointTemperatureMessage = "OFF"
    TemperatureUnits = "°C"
    SetpointTurnedOffMessage = "Setpoint off"


class ValvePositionConditionCardConstants:
    MaxValveWaitTime = 10
    valve_position_list = ["Inject", "Blocked", "Load" ]


class AmbientTemperatureConditionCardConstants:
    OutOfRangeMessage = "OUTSIDE OF OPERATING RANGE"
    NoTemperatureDetectedMessage = "Check Sensor"
    MaxTimeToReachTemperature = 60
    TitleIconTemperatureUnavailableStatus = "ics-img-temperature-unavailable"
    TitleIconTemperatureInRangeColorCode = "29, 233, 182, 1"
    TitleIconTemperatureOutOfRangeColorCode = "255, 234, 0"
    DefaultTemperature = "22.0 ± 5.0 °C"
    TemperatureUnits = "°C"
    InformationText = "Set the ambient temperature to what you have your lab temperature set as well as your tolerance for changes in this temperature."


class TUVConditionCardConstants:
    AbsorbanceUnits = "AU"
    WavelengthInUnits = "nm"
    NoAbsorbanceValue = "--"
    ChannelReadBackStatus = "LAMP IS OFF"
    # Absorbance range is -1.0000 AU to 4.0000 AU
    MinAbsorbanceValue = -1.0000
    MaxAbsorbanceValue = 4.0000
    ProgressBarLoadTime = 10


class ColumnConditionCardConstant:
    InjectionMonitorDisabledState = "Disabled"
    InformationText = "If you suspect the column information displayed is incorrect, then check the column installation and ensure that the column includes an eConnect tag. Only columns with eConnect tags are supported."
    InstructionHeader = "To re-read the eConnect tag:"
    FirstInstruction = "Open then close the compartment door, or"
    SecondInstruction = "With the door closed, tap the READ button."
    expected_instruction_text = [InstructionHeader, FirstInstruction, SecondInstruction]


class DeltaPressureConditionCardConstants:
    InRangeIndicatorMessage = "ready"
    OutOfRangeIndicatorMessage = "error"
    PressureUnits = "psi"
    DeltaPressurePerMinUnit = "psi, 1 min"
    DeltaPressureDisableColorCode = "117, 117, 117, 1"
    DeltaPressureOutOfRangeColorCode = "189, 67, 67, 1"
    DeltaPressureInRangeColorCode = "105, 240, 174, 1"


class SolventCompositionConditionCardConstants:
    SolventHintMessage = "0 to 100%"
    FlowHintMessage = "0.001 to 10.000 mL/min"
    EmptyEditFieldMessage = "This field is required"


class FlowConditionCardConstants:
    MaxTimeToachieveFlowRate = 60  # This needs to be verified
    OffReadbackMessage = "OFF"
    FlowUnits = "mL/min"


class SamplePressureConditionCard:
    MaxTimeToachievePressure = 60


class VolumePumpedConditionCard:
    NearThresholdReadBackMessage = "NEARING THRESHOLD"
    ThresholdReachedReadBackMessage = "THRESHOLD REACHED"
    OverMaximumReadbackMessage = "OVER MAXIMUM"
    TimetoReachOverThresholdValue = 60  # TODO need to verify
    EmptyEditFieldMessage = "This field is required"
    FlowHintMessage = "1.0L-100.0L"


class MobilePhaseSolventConditionCard:
    ConfigureSolventsInfo = "Change the bottle size or you want to reconfigure this or any other solvents bottle."
    StopPrimeInfo1 = "Workflow was manually stopped."
    StopPrimeInfo2 = "Tap CLOSE when available."
    TimeToTerminate = 5
    DefaultTestTime = 120
    RunningTextStatus = "In progress..."
    StoppingTextStatus = "Stopping"
    StoppedTextStatus = "Stopped"

"""
File_Name: commands.py
Desc: This file contains the constants used in commands screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/10/2021
__modified__ "Sharmila VAiramani" Added LampStateOn and LamStateOff - 05/20/2021
__modified__ "Sharmila Vairamani" Added LampWarmingTime constant -06/04/2021
__modified__ "Tyler Prada" Added autozero complete constant 7/2/21
"""


class CommandsConstants:
    TurnOnCommandActionText = "Lamp is off"
    LampOffReadBackMessage = "Lamp is off"
    LampOnReadBackMessage = "Lamp is on"
    LampWarmReadBackMessage = "Warming up..."
    LampStateOn = "On"
    LampStateOff = "Off"
    LampOnRequest = "on"
    LampOffRequest = "off"
    LampWarmingTime = 500
    LampTurnOffTime = 30  ## TODO need to confirm
    AutozeroCompleteMessage = "Autozero complete"
    LampOfftransitiontext = "Hold to turn off"
    LampOntransitiontext = "Hold to turn on"
    FlowTurnOnCommandActionText = "Off"
    FlowOntransitiontext = "0.100"
    FlowOnRequest = "on"
    FlowOffRequest = "off"
    HoldToResetText = "Hold to reset"
    ResetText = "Tap to reset system"
    ResetTransitionText = "Reset command sent..."
    EmergencyStopText = "Tap to stop all running activities"
    StopSentCommand = "Stopped command sent..."
    StopTransitionText = "Stopping the acquisition..."
    MaxFlowRate = 2.00
    MinFlowRate = 0.00
    FlowRateUnit = "mL/min"
    CommandsSlideAnimationTime = 4

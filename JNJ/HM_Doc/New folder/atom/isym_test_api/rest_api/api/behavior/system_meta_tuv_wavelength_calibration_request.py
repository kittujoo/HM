"""
Desc: This file contains the payload that needs to be sent with a Calibrate Wavelength request
"""
from dataclasses import dataclass

from isym_test_api.rest_api.api.solvent_management.flow_request import SolvFlowRateAndCompositionW


@dataclass
class SystemFlushSettings:
    # Flow settings used during the flush
    flowRate: SolvFlowRateAndCompositionW
    # Whether to perform the flush
    enabled: bool
    # The flush duration, in minutes
    duration: float


@dataclass
class SystemMetaTuvWavelengthCalibration:
    # Flow settings used during the preflush
    preflush: SystemFlushSettings
    # Flow settings used during the flush
    flush: SystemFlushSettings


def generate_calibrate_wavelength_request(preflush_status: bool = False, flush_status: bool = False):
    payload = SystemMetaTuvWavelengthCalibration(
        preflush=SystemFlushSettings(
            enabled=preflush_status,
            flowRate=SolvFlowRateAndCompositionW(
                flowRateTargetMlPerMin=1.0,
                solventAPct=100.0,
                solventBPct=0.0,
                solventCPct=0.0,
                solventDPct=0.0
            ),
            duration=10.0
        ),
        flush=SystemFlushSettings(
            enabled=flush_status,
            flowRate=SolvFlowRateAndCompositionW(
                flowRateTargetMlPerMin=1.0,
                solventAPct=100.0,
                solventBPct=0.0,
                solventCPct=0.0,
                solventDPct=0.0
            ),
            duration=10.0
        )
    )
    return payload

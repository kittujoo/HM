"""
Desc: This file contains the payload that needs to be sent with the metering pump leak request
"""
from dataclasses import dataclass, field


@dataclass
class SolvFlowRateAndCompositionW:
    # The requested flow rate (mL/min)
    flowRateTargetMlPerMin: float = 1.0

    # The % composition of solvent A
    solventAPct: float = 100.0

    # The % composition of solvent B
    solventBPct: float = 0.0

    # The % composition of solvent C
    solventCPct: float = 0.0

    # The % composition of solvent D
    solventDPct: float = 0.0


@dataclass
class SystemMeteringPumpLeakTest:
    # Whether to prime the sample metering pump
    includePrime: bool = True

    # QSM flow and composition, flow rate should be 5 mL/min
    qsm1: SolvFlowRateAndCompositionW = field(default_factory=SolvFlowRateAndCompositionW)

    # The target pressure for the metering pump leak test
    targetPressurePsi: float = 10000.0


def generate_start_metering_pump_leak_test_payload():
    payload = SystemMeteringPumpLeakTest(
        includePrime=True,
        qsm1=SolvFlowRateAndCompositionW(
            solventAPct=100.0
        )
    )

    return payload


def generate_start_metering_pump_leak_test_non_default():
    payload = SystemMeteringPumpLeakTest(
        includePrime=False,
        qsm1=SolvFlowRateAndCompositionW(
            flowRateTargetMlPerMin=5.0,
            solventAPct=25.0,
            solventBPct=25.0,
            solventCPct=25.0,
            solventDPct=25.0
        ),
        targetPressurePsi=5000.0
    )

    return payload


def generate_start_metering_pump_leak_test_minimum_pressure():
    payload = SystemMeteringPumpLeakTest(
        includePrime=True,
        qsm1=SolvFlowRateAndCompositionW(
            solventAPct=100.0
        ),
        targetPressurePsi=100.0
    )

    return payload


def generate_start_metering_pump_leak_test_maximum_pressure():
    payload = SystemMeteringPumpLeakTest(
        includePrime=True,
        qsm1=SolvFlowRateAndCompositionW(
            solventAPct=100.0
        ),
        targetPressurePsi=10000.0
    )

    return payload


def generate_start_metering_pump_leak_test_below_min_pressure():
    payload = SystemMeteringPumpLeakTest(
        includePrime=True,
        qsm1=SolvFlowRateAndCompositionW(
            solventAPct=100.0
        ),
        targetPressurePsi=99.9
    )

    return payload


def generate_start_metering_pump_leak_test_above_max_pressure():
    payload = SystemMeteringPumpLeakTest(
        includePrime=True,
        qsm1=SolvFlowRateAndCompositionW(
            solventAPct=100.0
        ),
        targetPressurePsi=10000.1
    )

    return payload

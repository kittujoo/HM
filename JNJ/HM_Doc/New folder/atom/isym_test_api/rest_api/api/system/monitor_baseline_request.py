from dataclasses import dataclass


@dataclass
class MonitorBaselineRequest:
    runTimeMin: float


def generate_default_system_monitor_baseline():
    payload = (MonitorBaselineRequest(
        runTimeMin=1.0)
    )
    return payload

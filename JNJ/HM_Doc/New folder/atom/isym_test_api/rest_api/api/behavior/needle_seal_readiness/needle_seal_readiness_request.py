"""
Desc: This file contains the payload that needs to be sent with a method request
"""
from dataclasses import dataclass


@dataclass
class NeedleSealReadinessRequest:
    flowRateTargetMlPerMin: float
    solventAPct: float
    solventBPct: float
    solventCPct: float
    solventDPct: float


def generate_default_needle_seal_readiness_request(flow_rate_targe_ml_per_min=1.0, solventapct=100.0, solventbpct=0.0, solventcpct=0.0, solventdpct=0.0):
    payload = (NeedleSealReadinessRequest(
        flowRateTargetMlPerMin=flow_rate_targe_ml_per_min,
        solventAPct=solventapct,
        solventBPct=solventbpct,
        solventCPct=solventcpct,
        solventDPct=solventdpct,
    )
    )
    return payload

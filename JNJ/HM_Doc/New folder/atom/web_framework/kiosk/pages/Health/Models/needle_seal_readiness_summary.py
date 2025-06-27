"""
File_Name: needle_seal_readiness_summary.py
Desc: This is the data-holder class which holds the attributes of the needle seal readiness test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/17/22
"""


class NeedleSealReadinessSummaryDetails:
    flow_rate: str
    system_pressure: str
    estimated_time: str

    def __init__(self, flow_rate: str, system_pressure: str, estimated_time: str):
        self.flow_rate = flow_rate
        self.system_pressure = system_pressure
        self.estimated_time = estimated_time

    def __str__(self):
        return f"solvent => {self.flow_rate}, priming_option => {self.system_pressure}, estimated_time=> {self.estimated_time}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NeedleSealReadinessSummaryDetails):
            return self.flow_rate == other.flow_rate \
                   and self.system_pressure == other.system_pressure \
                   and self.estimated_time == other.estimated_time

        return False
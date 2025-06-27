"""
File_Name: calibrate_wavelength_summary.py
Desc: This is the data-holder class which holds the attributes of the calibrate wavelength workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 7/18/22
"""


class CalibrateWavelengthSummaryDetails:
    flush: str
    pre_flush: None
    flow_cell: str
    lamp_state: str

    def __init__(self, flush: str, pre_flush: None, flow_cell: str, lamp_state: str):
        self.flush = flush
        self.pre_flush = pre_flush
        self.flow_cell = flow_cell
        self.lamp_state = lamp_state

    def __str__(self):
        return f"flush => {self.flush}, pre_flush => {self.pre_flush}, flow_cell=> {self.flow_cell}, lamp_state=> {self.lamp_state}"

    def __eq__(self, other):
        if other is not None and isinstance(other, CalibrateWavelengthSummaryDetails):
            return self.flush == other.flush \
                and self.flow_cell == other.flow_cell \
                and self.pre_flush == other.pre_flush \
                and self.flow_cell == other.flow_cell \
                and self.lamp_state == other.lamp_state

        return False

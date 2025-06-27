"""
File_Name: calibrate_axes_summary.py
Desc: This is the data-holder class which holds the attributes of the calibrate_axes workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 3/9/22
__modified__ = "Tyler Prada" added summary screen validation 6/17/22
"""

class CalibrateAxesSummaryDetails:
    compartment_door: str
    sample_plate: None
    tray_door: None
    needle_adaptor: None
    test_time: str

    def __init__(self, compartment_door: str, sample_plate: None, tray_door: None, needle_adaptor: None, test_time: str):
        self.compartment_door = compartment_door
        self.sample_plate = sample_plate
        self.tray_door = tray_door
        self.needle_adaptor = needle_adaptor
        self.test_time = test_time

    def __str__(self):
        return f"compartment_door => {self.compartment_door}, sample_plate => {self.sample_plate}, tray_door=> {self.tray_door}, needle_adaptor=> {self.needle_adaptor}, test_time=> {self.test_time}"

    def __eq__(self, other):
        if other is not None and isinstance(other, CalibrateAxesSummaryDetails):
            return self.compartment_door == other.compartment_door \
                and self.sample_plate == other.sample_plate \
                and self.tray_door == other.tray_door \
                and self.needle_adaptor == other.needle_adaptor\
                and self.test_time == other.test_time

        return False
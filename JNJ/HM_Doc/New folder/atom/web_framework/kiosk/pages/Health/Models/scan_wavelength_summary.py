"""
File_Name: scan_wavelength_summary.py
Desc: This is the data-holder class which holds the attributes of the sample metering scan wavelengthtest workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila" Initial Check-in 11/28/22
"""


class ScanWavelengthSummaryDetails:
    min_wavelength: str
    maxi_wavelength: str
    data_rate: str

    def __init__(self, min_wavelength: int, maxi_wavelength: int, data_rate: int):
        self.min_wavelength = min_wavelength
        self.maxi_wavelength = maxi_wavelength
        self.data_rate = data_rate

    def __str__(self):
        return f"min_wavelength => {self.min_wavelength}, maxi_wavelength => {self.maxi_wavelength}, data_rate=> {self.data_rate}"

    def __eq__(self, other):
        if other is not None and isinstance(other, ScanWavelengthSummaryDetails):
            return self.min_wavelength == other.min_wavelength \
                   and self.maxi_wavelength == other.maxi_wavelength \
                   and self.data_rate == other.data_rate

        return False

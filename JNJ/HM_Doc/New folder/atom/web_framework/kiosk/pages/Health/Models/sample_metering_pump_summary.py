"""
File_Name: sample_metering_pump_summary.py
Desc: This is the data-holder class which holds the attributes of the sample metering pump leak test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/10/22
__modified__ = "Tyler Prada" adjusted summary validation 12/5/22
"""
from dataclasses import dataclass


@dataclass
class SampleMeteringPumpSummaryDetails:
    priming_option: None

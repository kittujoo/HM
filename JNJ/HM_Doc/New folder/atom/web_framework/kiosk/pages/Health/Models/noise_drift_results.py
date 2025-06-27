"""
File_Name: noise_drift_results.py
Desc: This is the data-holder class which holds the attributes of the noise & drift test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__  = "Sharmila Vairamani" Initial Check-in- 6/13/2022

"""


class NoiseDriftConditionDetails:
    flow_rate: str
    composition: float
    flow_cell: str
    ambient_temperature: str

    def __init__(self, flow_rate: str, composition: float, flow_cell: str, ambient_temperature: str):
        self.flow_rate = flow_rate
        self.composition = composition
        self.flow_cell = flow_cell
        self.ambient_temperature = ambient_temperature

    def __str__(self):
        return f"flow_rate => {self.flow_rate}, composition => {self.composition}, flow_cell =>{self.flow_cell} " \
               f" ambient_temperature=> {self.ambient_temperature}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NoiseDriftConditionDetails):
            return self.flow_rate == other.flow_rate \
                   and self.composition == other.composition \
                   and self.flow_cell == other.flow_cell \
                   and self.ambient_temperature == other.ambient_temperature

        return False


class NoiseDriftResultsDetails:
    total_drift: str
    segment_peak_noise: str

    def __init__(self, total_drift: str, segment_peak_noise: float):
        self.total_drift = total_drift
        self.segment_peak_noise = segment_peak_noise

    def __str__(self):
        return f"total_drift => {self.total_drift}, segment_peak_noise => {self.segment_peak_noise}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NoiseDriftConditionDetails):
            return self.total_drift == other.total_drift \
                   and self.segment_peak_noise == other.segment_peak_noise

        return False

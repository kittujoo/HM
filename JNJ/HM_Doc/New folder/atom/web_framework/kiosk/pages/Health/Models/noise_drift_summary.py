"""
File_Name: noise_drift_summary.py
Desc: This is the data-holder class which holds the attributes of the noise & drift test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/20/22
__modified__ = "Sharmila Vairamani" Added classes to vaidate - 6/13/2022

"""


class NoiseDriftSummaryDetails:
    flow_rate: str
    composition: str
    flow_cell: str
    data_rate: str
    filter: str
    lamp: str
    wavelength_a: str
    ambient_temperature: str
    test_time: str

    def __init__(self, flow_rate: str, composition: str, flow_cell: str, data_rate: str, filter: str, lamp: str,
                 wavelength_a: str, ambient_temperature: str, test_time: str):
        self.flow_rate = flow_rate
        self.composition = composition
        self.flow_cell = flow_cell
        self.data_rate = data_rate
        self.filter = filter
        self.lamp = lamp
        self.wavelength_a = wavelength_a
        self.ambient_temperature = ambient_temperature
        self.test_time = test_time

    def __str__(self):
        return f"flow_rate => {self.flow_rate}, composition => {self.composition}, flow_cell =>{self.flow_cell} " \
               f" data_rate => {self.data_rate}, filter=> {self.filter}, lamp=> {self.lamp} " \
               f" wavelength_a=> {self.wavelength_a}, ambient_temperature=> {self.ambient_temperature}, test_time=> {self.test_time}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NoiseDriftSummaryDetails):
            return self.flow_rate == other.flow_rate \
                   and self.composition == other.composition \
                   and self.flow_cell == other.flow_cell \
                   and self.data_rate == other.data_rate \
                   and self.filter == other.filter \
                   and self.lamp == other.lamp \
                   and self.wavelength_a == other.wavelength_a \
                   and self.ambient_temperature == other.ambient_temperature \
                   and self.test_time == other.test_time

        return False


class NoiseDriftSolventDetails:
    flow_rate: str
    solvent_a: str
    solvent_b: str
    solvent_c: str
    solvent_d: str

    def __init__(self, flow_rate: str, solvent_a: str,
                 solvent_b: str, solvent_c: str, solvent_d: str):
        self.flow_rate = flow_rate
        self.solvent_a = solvent_a
        self.solvent_b = solvent_b
        self.solvent_c = solvent_c
        self.solvent_d = solvent_d

    def __str__(self):
        return f"flow_rate => {self.flow_rate}, solvent_a => {self.solvent_a}, solvent_b =>{self.solvent_b} " \
               f" solvent_c => {self.solvent_c}, solvent_d=> {self.solvent_d}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NoiseDriftSolventDetails):
            return self.flow_rate == other.flow_rate \
                   and self.solvent_a == other.solvent_a \
                   and self.solvent_b == other.solvent_b \
                   and self.solvent_c == other.solvent_c \
                   and self.solvent_d == other.solvent_d

        return False


class NoiseDriftWavelengthDetails:
    single_wavelength: str
    dual_wavelength: str

    def __init__(self, single_wavelength: str, dual_wavelength: str):
        self.single_wavelength = single_wavelength
        self.dual_wavelength = dual_wavelength

    def __str__(self):
        return f"single_wavelength => {self.single_wavelength}, dual_wavelength => {self.dual_wavelength}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NoiseDriftWavelengthDetails):
            return self.single_wavelength == other.single_wavelength \
                   and self.dual_wavelength == other.dual_wavelength

        return False


class NoiseDriftDataFrequencyDetails:
    data_rate: str
    filter_time_constant: str

    def __init__(self, data_rate: str, filter_time_constant: str):
        self.data_rate = data_rate
        self.filter_time_constant = filter_time_constant

    def __str__(self):
        return f"data_rate => {self.data_rate}, filter_time_constant => {self.filter_time_constant}"

    def __eq__(self, other):
        if other is not None and isinstance(other, NoiseDriftDataFrequencyDetails):
            return self.data_rate == other.data_rate \
                   and self.filter_time_constant == other.filter_time_constant

        return False
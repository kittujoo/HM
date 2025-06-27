"""
File_Name: summary_workflow.py
Desc: This is the data-holder class which holds the attributes of the startup workflow
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 1/6/21
__modified__ = "Sharmila Vairamani" Added classes for each summary details- 07/05/2022

"""


class PrimeSummaryDetails:
    prime_solvent: str
    prime_seal_wash: str

    def __init__(self, prime_solvent: str, prime_seal_wash: str):
        self.prime_solvent = prime_solvent
        self.prime_seal_wash = prime_seal_wash

    def __str__(self):
        return f"prime_solvent => {self.prime_solvent}, prime_seal_wash => {self.prime_seal_wash}"

    def __eq__(self, other):
        if other is not None and isinstance(other, PrimeSummaryDetails):
            return self.prime_solvent == other.prime_solvent \
                   and self.prime_seal_wash == other.prime_seal_wash

        return False


class TemperatureSummaryDetails:
    sample_temperature: float
    column_temperature: float

    def __init__(self, sample_temperature: float, column_temperature: float):
        self.sample_temperature = sample_temperature
        self.column_temperature = column_temperature

    def __str__(self):
        return f"sample_temperature => {self.sample_temperature}, column_temperature => {self.column_temperature}"

    def __eq__(self, other):
        if other is not None and isinstance(other, TemperatureSummaryDetails):
            return self.sample_temperature == other.sample_temperature \
                   and self.column_temperature == other.column_temperature

        return False


class SolventSummaryDetails:
    flow_rate: float
    solvent_a: float
    solvent_b: float
    solvent_c: float
    solvent_d: float

    def __init__(self, flow_rate: float, solvent_a: float,
                 solvent_b: float, solvent_c: float, solvent_d: float):
        self.flow_rate = flow_rate
        self.solvent_a = solvent_a
        self.solvent_b = solvent_b
        self.solvent_c = solvent_c
        self.solvent_d = solvent_d
        

    def __str__(self):
        return f"flow_rate => {self.flow_rate}, solvent_a => {self.solvent_a}, solvent_b =>{self.solvent_b} " \
               f" solvent_c => {self.solvent_c}, solvent_d=> {self.solvent_d}"

    def __eq__(self, other):
        if other is not None and isinstance(other, SolventSummaryDetails):
            return self.flow_rate == other.flow_rate \
                   and self.solvent_a == other.solvent_a \
                   and self.solvent_b == other.solvent_b \
                   and self.solvent_c == other.solvent_c \
                   and self.solvent_d == other.solvent_d

        return False

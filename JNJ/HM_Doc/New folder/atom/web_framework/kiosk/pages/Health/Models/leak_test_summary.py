"""
File_Name: leak_test_summary.py
Desc: This is the data-holder class which holds the attributes of the leak test work flow
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/01/2020

"""


class LeakTestSummaryDetails:
    solvent: str
    accumulator_target_pressure: int
    primary_target_pressure: int
    end_point: str
    prime_option: str

    def __init__(self, solvent: str, accumulator_target_pressure: float,
                 primary_target_pressure: str, end_point: str, prime_option: str):
        self.Solvent = solvent
        self.accumulator_target_pressure = accumulator_target_pressure
        self.primary_target_pressure = primary_target_pressure
        self.end_point = end_point
        self.prime_option = prime_option

    def __str__(self):
        return f"Solvent => {self.Solvent}, accumulator_target_pressure => {self.accumulator_target_pressure}, primary_target_pressure =>{self.primary_target_pressure} " \
               f" end_point_option => {self.end_point}, selected_prime_option => {self.prime_option}"

    def __eq__(self, other):
        if other is not None and isinstance(other, LeakTestSummaryDetails):
            return self.Solvent == other.Solvent \
                   and self.accumulator_target_pressure == other.accumulator_target_pressure \
                   and self.primary_target_pressure == other.primary_target_pressure

        return False

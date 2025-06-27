"""
File_Name: dynamic_leak_test_results.py
Desc: This is the data-holder class which holds the attributes of the leak test work flow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/11/2022

"""


class PrimaryResultsDetails:
    result_state: str
    primary_pressure: int
    leak_rate: float
    final_stroke: int
    compression_attempts: int

    def __init__(self, result_state: str, primary_pressure: int,
                 leak_rate: float, final_stroke: int,
                 compression_attempts: int):
        self.result_state = result_state
        self.primary_pressure = primary_pressure
        self.leak_rate = leak_rate
        self.final_stroke = final_stroke
        self.compression_attempts = compression_attempts

    def __str__(self):
        return f"result_state => {self.result_state}, primary_pressure => {self.primary_pressure}, leak_rate =>{self.leak_rate} " \
               f" final_stroke => {self.final_stroke},  compression_attempts => {self.compression_attempts}"

    def __eq__(self, other):
        if other is not None and isinstance(other, PrimaryResultsDetails):
            return self.result_state == other.result_state \
                   and self.primary_pressure == other.primary_pressure \
                   and self.leak_rate == other.leak_rate \
                   and self.final_stroke == other.final_stroke \
                   and self.compression_attempts == other.compression_attempts


class AccumulatorResultsDetails:
    result_state: str
    accumulator_pressure: int
    leak_rate: float
    final_stroke: int
    compression_attempts: int

    def __init__(self, result_state: str, primary_pressure: int,
                 leak_rate: float, final_stroke: int,
                 compression_attempts: int):
        self.result_state = result_state
        self.accumulator_pressure = primary_pressure
        self.leak_rate = leak_rate
        self.final_stroke = final_stroke
        self.compression_attempts = compression_attempts

    def __str__(self):
        return f"result_state => {self.result_state}, accumulator_pressure => {self.accumulator_pressure}, leak_rate =>{self.leak_rate} " \
               f" final_stroke => {self.final_stroke},  compression_attempts => {self.compression_attempts}"

    def __eq__(self, other):
        if other is not None and isinstance(other, AccumulatorResultsDetails):
            return self.result_state == other.result_state \
                   and self.accumulator_pressure == other.accumulator_pressure \
                   and self.leak_rate == other.leak_rate \
                   and self.final_stroke == other.final_stroke \
                   and self.compression_attempts == other.compression_attempts

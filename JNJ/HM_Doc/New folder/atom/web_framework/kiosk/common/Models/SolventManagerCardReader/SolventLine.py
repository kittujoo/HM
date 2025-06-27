"""
File_Name: sm_configuration_settings.py
Desc: This is the data-holder class which holds the attributes of the solvent composition screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani " Initial Check-in 02/15/2021
__modified__ = "Sharmila Varamani" Added get_percentage_value function -06/29/2021
__modified_ = "Sharmla Vairamani" Removed the lock icon attribute - 10/17/2022

"""


class SolventLine:
    line_id: str
    percentage_value: float

    def __init__(self, line_id: str, percentage_value: float) -> None:
        self.line_id = line_id
        self.percentage_value = percentage_value

    def __str__(self):
        return f"From SolventLine {self.line_id}, Percentage => {self.percentage_value}"

    @staticmethod
    def parse(solvent_data):
        if solvent_data is not None:
            solvent_line_data_list = solvent_data.split(',')
            print(len(solvent_line_data_list))
            if len(solvent_line_data_list) == 3:
                percentage_value = solvent_line_data_list[2]
                solvent_line = SolventLine(solvent_line_data_list[0], percentage_value)
                return solvent_line
        return None

    @staticmethod
    def get_percentage_value(solvent_data):
        if solvent_data is not None:
            solvent_line_data_list = solvent_data.split(',')
            print(len(solvent_line_data_list))
            if len(solvent_line_data_list) == 3:
                percentage_value = solvent_line_data_list[2]
                return percentage_value
        return None

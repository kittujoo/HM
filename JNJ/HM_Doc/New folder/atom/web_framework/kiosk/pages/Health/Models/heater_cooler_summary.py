"""
File_Name: heater_cooler_summary.py
Desc: This is the data-holder class which holds the attributes of the heater/cooler workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 2/15/22
__modified__ = "Tyler Prada" Removed results due to different validation method 7/22/22
"""


class HeaterCoolerSummaryDetails:
    ambient_temperature: float
    column_temperature: float
    column_door: str
    

    def __init__(self, ambient_temperature: float, column_temperature: float, column_door: str):
        self.ambient_temperature = ambient_temperature
        self.column_temperature = column_temperature
        self.column_door = column_door


    def __str__(self):
        return f"ambient_temperature => {self.ambient_temperature}, column_temperature =>{self.column_temperature} " \
               f" column_door => {self.column_door}"

    def __eq__(self, other):
        if other is not None and isinstance(other, HeaterCoolerSummaryDetails):
            return self.ambient_temperature == other.ambient_temperature \
                   and self.column_temperature == other.column_temperature \
                   and self.column_door == other.column_door

        return False
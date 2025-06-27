"""
File_Name: ColumnDetails.py
Desc: This is data-holder class which holds the attribute of the column details
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/20/2023

"""

from pydantic import BaseModel, Field


class ColumnDetails(BaseModel):
    column_name: str = Field(min_length=3)
    description: str = Field(min_length=3)
    serial_number: str = Field(min_length=14)
    gtin: str = Field(min_length=14)
    part_number: str = Field(min_length=10)
    maximum_pressure : int
    maximum_temperature : float
    ph_lower_limit: int = Field(gt=0)
    ph_higher_limit:  int = Field(le=12)

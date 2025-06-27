"""
File_Name: LampDetails.py
Desc: This is data-holder class which holds the attribute of the lamp details
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 10/04/2023

"""

from pydantic import BaseModel, Field


class LampDetails(BaseModel):
    serial_number: str = Field(min_length=10)
    install_date: str = Field(default='02/29/2020')
    total_lamp_hours: str = Field(default='2000 hours')
    successful_ignitions: int = Field(ge=0)
    failed_ignitions: int = Field(ge=0)
    
   
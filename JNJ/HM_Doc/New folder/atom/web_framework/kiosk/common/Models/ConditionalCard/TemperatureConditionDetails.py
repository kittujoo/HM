"""
File_Name: TemperatureConditionDetails.py
Desc: This is data-holder class which holds the attribute of the column temperature
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 03/10/2020
__modified__ = "Sharmila vairamani" Added title icon status attribute - 09/03/2020
__modified__ = "Sharmila vairamani" Added validate progress bar values - 09/03/2020
__modified__ = "Sharmila Vairamani" Added validate_progress_bar_values function- 10/02/2020

"""

from utilities.logger import Logger
from utilities.string_utility import remove_substring
from utilities.type_converter import TypeConverter


class TemperatureConditionCardDetails:
    read_back_message: str
    temperature: float
    title_icon_status: str
    progress_bar_start_point: str
    progress_bar_end_point: str

    def __init__(self, input_read_back_message: str, input_temperature: float, title_icon_status: str = None,
                 progress_bar_start_point: str = None, progress_bar_end_point: str = None):
        self.read_back_message = input_read_back_message
        self.temperature = input_temperature
        self.title_icon_status = title_icon_status
        if progress_bar_start_point is not None:
            self.progress_bar_start_point = remove_substring(progress_bar_start_point, "%")
        if progress_bar_end_point is not None:
            self.progress_bar_end_point = remove_substring(progress_bar_end_point, "%")
        self.logger = Logger(self.__class__.__name__)

    def validate_progress_bar_values(self, previous_conditional_card_detail, raise_in_temperature):
        """
           desc:This function is to validate the increase or decrease of the temperature is linear.
               When temp increases, right/end stays same and left/start increases until the desired temperature is reached
               When temp decreases, left/start stays same and right/end increases until the desired temperature is reached
        """

        validation_status = True
        if previous_conditional_card_detail is not None:
            if raise_in_temperature:
                (f"When there is an increase in temperature")
                self.logger.info(f" self.progress_bar_start_point=> {self.progress_bar_start_point}, "
                             f"previous progress_bar_start_point => {previous_conditional_card_detail.progress_bar_start_point}")
                validation_status = self.validate_progress_bar_points(self.progress_bar_start_point,
                                                                      previous_conditional_card_detail.progress_bar_start_point)
            else:
                (f"When there is an decrease in temperature")
                self.logger.info(f" self.progress_bar_end_point=> {self.progress_bar_end_point}, "
                             f"previous progress_bar_end_point => {previous_conditional_card_detail.progress_bar_end_point}")
                validation_status = self.validate_progress_bar_points(self.progress_bar_end_point,
                                                                      previous_conditional_card_detail.progress_bar_end_point)

        return validation_status

    def validate_progress_bar_points(self, current_progress_bar_point: str, previous_progress_bar_point: str):
        """
        This function validates current set point line of the progress bar with the previous set point line of the progress bar
        and if the current line is greater than the previous line , then it returns true
        @param current_progress_bar_point:
        @param previous_progress_bar_point:
        @return:
        """
        validation_status = True
        if TypeConverter.is_float(current_progress_bar_point) and TypeConverter.is_float(previous_progress_bar_point):
            current_progress_bar_point_value = TypeConverter.to_float(current_progress_bar_point)
            previous_progress_bar_point_value = TypeConverter.to_float(previous_progress_bar_point)
            self.logger.info(f" current progress_bar_point => {current_progress_bar_point_value}, "
                             f"previous progress_bar_point => {previous_progress_bar_point_value}")

            validation_status = current_progress_bar_point_value >= previous_progress_bar_point_value
            self.logger.info(f"validation_status=====>{validation_status}")
        return validation_status

    def __str__(self):
        return f"read_back_message => {self.read_back_message}, temperature => {self.temperature}, title icon status  => {self.title_icon_status}, progress bar start point => {self.progress_bar_start_point}, progress bar end point => {self.progress_bar_end_point}"

"""
File_Name: pressure_settings_screen_base.py
Desc: This file contains common user specific function on any pressure settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/5/2021

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.base_page import BasePage


class PressureSettingsScreenBase(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.locators_class = None

    def select_unit_option(self, unit):
        """
        This function is used to tap on the given pressure unit option
        within a pressure setting screen
        :param unit: The current pressure unit to be selected
        :return: Void
        """
        pressure_unit_text_dictionary = {
            "bar": self.locators_class.BAR_OPTION,
            "kPa": self.locators_class.KPA_OPTION,
            "psi": self.locators_class.PSI_OPTION,
            "MPa": self.locators_class.MPA_OPTION
        }

        if unit in pressure_unit_text_dictionary:
            locator = pressure_unit_text_dictionary[unit]
            self.tap(locator)
            return

        assert False, (f"Unexpected pressure unit => {unit}")

    def find_active_unit(self):
        """
        This function is used to verify if the chosen active unit is psi
        :return psi_active: bool value
        """
        psi_active = self.is_displayed(self.locators_class.ACTIVE_PSI_OPTION)
        return psi_active

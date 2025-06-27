"""
File_Name: calibrate_axes_summary_screen.py
Desc: This file contains specific user actions on screens within the calibrate axes workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 3/9/2022
__modified__ = "Tyler Prada" added validation method 4/4/22
__modified__ = "Tyler Prada" added summary screen validation functions 6/17/22
__modified__ = "Tyler Prada" added results validation functions 7/28/22
__modified__ = "Tyler Prada" added platter path results 8/31/22
__modified__ = "Tyler Prada" Post-FCS Adjustments 7/26/23
"""
from web_framework.kiosk.pages.Maintain.Models.calibrate_axes_summary import CalibrateAxesSummaryDetails
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.calibrate_axes_constants import (CalibrateAxesConstants,
                                                                                                CalibratePlatterConstants,
                                                                                                CalibrateB0AxesConstants,
                                                                                                CalibrateOffsetConstants)
from web_framework.kiosk.pages.Locators.Maintain.calibrate_axes_locators import CalibrateAxesWorkflowLocators
from web_framework.kiosk.pages.base_page import BasePage


class CalibrateAxesWorkflowSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_summary_screen(self):
        locator = CalibrateAxesWorkflowLocators.SUMMARY_PAGE_BANNER
        screen_name = "Summary screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_results_screen(self):
        locator = CalibrateAxesWorkflowLocators.RESULTS_PAGE_BANNER
        screen_name = "Results screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_completion_screen(self):
        locator = CalibrateAxesWorkflowLocators.COMPLETION_PAGE_BANNER
        screen_name = "Completion screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_screen_details(self, calibration_path):
        current_sample_plate = None
        current_tray_door = None
        current_needle_adaptor = None
        current_compartment_door = None
        current_test_time = None
        if calibration_path == "Z-Axis" or calibration_path == "Zp-Axis" or calibration_path == "Hard-Stop":
            current_compartment_door = self.get_text(CalibrateAxesWorkflowLocators.COMPARTMENT_DOOR_INFO_LABEL)
            current_sample_plate = self.get_text(CalibrateAxesWorkflowLocators.SAMPLE_PLATES_INFO_LABEL)
            current_test_time = self.get_text(CalibrateAxesWorkflowLocators.TEST_TIME_INFO_LABEL)

        if calibration_path == "Platter":
            current_compartment_door = self.get_text(CalibrateAxesWorkflowLocators.COMPARTMENT_DOOR_INFO_LABEL)
            current_tray_door = self.get_text(CalibrateAxesWorkflowLocators.TRAY_DRAWER_INFO_LABEL)
            current_test_time = self.get_text(CalibrateAxesWorkflowLocators.TEST_TIME_INFO_LABEL)

        if calibration_path == "B-0-Axes":
            current_compartment_door = self.get_text(CalibrateAxesWorkflowLocators.COMPARTMENT_DOOR_INFO_LABEL)
            current_sample_plate = self.get_text(CalibrateAxesWorkflowLocators.SAMPLE_PLATES_INFO_LABEL)
            current_needle_adaptor = self.get_text(CalibrateAxesWorkflowLocators.NEEDLE_ADAPTOR_INFO_LABEL)
            current_test_time = self.get_text(CalibrateAxesWorkflowLocators.TEST_TIME_INFO_LABEL)

        calibrate_axes_summary_details = CalibrateAxesSummaryDetails(current_compartment_door,
                                                                     current_sample_plate,
                                                                     current_tray_door,
                                                                     current_needle_adaptor,
                                                                     current_test_time)

        return calibrate_axes_summary_details

    def get_expected_summary_screen_details(self, calibration_path):
        expected_sample_plate = None
        expected_tray_door = None
        expected_needle_adaptor = None
        expected_compartment_door = None
        expected_test_time = None
        if calibration_path == "Z-Axis" or calibration_path == "Zp-Axis" or calibration_path == "Hard-Stop":
            expected_compartment_door = CalibrateAxesConstants.DefaultCompartmentDoor
            expected_sample_plate = CalibrateAxesConstants.DefaultSamplePlate
            expected_test_time = CalibrateAxesConstants.DefaultTestTime

        if calibration_path == "Platter":
            expected_compartment_door = CalibrateAxesConstants.DefaultCompartmentDoor
            expected_tray_door = CalibrateAxesConstants.DefaultTrayDoor
            expected_test_time = CalibrateAxesConstants.DefaultTestTime

        if calibration_path == "B-0-Axes":
            expected_compartment_door = CalibrateAxesConstants.DefaultCompartmentDoor
            expected_sample_plate = CalibrateAxesConstants.DefaultSamplePlate
            expected_needle_adaptor = CalibrateAxesConstants.DefaultNeedleAdaptor
            expected_test_time = CalibrateAxesConstants.DefaultTestTime

        calibrate_axes_summary_details = CalibrateAxesSummaryDetails(expected_compartment_door,
                                                                     expected_sample_plate,
                                                                     expected_tray_door,
                                                                     expected_needle_adaptor,
                                                                     expected_test_time)

        return calibrate_axes_summary_details

    def validate_results_details(self, calibration_path):
        if calibration_path == "Platter":
            self.validate_platter_results()
        elif calibration_path == "B-0-Axes":
            self.validate_beta_theta_results()
        else:
            assert self.get_text(CalibrateAxesWorkflowLocators.RESULTS_STATUS) == "Passed"

    def validate_platter_results(self):
        current_offset_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.OFFSET_VALUE_LABEL))
        assert current_offset_value >= CalibratePlatterConstants.OffsetValueMin and current_offset_value <= CalibratePlatterConstants.OffsetValueMax, f"Offset value is out of accepted range: {current_offset_value}"

    def validate_beta_theta_results(self):
        # TODO: If assert fails, then check if the value is highlighted orange | [INS-26139] all values out of range, highlighting not occurring
        # Rn values
        current_P1RN_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_ONE_RN))
        current_P2RN_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_TWO_RN))
        current_P3RN_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_THREE_RN))
        assert current_P1RN_value >= CalibrateB0AxesConstants.RnValueMin and current_P1RN_value <= CalibrateB0AxesConstants.RnValueMax, f"Plate 1 Rn value is out of acceptable range: {current_P1RN_value}"
        assert current_P2RN_value >= CalibrateB0AxesConstants.RnValueMin and current_P2RN_value <= CalibrateB0AxesConstants.RnValueMax, f"Plate 2 Rn value is out of acceptable range: {current_P2RN_value}"
        assert current_P3RN_value >= CalibrateB0AxesConstants.RnValueMin and current_P3RN_value <= CalibrateB0AxesConstants.RnValueMax, f"Plate 3 Rn value is out of acceptable range: {current_P3RN_value}"

        # Lc values
        current_P1LC_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_ONE_LC))
        current_P2LC_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_TWO_LC))
        current_P3LC_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_THREE_LC))
        assert current_P1LC_value >= CalibrateB0AxesConstants.LcValueMin and current_P1LC_value <= CalibrateB0AxesConstants.LcValueMax, f"Plate 1 Lc value is out of acceptable range: {current_P1LC_value}"
        assert current_P2LC_value >= CalibrateB0AxesConstants.LcValueMin and current_P2LC_value <= CalibrateB0AxesConstants.LcValueMax, f"Plate 2 Lc value is out of acceptable range: {current_P2LC_value}"
        assert current_P3LC_value >= CalibrateB0AxesConstants.LcValueMin and current_P3LC_value <= CalibrateB0AxesConstants.LcValueMax, f"Plate 3 Lc value is out of acceptable range: {current_P3LC_value}"

        # Beta values
        current_P1B_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_ONE_BETA))
        current_P2B_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_TWO_BETA))
        current_P3B_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_THREE_BETA))
        assert current_P1B_value >= CalibrateB0AxesConstants.BetaValueMin and current_P1B_value <= CalibrateB0AxesConstants.BetaValueMax, f"Plate 1 Beta value is out of acceptable range: {current_P1B_value}"
        assert current_P2B_value >= CalibrateB0AxesConstants.BetaValueMin and current_P2B_value <= CalibrateB0AxesConstants.BetaValueMax, f"Plate 2 Beta value is out of acceptable range: {current_P2B_value}"
        assert current_P3B_value >= CalibrateB0AxesConstants.BetaValueMin and current_P3B_value <= CalibrateB0AxesConstants.BetaValueMax, f"Plate 3 Beta value is out of acceptable range: {current_P3B_value}"

        # Theta values
        current_P1T_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_ONE_THETA))
        current_P2T_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_TWO_THETA))
        current_P3T_value = TypeConverter.to_float(self.get_text(CalibrateAxesWorkflowLocators.PLATE_THREE_THETA))
        assert current_P1T_value >= CalibrateB0AxesConstants.ThetaValueMin and current_P1T_value <= CalibrateB0AxesConstants.ThetaValueMax, f"Plate 1 Theta value is out of acceptable range: {current_P1T_value}"
        assert current_P2T_value >= CalibrateB0AxesConstants.ThetaValueMin and current_P2T_value <= CalibrateB0AxesConstants.ThetaValueMax, f"Plate 2 Theta value is out of acceptable range: {current_P2T_value}"
        assert current_P3T_value >= CalibrateB0AxesConstants.ThetaValueMin and current_P3T_value <= CalibrateB0AxesConstants.ThetaValueMax, f"Plate 3 Theta value is out of acceptable range: {current_P3T_value}"

    def validate_axis_results(self):
        self.wait_time_to_load_value(CalibrateAxesWorkflowLocators.OFFSET_VALUE_LABEL)
        current_offset_value = float(self.get_text(CalibrateAxesWorkflowLocators.OFFSET_VALUE_LABEL).strip())
        test_status = self.get_text(CalibrateAxesWorkflowLocators.RESULTS_STATUS)
        offset_unit = self.get_text(CalibrateAxesWorkflowLocators.OFFSET_VALUE)
        assert current_offset_value >= CalibrateOffsetConstants.OffsetValue, f"Offset value is out of accepted range: {current_offset_value}"
        assert CalibrateAxesConstants.OffsetUnit in offset_unit, f"Offset unit is not in mm. Actual Offset: {offset_unit}"
        assert test_status == CalibrateAxesConstants.PassMessage, f"The test was displayed as failed"

    def validate_z_axis_welcome_text(self):
        self.wait_time_to_load_value(CalibrateAxesWorkflowLocators.WELCOME_PARA_ONE_Z_AXIS)
        actual_paragraph_text = [self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_ONE_Z_AXIS),
                                 self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_TWO_Z_AXIS),
                                 self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_THREE_Z_AXIS)]
        expected_paragraph_text = CalibrateAxesConstants.expected_welcome_paragraph_text_Z_axis
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    def validate_zp_axis_welcome_text(self):
        self.wait_time_to_load_value(CalibrateAxesWorkflowLocators.WELCOME_PARA_ONE_Zp_AXIS)
        actual_paragraph_text = [self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_ONE_Zp_AXIS),
                                 self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_TWO_Zp_AXIS)]
        expected_paragraph_text = CalibrateAxesConstants.expected_welcome_paragraph_text_Zp_axis
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    def validate_hard_stop_axis_welcome_text(self):
        self.wait_time_to_load_value(CalibrateAxesWorkflowLocators.WELCOME_PARA_ONE_HARD_STOP)
        actual_paragraph_text = [self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_ONE_HARD_STOP),
                                 self.get_text(CalibrateAxesWorkflowLocators.WELCOME_PARA_TWO_HARD_STOP)]
        expected_paragraph_text = CalibrateAxesConstants.expected_welcome_paragraph_text_HardStop_axis
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

"""
File_Name: calibrate_wavelength_work_flow.py
Desc: This file contains specific user action on all the screen in the calibrate wavelength workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 02/22/2022
__modified__ = "Tyler Prada" added misc page validations 7/18/22
__modified__ = "Tyler Prada" Tweaked status and results steps/logic 9/7/22
"""
import time

from selenium.webdriver.common.by import By

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.calibrate_wavelength_constant import CalibrateWavelengthConstant
from web_framework.kiosk.pages.Locators.Maintain.calibrate_wavelength_locators import CalibrateWavelengthWorkflowLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Maintain.calibrate_wavelength_locators_lookup import CalibrateWavelengthLookup
from web_framework.kiosk.pages.base_page import BasePage


class CalibrateWavelengthWorkflowScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)
        self.selected_summary_details = None

    def tap_back_icon(self):
        self.tap(CalibrateWavelengthWorkflowLocators.BACK_BUTTON)

    def tap_retry_button(self):
        self.wait_element_to_be_clickable(CalibrateWavelengthWorkflowLocators.RETRY_BUTTON, self.wait_time)
        self.tap(CalibrateWavelengthWorkflowLocators.RETRY_BUTTON)

    def select_solvent_line(self, solvent_line: str):
        if solvent_line in CalibrateWavelengthLookup.solvent_line_dictionary:
            locator = CalibrateWavelengthLookup.solvent_line_dictionary[solvent_line]
            self.click(locator)
            return
        assert False, f"Invalid solvent => {solvent_line}"

    def set_flow(self, flow_rate):
        self.enter_value_for_specific_module(CalibrateWavelengthWorkflowLocators.FLOW_EDIT_FIELD, flow_rate)

    def validate_options_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.OPTIONS_PAGE_BANNER
        screen_name = "Flush Column Options screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_result_status(self):
        return self.find_element(CalibrateWavelengthWorkflowLocators.TEST_STATUS).text

    def wait_for_test_end(self, timeout=CalibrateWavelengthConstant.MaxiTimeToCalibrate):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_displayed(CalibrateWavelengthWorkflowLocators.RESULTS_PAGE_BANNER):
                return
            elif self.is_displayed(CalibrateWavelengthWorkflowLocators.WORKFLOW_STOPPED_BANNER):
                assert False, "Calibration got interrupted"
        assert False, "Calibration did not finish in the allotted time"

    def validate_preconditions_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.PRECONDITIONS_PAGE_BANNER
        screen_name = "Preconditions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_stop_button(self):
        locator = BasePageLocators.STOP_BUTTON
        screen_name = "Flow control screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flow_control_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.FLOW_RATE_BANNER
        screen_name = "Flow Rate screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flow_interrupted_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.INTERRUPTED_BANNER
        screen_name = "Workflow Interrupted"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_next_button_for_check_box(self):
        current_check_box_checked_state = self.is_check_box_selected(
            CalibrateWavelengthWorkflowLocators.CHECK_FOR_LEAK_BUTTON)
        self.logger.info(f"current_check_box_checked_state===>>>{current_check_box_checked_state}")
        if current_check_box_checked_state is False:
            assert self.is_disabled(BasePageLocators.NEXT_BUTTON_LABEL) is False

    def validate_next_button_for_flow_control_flow(self):
        current_toggle_button_state = self.is_toggle_button_enabled(
            CalibrateWavelengthWorkflowLocators.FLOW_TOGGLE_BUTTON)
        if current_toggle_button_state is False:
            assert self.is_disabled(BasePageLocators.NEXT_BUTTON_LABEL) is False

    def get_welcome_paragraph_text(self):
        self.logger.info("The calibrate workflow++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return [self.get_text(CalibrateWavelengthWorkflowLocators.WELCOME_PARA_ONE),
                self.get_text(CalibrateWavelengthWorkflowLocators.WELCOME_PARA_TWO),
                self.get_text(CalibrateWavelengthWorkflowLocators.WELCOME_PARA_THREE)]

    def get_better_results_text(self):
        return [self.get_text(CalibrateWavelengthWorkflowLocators.POINT_ONE_FOR_BETTER_RESULTS_TEXT),
                self.get_text(CalibrateWavelengthWorkflowLocators.POINT_TWO_FOR_BETTER_RESULTS_TEXT)]

    def validate_function_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.FUNCTION_BANNER
        screen_name = "Welcome Screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_wavelength_table_data(self):
        self.wait_for_element_visibility(self.wait_time, CalibrateWavelengthWorkflowLocators.WAVELENGTH_TABLE_DATA)
        wavelength_table_locator = self.find_element(CalibrateWavelengthWorkflowLocators.WAVELENGTH_TABLE)
        rows = wavelength_table_locator.find_elements(By.XPATH,
                                                      "//ics-info-list-item[@class='collapsible-table-header']//ics-table//div[@class='table']/ul")
        self.logger.info(f" The no of rows {len(rows)}")
        measured_wavelength_list = self.get_wavelength_data_list(2, wavelength_table_locator)
        for i in range(len(measured_wavelength_list)):
            assert measured_wavelength_list[i] < 1

    def get_wavelength_data_list(self, row, table_locator):
        data_list = []
        for col in range(2, 5):
            col_text = table_locator.find_element(By.XPATH,
                                                  "//ics-info-list-item//ics-table//div[@class='table']/ul[{}]//li[{}]//li/div".format(
                                                      row, col))

            single_wavelength = TypeConverter.to_float(col_text.text)

            self.logger.info(f"The single wavelength from the table is ==>{single_wavelength}<==")
            data_list.append(single_wavelength)
        return data_list

    def check_for_deviation(self):
        for col in range(2, 5):
            base_locator = "//ics-info-list-item//ics-table//div[@class='table']/ul[2]"
            deviation_wavelength_locator_string = str(base_locator) + "//li[{}]//li/div".format(col)
            deviation_wavelength_locator = (By.XPATH, deviation_wavelength_locator_string)
            time.sleep(1)
            deviation_value = TypeConverter.to_float(self.get_text(deviation_wavelength_locator))
            self.logger.info(f"deviation_value======>>>>{deviation_value}")

            if deviation_value > 1:
                self.logger.info(f"The deviation wavelength locator==>>> {deviation_wavelength_locator}")
                self.logger.info(f"The deviation_value==>>> {deviation_value}")

                assert self.is_state_warning(deviation_wavelength_locator) is True

    def is_state_warning(self, locator):
        value_element = self.get_element(locator)
        value_element_class = value_element.get_attribute('class')
        self.logger.info(f"value_element_class=====>>>>>{value_element_class} ")
        if value_element_class == "value-warning":
            return True
        else:
            return False

    def get_precondition_state(self):
        return [self.get_text(CalibrateWavelengthWorkflowLocators.LAMP_STATE),
                self.get_text(CalibrateWavelengthWorkflowLocators.FLOW_CELL_TYPE)]

    def validate_preflush_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.ADDITIONAL_FLUSH_OPTION_BANNER
        screen_name = "Preflush screen screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flush_control_screen(self):
        locator = CalibrateWavelengthWorkflowLocators.PRE_FLUSH_PAGE_BANNER
        screen_name = "Flow Rate screen"
        self.validate_screen(locator, screen_name, self.wait_time)

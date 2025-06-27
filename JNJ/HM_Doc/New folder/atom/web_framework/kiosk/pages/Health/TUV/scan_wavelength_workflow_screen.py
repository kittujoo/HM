"""
File_Name: scan_wavelength_workflow.py
Desc: This file contains specific user actions on screens within the scan wavelength workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/01/22
__modified__ = "Tyler Prada" added flush option function & page validation functions 10/7/22

"""
import time

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.scan_wavelength_constants import (RecommendedMaterialsForPMTestUsingCuvettes,
                                                                                                 RecommendedMaterialsForPMTestUsingFlowcell,
                                                                                                 RecommendedMaterialsForSampleScanUsingCuvettes,
                                                                                                 RecommendedMaterialsForSampleScanUsingFlowcell,
                                                                                                 ScanWavelengthPreparationForPMTest,
                                                                                                 ScanWavelengthPreparationForSampleScan)
from web_framework.kiosk.pages.Locators.Health.TUV.scan_wavelength_workflow_locators import (ScanWavelengthWelcomeLocators, ScanWavelengthSetupLocators,
                                                                                             PMTestUsingCuvettesLocators, PMTestUsingFlowcellLocators,
                                                                                             SampleScanUsingCuvettes, SampleScanUsingFlowcell,
                                                                                             PreparationLocator, ScanWavelengthFlushOptionLocators)
from web_framework.kiosk.pages.base_page import BasePage


class ScanWavelengthWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_solvent_details = None
        self.selected_wavelength_details = None
        self.selected_frequency_rate_details = None

    def validate_welcome_screen(self):
        locator = ScanWavelengthWelcomeLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_mode_screen(self):
        locator = ScanWavelengthSetupLocators.MODE_PAGE_BANNER
        screen_name = "Mode selection screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_sample_delivery_screen(self):
        locator = ScanWavelengthSetupLocators.SAMPLE_DELIVERY_PAGE_BANNER
        screen_name = "Sample delivery selection screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_tools_materials_screen(self):
        locator = ScanWavelengthSetupLocators.TOOLS_MATERIALS_PAGE_BANNER
        screen_name = "Tools & materials screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preparations_screen(self):
        locator = PreparationLocator.PREPARATION_PAGE_BANNER
        screen_name = "Preparations screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_screen(self):
        locator = PreparationLocator.PRECONDITIONS_PAGE_BANNER
        screen_name = "Preconditions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flow_options_screen(self):
        locator = ScanWavelengthFlushOptionLocators.FLOW_OPTIONS_PAGE_BANNER
        screen_name = "Flush options screen containing flow options"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_first_solvent_selection_screen(self):
        locator = ScanWavelengthFlushOptionLocators.FIRST_SOLVENT_SELECTOR_BANNER
        screen_name = "First solvent selection screen containing flow options"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_second_flow_options_screen(self):
        locator = ScanWavelengthFlushOptionLocators.SECOND_FLOW_OPTIONS_PAGE_BANNER
        screen_name = "Second flush options screen containing flow options"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_second_solvent_selection_screen(self):
        locator = ScanWavelengthFlushOptionLocators.SECOND_SOLVENT_SELECTOR_BANNER
        screen_name = "Second solvent selection screen containing flow options"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(ScanWavelengthWelcomeLocators.WELCOME_PARAGRAPH_ONE),
                self.get_text(ScanWavelengthWelcomeLocators.WELCOME_PARAGRAPH_TWO),
                self.get_text(ScanWavelengthWelcomeLocators.WELCOME_PARAGRAPH_THREE),
                self.get_text(ScanWavelengthWelcomeLocators.WELCOME_PARAGRAPH_FOUR),
                self.get_text(ScanWavelengthWelcomeLocators.WELCOME_PARAGRAPH_FIVE),
                self.get_text(ScanWavelengthWelcomeLocators.WELCOME_PARAGRAPH_SIX)]

    def get_preparation_text(self):
        time.sleep(2)  # TODO Will remove this once the screen is fully implemented
        return [self.get_text(PreparationLocator.LINE_ONE),
                self.get_text(PreparationLocator.LINE_TWO),
                self.get_text(PreparationLocator.LINE_THREE)]

    def get_pm_test_using_cuvettes_text(self):
        return [self.get_text(PMTestUsingCuvettesLocators.LINE_ONE),
                self.get_text(PMTestUsingCuvettesLocators.LINE_TWO),
                self.get_text(PMTestUsingCuvettesLocators.LINE_THREE)]

    def get_pm_test_using_flowcell_text(self):
        return [self.get_text(PMTestUsingFlowcellLocators.LINE_ONE),
                self.get_text(PMTestUsingFlowcellLocators.LINE_TWO),
                self.get_text(PMTestUsingFlowcellLocators.LINE_THREE),
                self.get_text(PMTestUsingFlowcellLocators.LINE_FOUR)]

    def get_sample_scan_using_cuvettes(self):
        time.sleep(2)  # TODO Will remove this once the screen is fully implemented
        return [self.get_text(SampleScanUsingCuvettes.LINE_ONE),
                self.get_text(SampleScanUsingCuvettes.LINE_TWO),
                self.get_text(SampleScanUsingCuvettes.LINE_THREE)]

    def get_sample_scan_using_flowcell(self):
        return [self.get_text(SampleScanUsingFlowcell.LINE_ONE),
                self.get_text(SampleScanUsingFlowcell.LINE_TWO),
                self.get_text(SampleScanUsingFlowcell.LINE_THREE),
                self.get_text(SampleScanUsingFlowcell.LINE_FOUR)]

    def tap_mode(self, mode):
        mode_option_dictionary = {
            "calibration_test": ScanWavelengthSetupLocators.PM_CALIBRATION_TEST,
            "sample_scan": ScanWavelengthSetupLocators.GENERAL_SAMPLE_SCAN

        }

        if mode in mode_option_dictionary:
            self.tap(mode_option_dictionary[mode])
            return

        assert False, f"Unexpected filter time option => {mode}"

    def tap_sample_delivery_option(self, delivery_method):
        mode_option_dictionary = {
            "cuvettes": ScanWavelengthSetupLocators.CUVETTES_SAMPLE_DELIVERY,
            "flow_cell": ScanWavelengthSetupLocators.FLOW_CELL_DELIVERY

        }

        if delivery_method in mode_option_dictionary:
            self.tap(mode_option_dictionary[delivery_method])
            return

        assert False, f"Unexpected filter time option => {delivery_method}"

    # def tap_next_button(self):
    #    self.tap_next_button()

    def validate_recommended_materials_for_pm_test_using_cuvettes(self):
        try:
            time.sleep(1)
            actual_paragraph_text = self.get_pm_test_using_cuvettes_text()
            self.logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

            expected_paragraph_text = RecommendedMaterialsForPMTestUsingCuvettes.expected_pm_test_using_cuvettes_text
            self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
            assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

        finally:
            self.tap_next_button()

    def validate_recommended_materials_for_pm_test_using_flowcell(self):
        try:
            actual_paragraph_text = self.get_pm_test_using_flowcell_text()
            self.logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

            expected_paragraph_text = RecommendedMaterialsForPMTestUsingFlowcell.expected_pm_test_using_flowcell_text
            self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
            assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

        finally:
            self.tap_next_button()

    def validate_recommended_materials_for_sample_scan_using_cuvettes(self):
        try:
            actual_paragraph_text = self.get_sample_scan_using_cuvettes()
            self.logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

            expected_paragraph_text = RecommendedMaterialsForSampleScanUsingCuvettes.expected_sample_scan_test_using_cuvettes_text
            self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
            assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

        finally:
            self.tap_next_button()

    def validate_recommended_materials_for_sample_scan_using_flowcell(self):
        try:
            actual_paragraph_text = self.get_sample_scan_using_flowcell()
            self.logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

            expected_paragraph_text = RecommendedMaterialsForSampleScanUsingFlowcell.expected_sample_scan_test_using_flowcell_text
            self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
            assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

        finally:
            self.tap_next_button()

    def select_solvent_line(self, line):
        solvent_line_dictionary = {
            "A": ScanWavelengthFlushOptionLocators.SOLVENT_LINE_A,
            "B": ScanWavelengthFlushOptionLocators.SOLVENT_LINE_B,
            "C": ScanWavelengthFlushOptionLocators.SOLVENT_LINE_C,
            "D": ScanWavelengthFlushOptionLocators.SOLVENT_LINE_D
        }

        if line in solvent_line_dictionary:
            self.tap(solvent_line_dictionary[line])
            return

        assert False, f"Unexpected solvent line => {line}"

    def validate_preparation_materials_for_pm_test(self):

        try:
            actual_paragraph_text = self.get_preparation_text()
            self.logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

            expected_paragraph_text = ScanWavelengthPreparationForPMTest.scan_wavelength_preparation
            self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
            assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

        finally:
            self.tap_next_button()

    def validate_preparation_materials_for_sample_scan(self):

        try:
            actual_paragraph_text = self.get_preparation_text()
            self.logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

            expected_paragraph_text = ScanWavelengthPreparationForSampleScan.scan_wavelength_preparation
            self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
            assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

        finally:
            self.tap_next_button()

    def select_and_get_wavelength_range(self, min_wavelength, maxi_wavelength):
        self.tap(ScanWavelengthSetupLocators.WAVELENGTH_VALUE)
        self.set_spinner_value(ScanWavelengthSetupLocators.MINI_WAVELENGTH, min_wavelength)
        self.set_spinner_value(ScanWavelengthSetupLocators.MAXI_WAVELENGTH, maxi_wavelength)

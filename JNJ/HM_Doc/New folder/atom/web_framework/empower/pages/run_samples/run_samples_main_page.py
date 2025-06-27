from enum import Enum
from time import time
from typing import Optional

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.logger import Logger
from utilities.timer import timer
from web_framework.empower.pages.run_samples.new_method_set_wizard import NewMethodSetWizard
from web_framework.empower.pages.run_samples.single_injection_tab import SingleInjectionTab
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.web_driver_common.constants import WIN_APP_BY


class SampleRunMode(Enum):
    RunOnly = "Run Only"
    RunAndProcess = "Run and Process"
    RunAndReport = "Run and Report"


class SampleSetRunStatus(Enum):
    ABORTED_INSTRUMENT_IN_USE = "System Idle - Run aborted - Instrument already in use."
    CONFIRMATION_FAILED = "Sample Set - Sample Set confirmation failed."
    PREPARING_FOR_INJECTION = "Sample Set - Preparing For Injection"
    WAITING_FOR_INJECTION = "Sample Set - Waiting for Injection"
    INJECTION_RUNNING = "Sample Set - Injection Running"
    COMPLETE = "System Idle - Sample Set Complete"


SAMPLE_SET_FINALIZING_STATUSES = [SampleSetRunStatus.ABORTED_INSTRUMENT_IN_USE, SampleSetRunStatus.CONFIRMATION_FAILED, SampleSetRunStatus.COMPLETE]


class SingleInjectionPreparationStatus(Enum):
    SETTING_UP = "Single Inject - Setting Up"
    VALIDATING_SAMPLE_SUBMISSION = "Single Inject - Validating sample submission"
    PRESS_INJECT_BUTTON = "Single Inject - Please Press Inject Button"


class SingleInjectionRunStatus(Enum):
    SETTING_UP = "Single Inject - Setting Up"
    INSTRUMENT_FAILURE = "System Idle - Instrument Failure"
    VALIDATING_SAMPLE_SUBMISSION = "System Idle - Validating sample submission"
    SAMPLE_SUBMISSION_FAILED = "System Idle - Sample submission failed."
    ABORTED_INSTRUMENT_IN_USE = "System Idle - Run aborted - Instrument already in use."
    WAITING_FOR_INJECTION = "Single Inject - Waiting for Injection"
    INJECTION_RUNNING = "Single Inject - Injection Running"
    COMPLETE = "System Idle - Single Inject Complete"


SINGLE_INJECTION_FINALIZING_STATUSES = [SingleInjectionRunStatus.ABORTED_INSTRUMENT_IN_USE, SingleInjectionRunStatus.SAMPLE_SUBMISSION_FAILED,
                                        SingleInjectionRunStatus.INSTRUMENT_FAILURE]


class RunSamplesMainPage(WinAppBasePage):
    INSTRUMENT_NEXT_BUTTON_LOCATOR = (WIN_APP_BY, '12324')

    # Text fields
    RUN_STATUS_TEXT_FIELD_LOCATOR = (By.XPATH, '//StatusBar/Text[3]')
    TOTAL_SAMPLES_TIME_REMAINING_TEXT_FIELD_LOCATOR = (WIN_APP_BY, "20547")
    SAMPLE_SET_TIME_REMAINING_TEXT_FIELD_LOCATOR = (WIN_APP_BY, "20548")

    def __init__(self, driver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)
        self._single_injection_tab: Optional[SingleInjectionTab] = None
        self._new_method_set_window: Optional[NewMethodSetWizard] = None

    @property
    def single_injection_tab(self) -> SingleInjectionTab:
        if not self._single_injection_tab:
            self._single_injection_tab = SingleInjectionTab(self._driver)
        return self._single_injection_tab

    @property
    def new_method_set_wizard(self) -> NewMethodSetWizard:
        if not self._new_method_set_window:
            self._new_method_set_window = NewMethodSetWizard(self._driver)
        return self._new_method_set_window

    def click_file_menu(self):
        # TODO: investigate why menu interaction is failing
        # file_menu = self.find_element((By.NAME,'File'))
        # file_menu.click()
        ActionChains(self._driver).key_down(Keys.ALT).send_keys("F").perform()

    def select_new_sample_set_method_menu_item(self):
        ActionChains(self._driver).send_keys("N").perform()

    def select_using_sample_set_wizard_menu_item(self):
        ActionChains(self._driver).send_keys("W").perform()

    def select_create_sample_using_wizard(self):
        self.click_on_element((WIN_APP_BY, '15280'))

    def click_next(self):
        self.click_on_element(self.INSTRUMENT_NEXT_BUTTON_LOCATOR)

    def click_message_center_button(self):
        self.save_page_source()
        self.click_on_element((By.XPATH, "//Button[@Name='Paste']/following-sibling::Button"))

    def select_sample_set_method_type(self, sample_set_method_type, dissolution_type=None):
        self.click_on_element((By.NAME, sample_set_method_type))
        if dissolution_type:
            self.click_on_element((By.NAME, dissolution_type))

    def select_standard_injections_location(self, standard_injections_location):
        self.click_on_element((By.NAME, standard_injections_location))

    def describe_sample_information(self, samples_number, injections_number, injection_volume, run_time):
        number_of_samples_textbox = self.find_element((WIN_APP_BY, '15244'))
        number_of_samples_textbox.send_keys(samples_number)

        number_of_injections_textbox = self.find_element((WIN_APP_BY, '15245'))
        number_of_injections_textbox.send_keys(injections_number)

        injection_volume_textbox = self.find_element((WIN_APP_BY, '15221'))
        injection_volume_textbox.send_keys(injection_volume)

        run_time_textbox = self.find_element((WIN_APP_BY, '15226'))
        run_time_textbox.send_keys(run_time)

    def create_new_method_set(self):
        self.click_on_element((WIN_APP_BY, '15273'))
        self.click_on_element((WIN_APP_BY, '5046'))

    def select_instrument_method_from_dialog(self, method_name):
        self.click_on_element((WIN_APP_BY, "20306"))
        self.click_on_element((By.XPATH, f"//ListItem[@Name='{method_name}']"))

    def set_combobox_value(self, column_name):
        self.click_on_element((By.XPATH, "//ComboBox[@AutomationId='15385']"))
        action = ActionChains(self._driver)
        column_name_item = self.find_element((By.XPATH, f"//ListItem[@Name='{column_name}']"))
        action.move_to_element(column_name_item)
        action.click()
        action.perform()

    def set_sample_name(self, sample_name=None, incrementing_prefix=None, incrementing_suffix=None):
        if sample_name:
            sample_name_input = self.find_element((WIN_APP_BY, '15242'))
            sample_name_input.clear()
            sample_name_input.send_keys(sample_name)
        if incrementing_prefix:
            incrementing_prefix_input = self.find_element((WIN_APP_BY, '15177'))
            incrementing_prefix_input.clear()
            incrementing_prefix_input.send_keys(incrementing_prefix)
        if incrementing_suffix:
            sample_name_input = self.find_element((WIN_APP_BY, '15179'))
            sample_name_input.clear()
            sample_name_input.send_keys(incrementing_suffix)

    def set_solvent(self, solvent):
        solvent_input = self.find_element((WIN_APP_BY, '15241'))
        solvent_input.clear()
        solvent_input.send_keys(solvent)

    def select_run_mode(self, run_mode):
        self.click_on_element((By.NAME, run_mode))

    def select_load_samples_menu_item(self):
        self.click_on_element((WIN_APP_BY, '20299'))

    def select_load_using_previously_create_sample(self):
        self.click_on_element((WIN_APP_BY, '20247'))

    def select_sample_set_name(self, sample_set_name):
        self.click_on_element((By.XPATH, f"//ListItem[contains(@Name, '{sample_set_name}')]"))

    def confirm_load_sample(self):
        self.click_on_element((WIN_APP_BY, '6189'))

    def click_run_button(self):
        self.click_on_element((By.NAME, 'Run'))

    def click_run_window_run_button(self):
        self.click_on_element((WIN_APP_BY, '20476'))

    def select_sample_run_mode(self, sample_run_mode: SampleRunMode):
        self.click_on_element((By.XPATH, "//Window[@Name='Run Sample Set']//ComboBox[@AutomationId='20465']"))
        action = ActionChains(self._driver)
        sample_mode_item = self.find_element((By.XPATH, f"//ListItem[@Name='{sample_run_mode.value}']"))
        action.move_to_element(sample_mode_item)
        action.click()
        action.perform()

    def set_sample_set_name(self, sample_set_name):
        sample_set_name_input = self.find_element((WIN_APP_BY, '20309'))
        sample_set_name_input.send_keys(sample_set_name)

    def wait_run_started(self, preparation_timeout):
        start_time = time()
        current_status = ""

        while time() - start_time <= preparation_timeout:
            status = self.get_run_status()
            if current_status != status:
                current_status = status
                self._logger.debug(f"Run status update: '{current_status}'")

            if status == SampleSetRunStatus.INJECTION_RUNNING.value:
                return
            if status in [SampleSetRunStatus.CONFIRMATION_FAILED.value, SampleSetRunStatus.ABORTED_INSTRUMENT_IN_USE.value]:
                raise ValueError(f"System failed to run samples: '{status}'")

        raise ValueError(f"System failed to start running samples within {preparation_timeout} seconds")

    def wait_run_finished(self, running_timeout) -> str:
        preparation_timeout = 300
        self.wait_run_started(preparation_timeout)

        start_time = time()
        current_status = ""

        while True:
            status = self.get_run_status()
            if current_status != status:
                current_status = status
                self._logger.debug(f"Run status update: '{current_status}'")

            if status == SampleSetRunStatus.INJECTION_RUNNING.value:
                while time() - start_time <= running_timeout:
                    status = self.get_run_status()
                    if current_status != status:
                        current_status = status
                        self._logger.debug(f"Run status update: '{current_status}'")

                    if status in [SampleSetRunStatus.CONFIRMATION_FAILED.value, SampleSetRunStatus.ABORTED_INSTRUMENT_IN_USE.value,
                                  SampleSetRunStatus.COMPLETE.value]:
                        return status
                break
        assert False, f"System run still in progress after {running_timeout} seconds, last status was: [{status}]"

    def get_run_status(self) -> str:
        return self.get_text(self.RUN_STATUS_TEXT_FIELD_LOCATOR)

    def get_total_sample_time_remaining(self):
        return self.get_text(self.TOTAL_SAMPLES_TIME_REMAINING_TEXT_FIELD_LOCATOR)

    def get_sample_set_time(self):
        return self.get_text(self.SAMPLE_SET_TIME_REMAINING_TEXT_FIELD_LOCATOR)

    def is_error_popup_displayed(self):
        return self.is_displayed_with_timeout(10, (By.NAME, 'Error'))

    def click_view_menu(self):
        ActionChains(self._driver).key_down(Keys.ALT).send_keys("V").perform()

    def click_create_new_instrument_method(self):
        create_new_button = self._driver.find_element(WIN_APP_BY, '5046')  # this is duplicated, need some refactor to optimize
        create_new_button.click()

    def wait_single_injection_preparation_finished(self, timeout: int) -> str:
        status = ""
        current_status = ""

        tmr = timer(timeout).start()
        while tmr:
            status = self.get_run_status()
            if current_status != status:
                current_status = status
                self._logger.debug(f"Single Injection preparation status update: '{status}'")

            if status == SingleInjectionPreparationStatus.PRESS_INJECT_BUTTON.value:
                self._logger.debug(f"Single Injection preparation final status: '{status}'")
                return status

            if status == SampleSetRunStatus.ABORTED_INSTRUMENT_IN_USE.value:
                raise ValueError(f"System failed to prepare single injection: '{status}'")

        assert False, f"Single Injection Preparation still in progress after {timeout} seconds, last status was: [{status}]"

    def click_inject_button(self):
        prepare_button = self._driver.find_element(WIN_APP_BY, '20501')
        prepare_button.click()

    def wait_for_single_injection_run_status(self, expected_status: SingleInjectionRunStatus, timeout: int):
        previous_status = None

        tmr = timer(timeout).start()
        while True:
            current_status = SingleInjectionRunStatus(self.get_run_status())
            if previous_status != current_status:
                previous_status = current_status
                self._logger.debug(f"Current injection status is: '{previous_status}'")

            if current_status == expected_status:
                return current_status
            elif current_status in SINGLE_INJECTION_FINALIZING_STATUSES:
                self._logger.debug(f"Run status [{previous_status.value}] is one of finalizing, no sense to wait anymore")
                assert False, f"Run samples finished with one of finalizing status: '{current_status.value}'"
            assert tmr, f"Injection run still in progress after {timeout} seconds, last status was: [{current_status.value}]"

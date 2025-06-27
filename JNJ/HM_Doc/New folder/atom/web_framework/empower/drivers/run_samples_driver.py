import time
from typing import Optional, Callable, Union

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from fixtures_win_app_driver import WinAppDriverHandler
from utilities.assert_timeout import AssertTimeout
from utilities.constants import EMPOWER_BIN_FOLDER
from utilities.logger import Logger
from utilities.string_utility import str_to_seconds, str_to_bool
from web_framework.empower.pages.common.common_login_page import CommonLoginScreen
from web_framework.empower.pages.method_editor.instrument_method_editor import InstrumentMethodEditorPage
from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient
from web_framework.empower.pages.run_samples.control_panel_web import ControlPanel
from web_framework.empower.pages.run_samples.run_samples_main_page import RunSamplesMainPage, SampleRunMode, SingleInjectionRunStatus
from web_framework.empower.pages.run_samples.run_samples_tabs import RunSamplesTabs
from web_framework.empower.pages.run_samples.sample_set_method import SampleSetMethodPage
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.web_driver_common.element import is_displayed_with_timeout


class RunSamplesDriver:
    NEW_METHOD_WIZARD_OVERWRITE_PAGE_LOCATOR = (By.XPATH, "//Window[@Name='Run Samples']")

    @property
    def _driver(self):
        if not self.__driver:
            raise ValueError("Application was not initialized, run login method to start application")
        return self.__driver

    @_driver.setter
    def _driver(self, value):
        self.__driver = value

    @property
    def run_samples_page(self):
        if not self._run_samples_main_page:
            driver = self._win_app_driver_handler.attach_to_running_application("- Run Samples")
            self._run_samples_main_page = RunSamplesMainPage(driver)
        return self._run_samples_main_page

    @property
    def run_samples_tabs(self):
        if not self._run_samples_tabs:
            self._run_samples_tabs = RunSamplesTabs(self._driver, self._miltest_rest_client_creator)
        return self._run_samples_tabs

    @property
    def control_panel(self) -> ControlPanel:
        if not self._control_panel:
            self._control_panel = ControlPanel(self._driver, self._assert_timeout)
        return self._control_panel

    @property
    def instrument_method(self) -> InstrumentMethodEditorPage:
        if not self._instrument_method:
            self._instrument_method = InstrumentMethodEditorPage(self._driver)
        return self._instrument_method

    def __init__(self, win_app_driver_handler: WinAppDriverHandler, miltest_rest_client_creator: Callable[[str], MiltestRestClient],
                 assert_timeout: AssertTimeout):
        self._logger = Logger(self.__class__.__name__)
        self._win_app_driver_handler = win_app_driver_handler
        self._miltest_rest_client_creator = miltest_rest_client_creator
        self._executable_path = f"{EMPOWER_BIN_FOLDER}\\QuickSet.exe"
        self._sample_set_time = None
        self.__driver = None
        self._control_panel: Optional[ControlPanel] = None
        self._assert_timeout = assert_timeout
        self._run_samples_tabs: Optional[RunSamplesTabs] = None
        self._run_samples_main_page: Optional[RunSamplesMainPage] = None
        self._instrument_method: Optional[InstrumentMethodEditorPage] = None

    def login_to_project(self, project_name, username, password, system_name):
        login_app = self._win_app_driver_handler.start_application(self._executable_path)
        login_page = CommonLoginScreen(login_app)
        login_page.enter_project(project_name)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.press_ok()

        # TODO: we don't need yet to support multiple configured systems and this is causing a delay when executing tests
        # chromatographic_selection = ChromatographicSelectionPage(self._driver)
        # if chromatographic_selection.is_system_selection_opened():
        #     chromatographic_selection.select_system(system_name)
        #     chromatographic_selection.press_ok()

        self._driver = self._win_app_driver_handler.attach_to_running_application(f"in {project_name} as System/Administrator - Run Samples")

    def load_created_sample_set(self, sample_set_name):
        self.run_samples_page.click_file_menu()
        self.run_samples_page.select_load_samples_menu_item()
        self.run_samples_page.select_load_using_previously_create_sample()
        self.run_samples_page.press_ok()
        self.run_samples_page.select_sample_set_name(sample_set_name)
        self.run_samples_page.confirm_load_sample()
        time.sleep(5)  # missing Empower tables support for validating samples are loaded

    def run_sample_set(self, run_mode: SampleRunMode, sample_set_name=None):
        self._sample_set_time = str_to_seconds(self.run_samples_page.get_sample_set_time())
        self.run_samples_page.click_run_button()
        if sample_set_name:
            self.run_samples_page.set_sample_set_name(sample_set_name)
        self.run_samples_page.select_sample_run_mode(run_mode)
        self.run_samples_page.click_run_window_run_button()
        if self.run_samples_page.is_error_popup_displayed():
            self.run_samples_page.press_ok_by_name()

    def validate_run_status(self, expected_status, running_timeout_buffer_in_seconds):
        """
        Waits for the pre-setup to complete, it will identify the expected runtime
        (with some configurable extra wait time) and will wait for completion
        :param expected_status: The status expected at the end of the run
        :param running_timeout_buffer_in_seconds: Number of extra seconds to wait in case
        Run Samples does not finish within the expected calculated runtime
        """
        running_timeout = self._sample_set_time + running_timeout_buffer_in_seconds
        self._logger.debug(f"Maximum wait time: {running_timeout} seconds. Expected runtime: {self._sample_set_time} (s) + "
                           f"Extra added wait time:{running_timeout_buffer_in_seconds} (s).")
        actual_status = self.run_samples_page.wait_run_finished(running_timeout)
        assert actual_status == expected_status, f"Wrong run samples status, expected [{expected_status}] but was [{actual_status}]"

    def validate_intermediate_run_status(self, expected_status, wait_time=WaitTimeConstants.LongWait):
        """
        Waits for the intermediate run status. i.e. "Sample Set - Wet Prime"
        Args:
            expected_status (str): The status expected at the end of the run
            wait_time (int): Number of seconds to wait for status to occur
        """
        self._assert_timeout.are_equal(self.run_samples_page.get_run_status, expected_status, message="Wrong run samples run status",
                                       timeout_in_seconds=wait_time,
                                       polling_period_in_seconds=1)

    def create_new_sample_set(self):
        self.run_samples_page.click_file_menu()
        self.run_samples_page.select_new_sample_set_method_menu_item()

    def select_new_sample_method_creation(self):
        self.run_samples_page.select_using_sample_set_wizard_menu_item()
        self.run_samples_page.click_next()

    def select_sample_method_type(self, sample_set_method_type, dissolution_type):
        self.run_samples_page.select_sample_set_method_type(sample_set_method_type, dissolution_type)
        self.run_samples_page.click_next()

    def select_location_of_standard_injections(self, standard_injections_location):
        self.run_samples_page.select_standard_injections_location(standard_injections_location)
        self.run_samples_page.click_next()

    def describe_samples(self, samples_number, injections_number, injection_volume, run_time):
        self.run_samples_page.describe_sample_information(samples_number, injections_number, injection_volume, run_time)
        self.run_samples_page.create_new_method_set()

    def is_overwrite_dialog_opened(self):
        return is_displayed_with_timeout(self._win_app_driver_handler.win_app_root_driver, self.NEW_METHOD_WIZARD_OVERWRITE_PAGE_LOCATOR, 3)

    def select_instrument_method(self):
        new_method_wizard = self.run_samples_page.new_method_set_wizard
        new_method_wizard.select_instrument_method()
        new_method_wizard.select_default_method()
        new_method_wizard.click_finish()

        if self.is_overwrite_dialog_opened():
            ActionChains(self._win_app_driver_handler.win_app_root_driver).send_keys("Y").perform()
        # new_method_wizard.click_next()

    def select_instrument_method_from_dialog(self, method_name):
        self.run_samples_page.select_instrument_method_from_dialog(method_name)

    # TODO method should be refactored, all default values should be removed
    def identify_standards(self, column_name=None, serial_number=None, sample_matrix=None, sample_name=None,
                           incrementing_prefix=None, incrementing_suffix=None, solvent=None):
        if column_name:
            self.run_samples_page.set_combobox_value(column_name)
        self.run_samples_page.click_next()
        if serial_number:
            self.run_samples_page.set_combobox_value(serial_number)
        self.run_samples_page.click_next()
        if sample_matrix:
            self.run_samples_page.set_combobox_value(sample_matrix)
        self.run_samples_page.click_next()
        self.run_samples_page.set_sample_name(sample_name, incrementing_prefix, incrementing_suffix)
        self.run_samples_page.click_next()
        if solvent:
            self.run_samples_page.set_solvent(solvent)
        self.run_samples_page.click_next()

    def select_runtime_option(self, run_mode):
        self.run_samples_page.select_run_mode(run_mode)
        self.run_samples_page.click_next()

    def confirm_sample_set_method_summary(self):
        self.run_samples_page.new_method_set_wizard.confirm_set_method_summary()
        self.run_samples_page.new_method_set_wizard.click_finish()

    def confirm_component_editor(self):
        self.run_samples_page.press_ok_by_name()

    def create_new_single_injection(self, sample_set_name: str, function_type: str, plate: str, injection_volume: Union[int, float],
                                    run_time: Union[int, float]):
        single_injection = self.run_samples_page.single_injection_tab
        single_injection.set_sample_name(sample_set_name)
        single_injection.select_function(function_type)
        single_injection.set_plate(plate)
        single_injection.set_injection_volume(injection_volume)
        single_injection.set_run_time(run_time)

    def create_instrument_method(self):
        self.run_samples_page.single_injection_tab.click_develop_methods_button()
        self.run_samples_page.new_method_set_wizard.click_create_new_instrument_method()

    def prepare_single_injection(self):
        self.run_samples_page.single_injection_tab.click_prepare_button()

    def validate_single_injection_preparation_status(self, expected_status, timeout):
        self._logger.debug(f"Maximum wait time: {timeout} seconds.")
        actual_status = self.run_samples_page.wait_single_injection_preparation_finished(timeout)
        assert actual_status == expected_status, f"Wrong Single Injection preparation status, expected [{expected_status}] but was [{actual_status}]"

    def run_single_injection(self):
        self._sample_set_time = str_to_seconds(self.run_samples_page.get_total_sample_time_remaining())
        self.run_samples_page.single_injection_tab.click_inject_button()

    def validate_single_injection_run_status(self, expected_status: SingleInjectionRunStatus, timeout: int):
        running_timeout = timeout + self._sample_set_time
        self._logger.debug(f"Maximum wait time: {running_timeout} seconds.")
        self.run_samples_page.wait_for_single_injection_run_status(expected_status, running_timeout)

    def set_sample_runtime(self, row: int, value: str):
        self.run_samples_tabs.samples_tab.set_runtime(row, value)

    def save_sample_set_method(self, name: str, comments: str = None):
        sample_set_page = SampleSetMethodPage(self._driver)
        sample_set_page.click_toolbar_save_button()
        sample_set_page.set_current_sample_set_name(name)
        if comments:
            sample_set_page.set_current_sample_set_comments(comments)
        sample_set_page.click_dialog_save_button()
        if sample_set_page.is_overwrite_dialog_opened():
            sample_set_page.press_yes_by_name()

    def validate_control_panel_flow_rate_equal_to(self, expected_rate: str):
        self._assert_timeout.are_equal(lambda: self.control_panel.get_flow_rate_value(), expected_rate, "Unexpected Control Panel flow rate",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_control_panel_lamp_state(self, state: bool):
        self._assert_timeout.are_equal(lambda: str_to_bool(self.control_panel.get_lamp_state()), state, "Unexpected Control Panel lamp state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_sample_temperature(self, expected_value: float):
        self._assert_timeout.value_is_within_tolerance(lambda: float(self.control_panel.get_sample_temperature_value()), expected_value, tolerance=0.1,
                                                       message="Unexpected Control Panel sample temperature",
                                                       timeout_in_seconds=WaitTimeConstants.SmallWait)

    def validate_column_temperature(self, expected_value: float):
        self._assert_timeout.value_is_within_tolerance(lambda: float(self.control_panel.get_column_temperature_value()), expected_value, tolerance=0.1,
                                                       message="Unexpected Control Panel column temperature",
                                                       timeout_in_seconds=WaitTimeConstants.SmallWait)

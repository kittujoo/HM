from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from fixtures_win_app_driver import WinAppDriverHandler
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.string_utility import str_to_bool
from web_framework.empower.pages.configuration.console_commands_page import ConsoleCommandsPage
from web_framework.empower.pages.configuration.console_page import ConsoleHomePage, ConsoleBasePage
from web_framework.empower.pages.configuration.console_setup_page import ConsoleSetupPage
from web_framework.web_driver_common.element import assert_element_visible


class ConsoleDriver:
    __driver_field: Optional[WebDriver] = None

    @property
    def _driver(self):
        if not self.__driver_field:
            self.__driver_field = self._win_app_driver_handler.attach_to_running_application_by_xpath("//Window[contains(@Name,'Console')]")
        return self.__driver_field

    @property
    def console_base_page(self) -> ConsoleBasePage:
        if not self._console_base_page:
            self._console_base_page = ConsoleBasePage(self._driver)
        return self._console_base_page

    @property
    def console_home_page(self) -> ConsoleHomePage:
        if not self._console_home_page:
            self._console_home_page = ConsoleHomePage(self._driver)
        return self._console_home_page

    @property
    def console_setup_page(self) -> ConsoleSetupPage:
        if not self._console_setup_page:
            self._console_setup_page = ConsoleSetupPage(self._driver)
        return self._console_setup_page

    @property
    def console_cmd_page(self) -> ConsoleCommandsPage:
        if not self._console_cmd_page:
            self._console_cmd_page = ConsoleCommandsPage(self._driver)
        return self._console_cmd_page

    def __init__(self, win_app_driver_handler: WinAppDriverHandler, assert_timeout: AssertTimeout):
        self._win_app_driver_handler = win_app_driver_handler
        self._assert_timeout = assert_timeout
        self._console_base_page = None
        self._console_home_page = None
        self._console_setup_page = None
        self._console_cmd_page = None

    def is_flow_enabled(self) -> bool:
        status = self.flow_state_text()
        if status == "Flow On":
            return True
        elif status == "Flow Off":
            return False
        else:
            raise ValueError(f"Invalid console command page flow state: [{status}]")

    def is_lamp_enabled(self) -> bool:
        status = False if self.console_cmd_page.is_lamp_off() else True
        return status

    def set_flow(self, flow_state: bool):
        current_state = self.is_flow_enabled()
        if current_state == flow_state:
            return
        self.console_cmd_page.click_on_flow_rate_button()
        self.validate_dialog_opened()
        self.console_cmd_page.press_continue_by_name()

    def set_lamp_state(self, lamp_state: bool):
        current_state = self.is_lamp_enabled()
        if current_state == lamp_state:
            return
        self.console_cmd_page.click_on_lamp_button()
        self.validate_dialog_opened()
        self.console_cmd_page.press_continue_by_name()

    def flow_state_text(self) -> str:
        return self.console_cmd_page.get_control_flow_state_text()

    def reset_system(self):
        self.console_cmd_page.system_reset_command()
        self.validate_dialog_opened()
        self.console_cmd_page.press_continue_by_name()

    def select_shutdown_option(self):
        self.console_setup_page.click_shutdown()
        self.validate_dialog_opened()
        self.console_setup_page.press_continue_by_name()

    def validate_commands_tab_opened(self):
        locator = (By.XPATH, '//*[contains(@Name, "Flow")]')
        assert_element_visible(self._driver, locator, "Commands Tab")

    def validate_home_tab_opened(self):
        locator = (By.XPATH, '//*[contains(@Name, "Composition")]')
        assert_element_visible(self._driver, locator, "Home Tab")

    def validate_setup_tab_opened(self):
        locator = (By.XPATH, "//Image[@Name='ics-img-play.svg'][2]")
        assert_element_visible(self._driver, locator, "Setup Tab")

    def validate_dialog_opened(self):
        locator = (By.XPATH, '//*[contains(@Name, "Continue")]')
        assert_element_visible(self._driver, locator, "Confirmation Dialog")

    def validate_console_opened(self):
        locator = (By.XPATH, '//Document')
        assert_element_visible(self._driver, locator, "Console Window")

    def validate_active_text(self, text):
        locator = (By.XPATH, f'//Text[contains(@Name, "{text}")]')
        assert_element_visible(self._driver, locator, "Active Text Element")

    def validate_system_state(self, expected_state: str):
        self._assert_timeout.are_equal(lambda: self.console_home_page.get_system_state(), expected_state, "Unexpected Console system state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_control_flow_rate_equal_to(self, expected_state: str):
        self._assert_timeout.are_equal(lambda: self.console_home_page.get_flow_value(), expected_state, "Unexpected Console flow rate",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_control_flow_not_equal_to(self, expected_state: str):
        self._assert_timeout.are_not_equal(lambda: self.console_home_page.get_flow_value(), expected_state, "Unexpected Console flow rate",
                                           timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_control_flow_state_equal_to(self, expected_state: str):
        self._assert_timeout.are_equal(lambda: self.console_cmd_page.get_control_flow_state_text(), expected_state, "Unexpected Console flow state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_lamp_state(self, state: bool):
        self._assert_timeout.are_equal(lambda: str_to_bool(self.console_home_page.get_lamp_state_value().lower()), state, "Unexpected console lamp state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_sample_temperature_state(self, state: bool):
        sample_temperature_text = self.console_home_page.get_sample_temperature_state()
        assert ("Setpoint" in sample_temperature_text) == state, (f"Unexpected sample temperature state in console home page. Expected: {state}, "
                                                                  f"Actual : {sample_temperature_text}")

    def validate_column_temperature_state(self, state: bool):
        column_temperature_text = self.console_home_page.get_column_temperature_state()
        assert ("Setpoint" in column_temperature_text) == state, (f"Unexpected column temperature state in console home page. Expected: {state}, "
                                                                  f"Actual : {column_temperature_text}")

    def validate_commands_page_lamp_state(self, state: bool):
        self._assert_timeout.are_equal(lambda: self.console_cmd_page.get_control_lamp_state(), state, "Unexpected console commands page lamp state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_commands_page_flow_state(self, state: bool):
        self._assert_timeout.are_equal(lambda: self.is_flow_enabled(), state, "Unexpected console commands page flow state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_sample_temperature(self, expected_state: str):
        if expected_state.isnumeric():
            expected_state = f"({expected_state}.0 °c setpoint)"
        else:
            expected_state = f"({expected_state.lower()})"
        self._assert_timeout.are_equal(lambda: self.console_home_page.get_sample_temperature_state().capitalize(), expected_state,
                                       "Unexpected Sample Temperature State",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

    def validate_column_temperature(self, expected_state: str):
        if expected_state.isnumeric():
            expected_state = f"({expected_state}.0 °c setpoint)"
        else:
            expected_state = f"({expected_state.lower()})"
        self._assert_timeout.are_equal(lambda: self.console_home_page.get_column_temperature_state().capitalize(), expected_state,
                                       "Unexpected Column Temperature State",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)

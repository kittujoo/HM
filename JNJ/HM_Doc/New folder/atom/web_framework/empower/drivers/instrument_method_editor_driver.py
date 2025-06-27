from time import sleep
from typing import Optional

from fixtures_win_app_driver import WinAppDriverHandler
from utilities.constants import EMPOWER_BIN_FOLDER
from utilities.logger import Logger
from utilities.string_utility import str_to_bool
from web_framework.empower.pages.common.common_login_page import CommonLoginScreen
from web_framework.method_editor.pages.method_editor_main_page import MethodEditorMainPage


class InstrumentMethodEditorDriver:

    def __init__(self, win_app_driver_handler: WinAppDriverHandler):
        self._logger = Logger(self.__class__.__name__)
        self._win_app_driver_handler = win_app_driver_handler
        self._executable_path = f"{EMPOWER_BIN_FOLDER}\\InEditor.exe"
        self._method_editor_page: Optional[MethodEditorMainPage] = None

    @property
    def method_editor_page(self):
        if not self._method_editor_page:
            driver = self._win_app_driver_handler.attach_to_running_application("- Instrument Method Editor")
            self._method_editor_page = MethodEditorMainPage(driver)
        return self._method_editor_page

    def login_to_project(self, project_name, username, password, system_name=None) -> MethodEditorMainPage:
        driver = self._win_app_driver_handler.start_application(self._executable_path)
        login_page = CommonLoginScreen(driver)
        login_page.enter_project(project_name)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.press_ok()
        self.method_editor_page.validate_opened()
        return self.method_editor_page

    def save_method(self, method_name, method_comment=None):
        self._method_editor_page.click_save_toolbar_button()
        save_method_window = self._method_editor_page.save_method_window
        save_method_window.set_method_name(method_name)
        if method_comment:
            save_method_window.set_method_comment(method_comment)

        save_method_window.click_dialog_save_button()
        if save_method_window.is_overwrite_dialog_opened():
            save_method_window.press_yes_by_name()

    def open_method(self, method_name: str):
        self._method_editor_page.click_open_toolbar_button()
        save_method_page = self._method_editor_page.save_method_window
        if save_method_page.is_save_dialog_displayed():
            save_method_page.click_unsaved_changes_dialog_no_button()
        save_method_page.set_method_name(method_name)
        save_method_page.click_dialog_open_button()
        if save_method_page.is_discard_dialog_displayed():
            save_method_page.press_yes_by_name()
        sleep(2)

    def close_method(self):
        self._method_editor_page.click_delete_toolbar_button()

    def is_cannot_save_method_dialog_opened(self):
        return self._method_editor_page.save_method_window.is_cannot_save_method_dialog_opened()

    def is_save_method_button_enabled(self):
        return self._method_editor_page.is_save_method_button_enabled()

    def setup_instrument_method(self):
        page = self.method_editor_page
        data_channels = page.left_panel.system.open_data_channels()
        data_channels.toggle_ambient_temperature()
        data_channels.toggle_system_pressure()
        data_channels.toggle_flow_rate()
        data_channels.toggle_percent_solvent_a()

    def export_to_json(self, file_path):
        main_page = self.method_editor_page
        main_page.click_hamburger_menu()
        file_save_page = main_page.click_export_to_json()
        file_save_page.set_file_path(file_path)
        file_save_page.click_save()

    def set_column_temperature(self, state: str):
        page = self.method_editor_page
        column_temperature = page.left_panel.column_compartment.open_column_temperature()
        state_to_set = str_to_bool(state) if not state.isnumeric() else True
        column_temperature.toggle_column_temperature(state_to_set)
        if state_to_set:
            column_temperature.set_setpoint(state)

    def set_sample_temperature(self, state: str):
        page = self.method_editor_page
        sample_temperature_page = page.left_panel.sample_manager.open_sample_temperature()
        state_to_set = str_to_bool(state) if not state.isnumeric() else True
        sample_temperature_page.toggle_sample_temperature(state_to_set)
        if state_to_set:
            sample_temperature_page.set_setpoint(state)

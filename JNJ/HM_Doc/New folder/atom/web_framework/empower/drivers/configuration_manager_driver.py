from fixtures_win_app_driver import WinAppDriverHandler
from utilities.constants import EMPOWER_BIN_FOLDER
from utilities.logger import Logger
from web_framework.empower.pages.common.common_login_page import CommonLoginScreen
from web_framework.empower.pages.configuration.main_configuration_page import MainConfigurationPage
from web_framework.empower.pages.configuration.system_creation_wizard import NewSystemWizardPage


class ConfigurationManagerDriver:
    @property
    def _driver(self):
        if not self.__driver:
            raise ValueError("Application was not initialized, run login method to start application")
        return self.__driver

    @_driver.setter
    def _driver(self, value):
        self.__driver = value

    def __init__(self, win_app_driver_handler: WinAppDriverHandler):
        self._logger = Logger(self.__class__.__name__)
        self._win_app_driver_handler: WinAppDriverHandler = win_app_driver_handler
        self._executable_path = f"{EMPOWER_BIN_FOLDER}\\cmgr.exe"
        self.__driver = None

    def login_to_project(self, username, password):
        self.__driver = self._win_app_driver_handler.start_application(self._executable_path)
        login_page = CommonLoginScreen(self.__driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.press_ok()

        self.__driver = self._win_app_driver_handler.attach_to_running_application("System/Administrator - Configuration Manager")

    def create_new_system(self, system_name, instruments_name):
        configuration_page = MainConfigurationPage(self.__driver)
        configuration_page.click_new_system()

        wizard = NewSystemWizardPage(self.__driver)

        # TODO: we don't need yet to support multiple configured systems and this is causing a delay when executing tests
        # if wizard.is_new_chromatographic_type_entry_wizard_displayed():
        #     wizard.select_create_new_system_rb()
        #     wizard.click_next()
        #     wizard.click_next()
        wizard.add_instruments_to_system(instruments_name)
        wizard.click_next()
        wizard.set_sharing_with_world()
        wizard.click_next()
        wizard.set_system_name(system_name)
        wizard.click_finish()
        if wizard.is_duplicated_system_windows_exists():
            wizard.press_ok_by_name()
        wizard.confirm_system_online()

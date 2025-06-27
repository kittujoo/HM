import os
from typing import Optional, Callable

from fixtures_win_app_driver import WinAppDriverHandler
from utilities.constants import EMPOWER_BIN_FOLDER
from utilities.logger import Logger
from web_framework.empower.pages.common.common_login_page import CommonLoginScreen
from web_framework.empower.pages.common.select_project_window_page import SelectProjectWindowPage
from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient
from web_framework.empower.pages.project.injections_tab import TableColumnNames, InjectionsTab
from web_framework.empower.pages.project.project_main_page import ProjectMainPage

logger = Logger(os.path.basename(__file__))


class ProjectDriver:

    def __init__(self, win_app_driver_handler: WinAppDriverHandler, miltest_rest_client_creator: Callable[[str], MiltestRestClient]):
        self._win_app_driver_handler = win_app_driver_handler
        self._executable_path = f"{EMPOWER_BIN_FOLDER}\\project.exe"
        self._miltest_rest_client_creator = miltest_rest_client_creator
        self._project_main_page: Optional[ProjectMainPage] = None

    @property
    def project_main_page(self) -> ProjectMainPage:
        if not self._project_main_page:
            driver = self._win_app_driver_handler.attach_to_running_application("- Project")
            self._project_main_page = ProjectMainPage(driver, self._miltest_rest_client_creator)
        return self._project_main_page

    def login_to_project(self, username, password, project_name):
        driver = self._win_app_driver_handler.start_application(self._executable_path)
        login_page = CommonLoginScreen(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.press_ok()

        driver = self._win_app_driver_handler.attach_to_running_application("Select Project(s)")
        select_project_page = SelectProjectWindowPage(driver)
        select_project_page.select_project(project_name)
        select_project_page.press_ok()

    def select_injections_tab(self) -> InjectionsTab:
        return self.project_main_page.open_injections()

    def open_preview_publisher(self, row: int, column_name: TableColumnNames):
        injections_tab = self.project_main_page.open_injections()
        injections_tab.right_click_cell(row, column_name.value)
        injections_tab.select_preview_publisher_menu_item()

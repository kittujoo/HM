from typing import Tuple

from selenium.webdriver.common.by import By

from utilities.logger import Logger
from web_framework.empower.pages.common.file_save_page import FileSavePage, FileSavePageLocators, FileType
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.web_driver_common.constants import WIN_APP_BY
from web_framework.web_driver_common.element import is_displayed_with_timeout


class ReportPublisherPage(WinAppBasePage):
    CURRENTLY_OPEN_REPORT_METHOD_CHECKBOX = (WIN_APP_BY, "20361")
    TABLE_PANE_LOCATOR = (WIN_APP_BY, "59648")
    PRINT_BUTTON_LOCATOR = (By.XPATH, "//Button[@Name='Print']")
    SAVE_CURRENT_REPORT_METHOD_METHOD_NAME_INPUT_LOCATOR = (WIN_APP_BY, "6188")
    OVERWRITE_WINDOW_LOCATOR = (By.XPATH, "//Window[@Name='Report Publisher']")
    PUBLISHER_NAME_COMBOBOX_LOCATOR = (WIN_APP_BY, "1139")
    FILE_MENU_ITEM_LOCATOR = (By.XPATH, "//MenuItem[@Name='File']")
    SAVE_REPORT_MENU_ITEM_LOCATOR = (By.XPATH, "//MenuItem[@Name='Save Report...']")
    FILE_SAVE_PAGE_LOCATORS = FileSavePageLocators(
        file_path=(By.XPATH, "//ComboBox[@AutomationId='1148']/Edit[@AutomationId='1148']"),
        file_path_dropdown=(By.XPATH, "//ComboBox[@AutomationId='1148']/Button[@AutomationId='DropDown']"),
        save_button=(By.XPATH, "//Button[@AutomationId='1' and @Name='Save']"),
        cancel_button=(By.XPATH, "//Button[@AutomationId='2' and @Name='Cancel']")
    )

    @staticmethod
    def _get_report_item_locator(report_name: str) -> Tuple[str, str]:
        return By.XPATH, f"//TreeItem[@Name='{report_name}']"

    @staticmethod
    def _get_publisher_item_locator(publisher_type: str) -> Tuple[str, str]:
        return By.XPATH, f"//ListItem[@Name='{publisher_type}']"

    def __init__(self, driver):
        super().__init__(driver)
        self._table_handle = None
        self._logger = Logger(self.__class__.__name__)
        self._file_save_page = FileSavePage(driver, self.FILE_SAVE_PAGE_LOCATORS)

    def select_open_report_method(self):
        self.click_on_element(self.CURRENTLY_OPEN_REPORT_METHOD_CHECKBOX)

    def select_report(self, report_name, report_group_name):
        self.double_click(self._get_report_item_locator(report_name))
        self.double_click(self._get_report_item_locator(report_group_name))

    def type_report_name(self, report_name):
        self.set_text(self.SAVE_CURRENT_REPORT_METHOD_METHOD_NAME_INPUT_LOCATOR, report_name)

    def click_print_button(self):
        self.click_on_element(self.PRINT_BUTTON_LOCATOR)

    def open_save_as_window(self):
        self.click_on_element(self.FILE_MENU_ITEM_LOCATOR)
        self.click_on_element(self.SAVE_REPORT_MENU_ITEM_LOCATOR)
        return self._file_save_page

    def select_print_type(self, report_type: str):
        self.wait_for_element_visibility(self.PUBLISHER_NAME_COMBOBOX_LOCATOR, 4)
        self.click_on_element(self.PUBLISHER_NAME_COMBOBOX_LOCATOR)
        self.click_on_element(self._get_publisher_item_locator(report_type))

    def set_filename(self, file_name, file_type: FileType):
        self._file_save_page.set_file_path(file_name, file_type)

    def is_overwrite_dialog_opened(self):
        return is_displayed_with_timeout(self._driver, self.OVERWRITE_WINDOW_LOCATOR, 3)

from selenium.webdriver.common.by import By

from web_framework.empower.pages.common.file_save_page import FileSavePage, FileSavePageLocators
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class MessageCenterPage(WinAppBasePage):
    SAVE_TABLE_AS_TEXT_LOCATOR = (By.NAME, "Saves table as Text")
    FILE_SAVE_PAGE_LOCATORS = FileSavePageLocators(
        file_path=(By.XPATH, "//ComboBox//Edit[@AutomationId='1148']"),
        file_path_dropdown=None,
        save_button=(By.XPATH, "//Button[@AutomationId='1' and @Name='Save']"),
        cancel_button=(By.XPATH, "//Button[@AutomationId='2' and @Name='Cancel']")
    )

    def __init__(self, driver):
        super().__init__(driver)
        self._file_save_page = FileSavePage(driver, self.FILE_SAVE_PAGE_LOCATORS)
        # self._logger = logging.getLogger(self.__class__.__name__)

    def save_log_to(self, file_path: str):
        self.click_on_element(self.SAVE_TABLE_AS_TEXT_LOCATOR)
        self._file_save_page.set_file_path(file_path)
        self._file_save_page.click_save()

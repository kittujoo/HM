from enum import Enum
from typing import Callable

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.empower.pages.common.base_table import BaseTable
from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient


class TableColumnNames(Enum):
    SAMPLE_NAME = "SampleName"
    VIAL = "Vial"
    INJECTION = "Injection"
    SAMPLE_TYPE = "Sample Type"
    DATE_ACQUIRED = "Date Acquired"
    SAMPLE_SET_NAME = "Sample Set Name"
    INJECTION_STATUS = "Injection Status"


class InjectionsTab(BaseTable):
    TABLE_ELEMENT_LOCATOR = (By.XPATH, "//Pane[@AutomationId='59648'and @ClassName='TableView']")

    def __init__(self, driver: WebDriver, miltest_rest_client_creator: Callable[[str], MiltestRestClient]):
        super().__init__(driver, miltest_rest_client_creator)

    def _get_table_element(self):
        return self.find_element(self.TABLE_ELEMENT_LOCATOR)

    def _get_miltest_handler(self):
        handler = self._get_table_element().get_attribute("NativeWindowHandle")
        return handler

    def select_preview_publisher_menu_item(self):
        self._driver.find_element_by_xpath("//*[@Name='Preview/Publisher']").click()

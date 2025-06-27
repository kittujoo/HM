from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.logger import Logger
from web_framework.empower.pages.project.injections_tab import InjectionsTab
from web_framework.empower.pages.project.tab_selector_item import TabSelectorItem, ProjectTabsHeaders
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class ProjectMainPage(WinAppBasePage):

    def _get_miltest_handler(self):
        pass

    def __init__(self, driver: WebDriver, miltest_rest_client_creator):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)
        self._miltest_rest_client_creator = miltest_rest_client_creator
        self.tab_selector: TabSelectorItem = TabSelectorItem(driver, miltest_rest_client_creator)

    def select_view_menu(self):
        ActionChains(self._driver).key_down(Keys.ALT).send_keys("V").perform()

    def open_injections(self) -> InjectionsTab:
        self.tab_selector.select_tab(ProjectTabsHeaders.INJECTIONS)
        return InjectionsTab(self._driver, self._miltest_rest_client_creator)

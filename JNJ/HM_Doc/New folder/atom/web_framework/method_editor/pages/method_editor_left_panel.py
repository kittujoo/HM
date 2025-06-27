from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.logger import Logger
from web_framework.method_editor.pages.all_settings.menu_item_all_settings import AllSettingsMenu
from web_framework.method_editor.pages.column_compartment.menu_item_column_compartment import ColumnCompartmentMenu
from web_framework.method_editor.pages.favorites.menu_item_favorites import FavoritesMenu
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage
from web_framework.method_editor.pages.pump.menu_item_pump import PumpMenu
from web_framework.method_editor.pages.sample_manager.menu_item_sample_manager import SampleManagerMenu
from web_framework.method_editor.pages.system.menu_item_system import SystemMenu
from web_framework.method_editor.pages.tuv_detector.menu_item_tuv_detector import TuvDetectorMenu


class MethodEditorLeftPanel(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    _system_menu_locator = (By.XPATH, "//Image[@Name='ics-m-img-system']")
    _all_settings_menu_locator = (By.XPATH, "//Image[@Name='ics-m-img-globe']")
    _favorite_menu_locator = (By.XPATH, "//Image[@Name='ics-m-img-heart']")
    _pump_menu_locator = (By.XPATH, "//Image[@Name='ics-img-pump']")
    _sample_manager_menu_locator = (By.XPATH, "//Image[@Name='ics-img-injection']")
    _column_compartment_menu_locator = (By.XPATH, "//Image[@Name='ics-img-column']")
    _tuv_detector_menu_locator = (By.XPATH, "//Image[@Name='ics-img-wavelength']")

    @property
    def system(self):
        self.click_on_element(self._system_menu_locator)
        return SystemMenu(self._driver)

    @property
    def all_settings(self):
        self.click_on_element(self._all_settings_menu_locator)
        return AllSettingsMenu(self._driver)

    @property
    def favorite_settings(self):
        self.click_on_element(self._favorite_menu_locator)
        return FavoritesMenu(self._driver)

    @property
    def pump(self):
        self.click_on_element(self._pump_menu_locator)
        return PumpMenu(self._driver)

    @property
    def sample_manager(self):
        self.click_on_element(self._sample_manager_menu_locator)
        sample_manager = SampleManagerMenu(self._driver)
        sample_manager.validate_opened()
        return sample_manager

    @property
    def column_compartment(self):
        self.click_on_element(self._column_compartment_menu_locator)
        return ColumnCompartmentMenu(self._driver)

    @property
    def tuv_detector(self):
        self.click_on_element(self._tuv_detector_menu_locator)
        return TuvDetectorMenu(self._driver)

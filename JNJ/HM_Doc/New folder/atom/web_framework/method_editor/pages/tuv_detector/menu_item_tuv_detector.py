from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage
from web_framework.method_editor.pages.tuv_detector.lamp_page import LampPage


class TuvDetectorMenu(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    _submenus_names = ["Lamp", "Wavelength Mode", "Data Rate", "Wavelength A", "Filter", "Autozero"]
    _submenus_names_locator = (By.XPATH, "//ListItem/Text[1]")

    _lamp_locator = (By.XPATH, "//Text[@Name='Lamp']")
    _lamp_state_locator = (By.XPATH, "//Text[@Name='Lamp']/following::Text")

    def validate_opened(self):
        def get_submenus_names():
            sub_menus = [element.get_attribute("Name") for element in self.find_elements(self._submenus_names_locator)]
            return sub_menus

        self._assert_timeout.is_true(lambda: get_submenus_names() == self._submenus_names,
                                     "Failed to validate TUV Detector menu, seems driver is on another location")

    def open_lamp(self) -> LampPage:
        self.click_on_element(self._lamp_locator)
        return LampPage(self._driver)

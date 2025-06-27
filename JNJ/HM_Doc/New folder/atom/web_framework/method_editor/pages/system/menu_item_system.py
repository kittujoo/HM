from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage
from web_framework.method_editor.pages.system.about_this_method_page import AboutThisMethodPage
from web_framework.method_editor.pages.system.column_page import ColumnPage
from web_framework.method_editor.pages.system.comment_page import CommentPage
from web_framework.method_editor.pages.system.data_channels_page import DataChannelsPage
from web_framework.method_editor.pages.system.mobile_phase_page import MobilePhasePage


class SystemMenu(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    DATA_CHANNELS_LOCATOR = (By.XPATH, "//Text[@Name='Data Channels']")

    COLUMN_LOCATOR = (By.XPATH, "//Text[@Name='Column']")
    COLUMN_STATE_LOCATOR = (By.XPATH, "//Text[@Name='Column']/following::Text")

    MOBILE_PHASE_LOCATOR = (By.XPATH, "//Text[@Name='Mobile Phase']")
    MOBILE_PHASE_STATE_LOCATOR = (By.XPATH, "//Text[@Name='Mobile Phase']/following::Text")

    COMMENT_LOCATOR = (By.XPATH, "//Text[@Name='Comment']")
    COMMENT_STATE_LOCATOR = (By.XPATH, "//Text[@Name='Comment']/following::Text")

    ABOUT_THIS_METHOD_LOCATOR = (By.XPATH, "//Text[@Name='About this Method']")
    ABOUT_THIS_METHOD_STATE_LOCATOR = (By.XPATH, "//Text[@Name='About this Method']/following::Text")

    def open_data_channels(self) -> DataChannelsPage:
        self.click_on_element(self.DATA_CHANNELS_LOCATOR)
        return DataChannelsPage(self._driver)

    def open_column(self):
        self.click_on_element(self.COLUMN_LOCATOR)
        return ColumnPage(self._driver)

    def get_column_state(self):
        state = self.get_element_name_attribute(self.COLUMN_STATE_LOCATOR)
        return state

    def open_mobile_phase(self):
        self.click_on_element(self.MOBILE_PHASE_LOCATOR)
        return MobilePhasePage(self._driver)

    def get_mobile_phase_state(self):
        state = self.get_element_name_attribute(self.MOBILE_PHASE_STATE_LOCATOR)
        return state

    def open_comment(self):
        self.click_on_element(self.COMMENT_LOCATOR)
        return CommentPage(self._driver)

    def get_comment_state(self):
        state = self.get_element_name_attribute(self.COMMENT_STATE_LOCATOR)
        return state

    def open_about_this_method(self):
        self.click_on_element(self.ABOUT_THIS_METHOD_LOCATOR)
        return AboutThisMethodPage(self._driver)

    def get_about_this_method_state(self):
        state = self.get_element_name_attribute(self.ABOUT_THIS_METHOD_STATE_LOCATOR)
        return state

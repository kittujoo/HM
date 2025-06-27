from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class PumpMenu(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

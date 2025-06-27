import time
from logging import Logger
from pathlib import Path
from pytest_bdd import scenarios, given, when, then

from utilities.assert_timeout import AssertTimeout
from web_framework.kiosk.pages.Locators.System.system_about_screen_locators import AboutScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.System.About.about_screen import AboutScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/kiosk_about_screen.feature')

logger = Logger("test_about_screen")

@given('User navigates to the About screen')
def navigate_system_logs_screen(session_system_settings_screen_page: SystemSettingsScreen):
    session_system_settings_screen_page.tap(SystemSettingsScreenLocators.ABOUT_TAB)

@then('Software icon is selected')
def validate_software_icon_enabled(about_screen: AboutScreen):
    about_screen.validate_about_screen()
    assert about_screen.is_button_selected(AboutScreenLocators.SOFTWARE_BUTTON)
    assert about_screen.is_displayed(AboutScreenLocators.BUILD_VERSION)

@when('User selects hardware icon')
def select_hardware_icon(about_screen: AboutScreen, assert_timeout: AssertTimeout):
    about_screen.validate_about_screen()
    about_screen.tap(AboutScreenLocators.HARDWARE_BUTTON)
    assert_timeout.is_true(lambda: about_screen.is_button_selected(AboutScreenLocators.HARDWARE_BUTTON),
                             message="The Hardware button was not selected within the specified timeout", timeout_in_seconds=5)

@when('User selects support icon')
def select_support_icon(about_screen: AboutScreen, assert_timeout: AssertTimeout):
    about_screen.validate_about_screen()
    about_screen.tap(AboutScreenLocators.SUPPORT_BUTTON)
    assert_timeout.is_true(lambda: about_screen.is_button_selected(AboutScreenLocators.SUPPORT_BUTTON),
                           message="The Support button was not selected within the specified timeout", timeout_in_seconds=5)

@then('User validates the Software version is correctly displayed')
def validate_software_screen(about_screen: AboutScreen):
    about_screen.validate_about_screen()
    assert not about_screen.contains_text(AboutScreenLocators.BUILD_VERSION, "---")

@then('User validates the Product model, product variant and serial number are correctly displayed')
def validate_hardware_screen(about_screen: AboutScreen):
    about_screen.validate_about_screen()
    assert not about_screen.contains_text(AboutScreenLocators.PRODUCT_MODEL, "---")
    assert about_screen.contains_text(AboutScreenLocators.PRODUCT_VARIANT, "TUV")
    assert not about_screen.contains_text(AboutScreenLocators.SERIAL_NUMBER, "---")

@then('User validates the manufacturer, support website and QR code are correctly displayed')
def validate_support_screen(about_screen: AboutScreen):
    about_screen.validate_about_screen()
    about_screen.verify_qrcode_link(AboutScreenLocators.QR_CODE, "https://help.waters.com/help/e")
    assert about_screen.contains_text(AboutScreenLocators.MANUFACTURER,"Waters Corporation")
    assert about_screen.contains_text(AboutScreenLocators.SUPPORT_WEBSITE, "help.waters.com")
    assert about_screen.contains_text(AboutScreenLocators.QR_LABEL_TITLE, "Waters")
    assert about_screen.contains_text(AboutScreenLocators.QR_LABEL_SUBTITLE, "help.waters.com")

import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.solvent_bottles import SolventLineColorsConstants
from web_framework.kiosk.pages.Locators.Home.SolventManager.mobile_phase_configuration_settings_locators import (
    MobilePhaseConfigurationSettingsScreenLocators as MobileLocators, ReplaceSolventLocators,
    SolventDetailsLocators)
from web_framework.kiosk.pages.Locators.Home.SolventManager.solvent_configuration_locators import SolventConfigurationsScreenLocators
from web_framework.kiosk.pages.Locators.System.SolventBottlesManager.mobile_phase_configuration_settings_screen_locators import \
    MobilePhaseConfigurationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class MobilePhaseSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait = 10

    def validate_mobile_phase_selection_screen(self):
        locator = MobileLocators.REPLACE_SOLVENT_PANEL
        screen_name = "Mobile Phase options screen "
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_mobile_phase_details_screen(self):
        locator = MobileLocators.SOLVENT_NAME
        screen_name = "Mobile Phase configuration details screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_mobile_phase_settings_screen(self):
        locator = MobileLocators.MOBILE_PHASE_A_TAB
        screen_name = "Mobile Phase configuration settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_replacement_screen(self):
        locator = ReplaceSolventLocators.SOLVENT_LEVEL_PANEL
        screen_name = "Replace solvent screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_mobile_phase_tab(self, mobile_phase):
        mobile_phase_text_dictionary = {
            "A": MobileLocators.MOBILE_PHASE_A_TAB,
            "B": MobileLocators.MOBILE_PHASE_B_TAB,
            "C": MobileLocators.MOBILE_PHASE_C_TAB,
            "D": MobileLocators.MOBILE_PHASE_D_TAB,
            "Needle": MobileLocators.MOBILE_PHASE_NEEDLE_TAB,
            "Seal": MobileLocators.MOBILE_PHASE_SEAL_TAB}

        locator = mobile_phase_text_dictionary[mobile_phase]
        self.tap(locator)

    def select_bottle_volume(self, mobile_phase, bottle_volume):
        bottle_volume_text_dictionary = {
            "2L": MobileLocators.SOLVENT_BOTTLE_2L_OPTION,
            "4L": MobileLocators.SOLVENT_BOTTLE_4L_OPTION,
            "5L": MobileLocators.SOLVENT_BOTTLE_5L_OPTION}
        mobile_phase_volume_dictionary = {
            "A": MobileLocators.SOLVENT_BADGE_A,
            "B": MobileLocators.SOLVENT_BADGE_B,
            "C": MobileLocators.SOLVENT_BADGE_C,
            "D": MobileLocators.SOLVENT_BADGE_D,
            "Seal": MobileLocators.SOLVENT_BADGE_SEAL,
            "Needle": MobileLocators.SOLVENT_BADGE_NEEDLE}

        self.tap(mobile_phase_volume_dictionary[mobile_phase])
        bottle_volume_locator = bottle_volume_text_dictionary[bottle_volume]
        self.scroll_to_view(bottle_volume_locator)
        self.tap(bottle_volume_locator)

    def select_line_color(self, mobile_phase, line_color):
        line_color_text_dictionary = {
            "blue": MobileLocators.LINE_COLOR_BLUE,
            "red": MobileLocators.LINE_COLOR_RED,
            "pink": MobileLocators.LINE_COLOR_PINK,
            "green": MobileLocators.LINK_COLOR_GREEN}
        mobile_phase_color_dictionary = {
            "A": MobileLocators.LINE_COLOR_INFO_LABEL_A,
            "B": MobileLocators.LINE_COLOR_INFO_LABEL_B,
            "C": MobileLocators.LINE_COLOR_INFO_LABEL_C,
            "D": MobileLocators.LINE_COLOR_INFO_LABEL_D,
            "Seal": SolventConfigurationsScreenLocators.SEAL_WASH_COLOR,
            "Needle": SolventConfigurationsScreenLocators.NEEDLE_WASH_COLOR}

        self.tap(mobile_phase_color_dictionary[mobile_phase])

        line_color_locator = line_color_text_dictionary[line_color]
        self.scroll_to_view(line_color_locator)
        self.logger.info(f"Solvent bottle {mobile_phase} was set as {line_color}")

    def validate_mobile_phase_installation(self, mobile_phase, installation_status):
        mobile_phase_badge_text_dictionary = {
            "A": MobileLocators.SOLVENT_BADGE_A,
            "B": MobileLocators.SOLVENT_BADGE_B,
            "C": MobileLocators.SOLVENT_BADGE_C,
            "D": MobileLocators.SOLVENT_BADGE_D,
            "Seal": MobileLocators.SOLVENT_BADGE_SEAL,
            "Needle": MobileLocators.SOLVENT_BADGE_NEEDLE}

        if mobile_phase in mobile_phase_badge_text_dictionary:
            uninstalled_color = "background-color: var(--option-10--v03);"
            badge_color_label_locator = self.get_element(mobile_phase_badge_text_dictionary[mobile_phase])
            label_style = badge_color_label_locator.get_attribute('style')
            label_style_color = label_style.find(uninstalled_color)

            if installation_status == "uninstalled":
                assert label_style_color == 0
                return
            if installation_status == "installed":
                assert label_style_color == -1
                return

        assert False, f"Unexpected mobile phase letter or installation status => {mobile_phase}, {installation_status}"

    def validate_mobile_phase_configured(self, mobile_phase, installation_status):
        mobile_phase_badge_text_dictionary = {
            "A": MobileLocators.SOLVENT_A_NOT_CONFIGURED,
            "B": MobileLocators.SOLVENT_B_NOT_CONFIGURED,
            "C": MobileLocators.SOLVENT_C_NOT_CONFIGURED,
            "D": MobileLocators.SOLVENT_D_NOT_CONFIGURED,
            "Needle": MobileLocators.NEEDLE_NOT_CONFIGURED,
            "Seal": MobileLocators.SEAL_NOT_CONFIGURED}

        if installation_status == "not displayed":
            assert "Not Configured" == self.get_text(
                mobile_phase_badge_text_dictionary[mobile_phase]), f"The mobile phase {mobile_phase} was expected to be {installation_status}"
        else:
            assert not "Not Configured" == self.get_text(
                mobile_phase_badge_text_dictionary[mobile_phase]), f"The mobile phase {mobile_phase} was expected to be {installation_status}"

    def validate_saved_mobile_phase_settings(self, mobile_phase, bottle_volume, line_color):
        mobile_phase_text_dictionary = {
            "A": MobilePhaseConfigurationScreenLocators.SOLVENT_A_LINE_COLOR_ICON,
            "B": MobilePhaseConfigurationScreenLocators.SOLVENT_B_LINE_COLOR_ICON,
            "C": MobilePhaseConfigurationScreenLocators.SOLVENT_C_LINE_COLOR_ICON,
            "D": MobilePhaseConfigurationScreenLocators.SOLVENT_D_LINE_COLOR_ICON,
            "Needle": SolventConfigurationsScreenLocators.NEEDLE_WASH_LINE_COLOR,
            "Seal": SolventConfigurationsScreenLocators.SEAL_WASH_LINE_COLOR}

        self.tap(MobileLocators.SOLVENT_LINE_COLOR)
        actual_volume = self.get_text(MobileLocators.BOTTLE_VOLUME_INFO_LABEL)
        assert actual_volume == bottle_volume, \
            f"The bottle volume setting was not saved properly.Expected:[{bottle_volume}] Actual:[{actual_volume}]"
        actual_color = Color.from_string(self.find_element(mobile_phase_text_dictionary[mobile_phase]).value_of_css_property('background-color'))
        assert actual_color == getattr(SolventLineColorsConstants, line_color), \
            f"The actual line color selected is not the same in A. Expected:[{getattr(SolventLineColorsConstants, line_color)}] Actual:[{actual_color}]"

    def validate_unsaved_mobile_phase_settings(self, mobile_phase, default_bottle_volume, default_line_color):
        mobile_phase_text_dictionary = {
            "A": MobilePhaseConfigurationScreenLocators.SOLVENT_A_LINE_COLOR_ICON,
            "B": MobilePhaseConfigurationScreenLocators.SOLVENT_B_LINE_COLOR_ICON,
            "C": MobilePhaseConfigurationScreenLocators.SOLVENT_C_LINE_COLOR_ICON,
            "D": MobilePhaseConfigurationScreenLocators.SOLVENT_D_LINE_COLOR_ICON,
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_LINE_COLOR,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_LINE_COLOR}

        self.tap(MobileLocators.SOLVENT_LINE_COLOR)
        actual_bottle = self.get_text(MobileLocators.BOTTLE_VOLUME_INFO_LABEL)
        assert actual_bottle == default_bottle_volume, \
            f"The bottle volume setting was saved when it should not have been." \
            f"Expected:[{default_bottle_volume}] Actual:[{actual_bottle}]"
        actual_color = Color.from_string(self.find_element(mobile_phase_text_dictionary[mobile_phase]).value_of_css_property('background-color'))
        assert actual_color == getattr(SolventLineColorsConstants, default_line_color), \
            f"The actual line color selected is not the same in A." \
            f"Expected:[{getattr(SolventLineColorsConstants, default_line_color)}] Actual:[{actual_color}]"

    # Replace solvent functions

    def get_solvent_level_height(self, desired_selection) -> str:
        solvent_level_dictionary = {
            "Empty": "0px",
            "1/8 Full": "33px",
            "1/4 Full": "66px",
            "3/8 Full": "99px",
            "1/2 Full": "132px",
            "5/8 Full": "165px",
            "3/4 Full": "198px",
            "7/8 Full": "231px",
            "Full": "264px"}

        solvent_level_height = solvent_level_dictionary[desired_selection]
        return solvent_level_height

    def set_solvent_level(self, desired_selection):
        locator = ReplaceSolventLocators.SOLVENT_LEVEL_SLIDER
        self.logger.info(locator)
        solvent_level_height = self.get_solvent_level_height(desired_selection)
        self.logger.info(f"Before setting: {self.find_element(locator).value_of_css_property('height')}")
        self._driver.execute_script("var element = document.evaluate(\"" + locator[
            1] + "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)"
                 ".singleNodeValue; element.setAttribute('style', 'height:" + solvent_level_height + "');")
        self.logger.info(f"After setting: {self.find_element(locator).value_of_css_property('height')}")

    def validate_solvent_level(self, solvent_level):
        self.wait_for_load(self.wait_time)
        current_solvent_level = self.get_text(ReplaceSolventLocators.SOLVENT_LEVEL_INFO_LABEL)
        assert solvent_level == current_solvent_level, f"The solvent level does not match. Expected: {solvent_level} | Current: {current_solvent_level}"

    def validate_solvent_expiry(self, locator, solvent_expire_month, solvent_expire_day, solvent_expire_year):
        full_date = self.get_text(locator)
        full_date_groups = re.search(r"(\d{1,2})\s(\w+)\s(\d{4})", full_date)
        expire_month = full_date_groups.group(2)
        expire_day = full_date_groups.group(1)
        expire_year = full_date_groups.group(3)
        if int(solvent_expire_day) < 10:
            solvent_expire_day = '0' + solvent_expire_day

        assert expire_month == solvent_expire_month, f"Expiry month not as expected. Expected:[{solvent_expire_month}] Actual:[{expire_month}]"
        assert expire_day == solvent_expire_day, f"Expiry day not as expected. Expected:[{solvent_expire_day}] Actual:[{expire_day}]"
        assert expire_year == solvent_expire_year, f"Expiry year not as expected. Expected:[{solvent_expire_year}] Actual:[{expire_year}]"

    def validate_details_solvent_level(self, solvent_level, bottle_size):
        self.wait_time_to_load_value(SolventDetailsLocators.SOLVENT_LEVEL_INFO_LABEL)
        current_solvent_level = self.get_text(SolventDetailsLocators.SOLVENT_LEVEL_INFO_LABEL)
        if '/' in solvent_level:
            solvent_level_height = eval(f"{bottle_size.strip('L')}*{solvent_level.strip(' Full')}")
            if solvent_level_height.is_integer():
                solvent_level_height = int(solvent_level_height)
            solvent_level_height = str(solvent_level_height) + ' Liters'
        elif solvent_level == "Empty":
            solvent_level_height = '0 Liters'
        else:
            solvent_level_height = bottle_size.strip('L') + ' Liters'
        assert solvent_level_height == current_solvent_level, f"The volume is not as expected, " \
                                                              f"Expected:[{solvent_level_height}] Actual:[{current_solvent_level}]"

    def set_toggle_status(self, wash_solvent, toggle_status):
        toggle_dict = {
            "A": MobileLocators.BOTTLE_TOGGLE_A,
            "B": MobileLocators.BOTTLE_TOGGLE_B,
            "C": MobileLocators.BOTTLE_TOGGLE_C,
            "D": MobileLocators.BOTTLE_TOGGLE_D,
            "Seal": MobileLocators.SEAL_WASH_TOGGLE,
            "Needle": MobileLocators.NEEDLE_WASH_TOGGLE}
        self.wait_for_element_visibility(self.wait_time, toggle_dict[wash_solvent])
        self.set_toggle_button(toggle_dict[wash_solvent], toggle_status)
        self.logger.info(f"Successfully Set The {wash_solvent} Toggle Value As {toggle_status}")

    def is_data_present(self, analyst_name) -> bool:
        return self.is_displayed((By.XPATH, f"//div[text()='{analyst_name}']"))

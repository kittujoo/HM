import re
import time

from selenium.webdriver.support.color import Color

from utilities.logger import Logger
from utilities.string_utility import get_string_in_range
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import DeltaPressureConditionCardConstants
from web_framework.kiosk.pages.Locators.Home.SolventManager.delta_pressure_condition_card import DeltaPressureSettingsScreenLocators
from web_framework.kiosk.pages.Locators.Home.SolventManager.sm_home_screen import SolventManagerHomeScreenLocators as sml
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class SolventManagerHomeScreen(BasePage):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.current_system_pressure = None

    def validate_solvent_manager_home_screen(self):
        locator = sml.FLOW_CONDITIONAL_CARD
        screen_name = "solvent manager home screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_manager_home_screen_page_two(self):
        locator = sml.MOBILE_PHASE_A_CONDITION_CARD
        screen_name = "solvent manager home screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_manager_home_screen_page_three(self):
        locator = sml.FLOW_PATH_CONDITIONAL_CARD
        screen_name = "solvent manager home screen page three"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_third_page(self):
        self.tap(sml.HOME_PAGE_THREE)

    def tap_flow_condition_card(self):
        self.tap(sml.FLOW_CONDITIONAL_CARD)

    def tap_solvent_composition_condition_card(self):
        self.tap(sml.SOLVENT_COMPOSITION_CONDITION_CARD)

    def is_home_icon_selected(self):
        self.is_selected(DashBoardsScreenPageLocators.HOME)

    def get_current_flow_read_back_message(self):
        return self.get_current_flow_rate(sml.FLOW_RATE)

    def tap_system_pressure_condition_card(self):
        self.tap(sml.SYSTEM_PRESSURE_CARD)

    def get_system_pressure_conditional_card(self):
        return self.get_system_pressure(
            sml.SYSTEM_PRESSURE_CARD_NUMBER_VALUE,
            sml.SYSTEM_PRESSURE_CARD_DECIMAL_VALUE)

    def get_system_pressure_unit(self):
        return self.get_text(sml.SYSTEM_PRESSURE_CARD_UNIT)

    def tap_flow_path_conditional_card(self):
        self.tap(sml.FLOW_PATH_CONDITIONAL_CARD)

    def get_flow_units(self):
        return self.get_container_text(sml.FLOW_RATE_UNITS)

    def get_flow_path_conditional_card(self):
        self.wait_for_element_visibility(5, sml.DISPLAYED_FLOW_PATH)
        return self.get_text(sml.DISPLAYED_FLOW_PATH)

    def get_solvent_a_composition(self):
        return self.get_condition_card_value(sml.SOLVENT_A_COMPOSITION_BEFORE_DECIMAL_VALUE,
                                             sml.SOLVENT_A_COMPOSITION_AFTER_DECIMAL_VALUE)

    def get_solvent_b_composition(self):
        return self.get_condition_card_value(sml.SOLVENT_B_COMPOSITION_BEFORE_DECIMAL_VALUE,
                                             sml.SOLVENT_B_COMPOSITION_AFTER_DECIMAL_VALUE)

    def get_solvent_c_composition(self):
        return self.get_condition_card_value(sml.SOLVENT_C_COMPOSITION_BEFORE_DECIMAL_VALUE,
                                             sml.SOLVENT_C_COMPOSITION_AFTER_DECIMAL_VALUE)

    def get_solvent_d_composition(self):
        return self.get_condition_card_value(sml.SOLVENT_D_COMPOSITION_BEFORE_DECIMAL_VALUE,
                                             sml.SOLVENT_D_COMPOSITION_AFTER_DECIMAL_VALUE)

    def get_solvent_line_id(self, locator):
        solvent_id_string = self.get_container_text(locator)
        solvent_id = solvent_id_string[1:]
        return solvent_id

    def get_min_delta_pressure(self):
        min_pressure = re.search(r'Min:\s(\d*.?\d*)', self.get_text(sml.DELTA_PRESSURE_RANGE_LABEL))
        return min_pressure[1]

    def get_max_delta_pressure(self):
        max_pressure = re.search(r'Max:\s(\d*.?\d*)', self.get_text(sml.DELTA_PRESSURE_RANGE_LABEL))
        return max_pressure[1]

    def get_current_delta_pressure(self):
        current_delta_pressure = self.get_temperature(
            DeltaPressureSettingsScreenLocators.BEFORE_DECIMAL_DELTA_PRESSURE_READ_BACK_MESSAGE,
            DeltaPressureSettingsScreenLocators.AFTER_DECIMAL_DELTA_PRESSURE_READ_BACK_MESSAGE)
        return current_delta_pressure

    def get_indicator_message(self):
        indicator_status = self.get_element(DeltaPressureSettingsScreenLocators.INDICATOR_BAR_STATUS)
        current_indicator_status = indicator_status.get_attribute("ng-reflect-ng-class")
        return current_indicator_status

    def get_minimum_value(self):
        pressure_read_back_text = self.get_text(DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_READ_BACK_MESSAGE)
        self.logger.info(f"pressure_read_back_text==>>> {pressure_read_back_text}")
        current_minimum_value = get_string_in_range(pressure_read_back_text, 5, 11)
        self.logger.info(f"current_minimum_value==>>> {current_minimum_value}")
        current_minimum_value = TypeConverter.to_float(current_minimum_value)
        return current_minimum_value

    def get_maximum_value(self):
        pressure_read_back_text = self.get_text(DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_READ_BACK_MESSAGE)
        self.logger.info(f"pressure_read_back_text==>>> {pressure_read_back_text}")
        current_maximum_value = get_string_in_range(pressure_read_back_text, 18, 25)
        current_maximum_value = TypeConverter.to_float(current_maximum_value)
        return current_maximum_value

    def get_pressure_units(self):
        pressure_read_back_text = self.get_text(DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_READ_BACK_MESSAGE)
        self.logger.info(f"pressure_read_back_text==>>> {pressure_read_back_text}")
        pressure_units = get_string_in_range(pressure_read_back_text, 25, 28)
        self.logger.info(f"pressure_units==>>> {pressure_units}")
        pressure_units = TypeConverter.to_str(pressure_units)
        return pressure_units

    def validate_pressure_read_back_units(self):
        actual_pressure_readback_units = self.get_pressure_units()
        self.logger.info(f"actual_pressure_units====>>>>{actual_pressure_readback_units}")
        expected_pressure_readback__units = DeltaPressureConditionCardConstants.PressureUnits
        assert actual_pressure_readback_units == expected_pressure_readback__units, \
            f"The pressure is not same.  Expected:[{expected_pressure_readback__units}] Actual:[{actual_pressure_readback_units}]"

    def get_expected_delta_pressure(self):
        current_minimum_value = self.get_minimum_value()
        current_maximum_value = self.get_maximum_value()
        expected_delta_pressure_value = current_maximum_value - current_minimum_value
        return expected_delta_pressure_value

    def validate_delta_pressure_value(self):
        expected_delta_pressure_value = self.get_expected_delta_pressure()
        current_delta_pressure_value = self.get_current_delta_pressure()
        current_delta_pressure_value = TypeConverter.to_float(current_delta_pressure_value)
        self.logger.info(f"expected_delta_pressure_value====>>>>{expected_delta_pressure_value}")
        self.logger.info(f"current_delta_pressure_value====>>>>{current_delta_pressure_value}")
        assert expected_delta_pressure_value == current_delta_pressure_value, \
            f"The pressure is not same.  Expected:[{expected_delta_pressure_value}] Actual:[{current_delta_pressure_value}]"

    def validate_pressure_units_per_min(self):
        actual_delta_pressure_units = self.get_text(DeltaPressureSettingsScreenLocators.PRESSURE_UNITS)
        self.logger.info(f"actual_delta_pressure_units====>>>>{actual_delta_pressure_units}")
        expected_delta_pressure_units = DeltaPressureConditionCardConstants.DeltaPressurePerMinUnit
        self.logger.info(f"expected_delta_pressure_units====>>>>{expected_delta_pressure_units}")
        assert actual_delta_pressure_units == expected_delta_pressure_units, \
            f"The pressure is not same.  Expected:[{expected_delta_pressure_units}] Actual:[{actual_delta_pressure_units}]"

    def tap_solvent_manager_schematic_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.SOLVENT_ICON)

    def is_toggle_button_enabled(self, locator):
        toggle_button = self.get_element(locator)
        is_toggle_button_state = toggle_button.get_attribute("class")
        get_check_box_state = is_toggle_button_state.find("mat-checked")

        if get_check_box_state != -1:
            return True
        return False

    def tap_mobile_phase_condition_card(self, mobile_phase):
        mobile_phase_text_dictionary = {
            "A": sml.MOBILE_PHASE_A_CONDITION_CARD,
            "B": sml.MOBILE_PHASE_B_CONDITION_CARD,
            "C": sml.MOBILE_PHASE_C_CONDITION_CARD,
            "D": sml.MOBILE_PHASE_D_CONDITION_CARD,
            "Needle": sml.MOBILE_PHASE_NEEDLE_CONDITION_CARD,
            "Seal": sml.MOBILE_PHASE_SEAL_CONDITION_CARD}

        if mobile_phase in mobile_phase_text_dictionary:
            if mobile_phase == "Needle" or mobile_phase == "Seal":
                self.tap(sml.HOME_PAGE_TWO)
                locator = mobile_phase_text_dictionary[mobile_phase]
                self.tap(locator)
                return
            else:
                locator = mobile_phase_text_dictionary[mobile_phase]
                self.tap(locator)
                return

        assert False, f"Unexpected mobile phase letter => {mobile_phase}"

    def validate_condition_card_mobile_phase_settings(self, mobile_phase, bottle_volume, line_color):
        bottle_volume_text_dictionary = {
            "A": sml.MOBILE_PHASE_A_SECONDARY_LEVEL,
            "B": sml.MOBILE_PHASE_B_SECONDARY_LEVEL,
            "C": sml.MOBILE_PHASE_C_SECONDARY_LEVEL,
            "D": sml.MOBILE_PHASE_D_SECONDARY_LEVEL,
            "Needle": sml.MOBILE_PHASE_NEEDLE_SECONDARY_LEVEL,
            "Seal": sml.MOBILE_PHASE_SEAL_SECONDARY_LEVEL
        }

        card_color_text_dictionary = {
            "A": sml.MOBILE_PHASE_A_CARD_COLOR,
            "B": sml.MOBILE_PHASE_B_CARD_COLOR,
            "C": sml.MOBILE_PHASE_C_CARD_COLOR,
            "D": sml.MOBILE_PHASE_D_CARD_COLOR,
            "Needle": sml.MOBILE_PHASE_NEEDLE_CARD_COLOR,
            "Seal": sml.MOBILE_PHASE_SEAL_CARD_COLOR
        }

        line_color_text_dictionary = {
            "blue": "background: var(--option-04--v01);",
            "red": "background: var(--option-01--v01);",
            "green": "background: var(--option-06--v01);",
            "pink": "background: var(--option-03--v01);"}

        if mobile_phase in bottle_volume_text_dictionary:
            bottle_volume_text = self.get_text(bottle_volume_text_dictionary[mobile_phase])
            bottle_volume_group = re.search(r"\/\s(\d+)", bottle_volume_text)
            current_bottle_volume = bottle_volume_group.group(1) + "L"
            assert current_bottle_volume == bottle_volume, f"Bottle volumes don't match. Current: {current_bottle_volume} | Expected: {bottle_volume}"

        if mobile_phase in card_color_text_dictionary:
            card_color_locator = self.get_element(card_color_text_dictionary[mobile_phase])
            card_style = card_color_locator.get_attribute('style')

            if line_color in line_color_text_dictionary:
                card_color = card_style.find(line_color_text_dictionary[line_color])
            if card_color == -1:
                assert False
            else:
                assert True
            return

        assert False, f"Unrecognized mobile phase: {mobile_phase} | or unrecognized bottle volume: {bottle_volume}"

    def validate_unsaved_condition_card_mobile_phase_settings(self, mobile_phase, default_bottle_volume, default_line_color):
        bottle_volume_text_dictionary = {
            "A": sml.MOBILE_PHASE_A_SECONDARY_LEVEL,
            "B": sml.MOBILE_PHASE_B_SECONDARY_LEVEL,
            "C": sml.MOBILE_PHASE_C_SECONDARY_LEVEL,
            "D": sml.MOBILE_PHASE_D_SECONDARY_LEVEL,
            "Needle": sml.MOBILE_PHASE_NEEDLE_SECONDARY_LEVEL,
            "Seal": sml.MOBILE_PHASE_SEAL_SECONDARY_LEVEL
        }

        card_color_text_dictionary = {
            "A": sml.MOBILE_PHASE_A_CARD_COLOR,
            "B": sml.MOBILE_PHASE_B_CARD_COLOR,
            "C": sml.MOBILE_PHASE_C_CARD_COLOR,
            "D": sml.MOBILE_PHASE_D_CARD_COLOR,
            "Needle": sml.MOBILE_PHASE_NEEDLE_CARD_COLOR,
            "Seal": sml.MOBILE_PHASE_SEAL_CARD_COLOR
        }

        default_color_text_dictionary = {
            "pink": "background: var(--option-03--v01);",
            "yellow": "background: var(--option-08--v03);"}

        if mobile_phase in bottle_volume_text_dictionary:
            bottle_volume_text = self.get_text(bottle_volume_text_dictionary[mobile_phase])
            bottle_volume_group = re.search(r"\/\s(\d+)", bottle_volume_text)
            current_bottle_volume = bottle_volume_group.group(1) + "L"
            assert current_bottle_volume == default_bottle_volume, f"The bottle volume setting was saved when it should not have been"

        if mobile_phase in card_color_text_dictionary:
            card_color_locator = self.get_element(card_color_text_dictionary[mobile_phase])
            card_style = card_color_locator.get_attribute('style')

            if default_line_color in default_color_text_dictionary:
                card_color_locator = card_style.find(default_color_text_dictionary[default_line_color])
            if card_color_locator == -1:
                assert False, f"{card_style}"
            else:
                assert True
            return

        assert False, f"Unexpected mobile phase letter, bottle volume, or line color => {mobile_phase}, {default_bottle_volume}, {default_line_color}"

    def get_volume(self, locator):
        time.sleep(1)
        threshold_volume_element = self.get_element(locator)
        threshold_volume_value = threshold_volume_element.get_attribute("ng-reflect-value")
        threshold_volume = TypeConverter.to_float(threshold_volume_value)
        return threshold_volume

    def set_current_system_pressure(self, current_system_pressure):
        self.logger.info(f'current_system_pressure==={current_system_pressure} ')
        self.current_system_pressure = current_system_pressure

    def get_current_system_pressure(self):
        return self.current_system_pressure

    def get_line_color(self, wash_solvent):
        mobile_phase_text_dictionary = {
            "A": sml.SOLVENT_A_COLOR,
            "B": sml.SOLVENT_B_COLOR,
            "C": sml.SOLVENT_C_COLOR,
            "D": sml.SOLVENT_D_COLOR,
            "Seal": sml.SEAL_COLOR,
            "Needle": sml.NEEDLE_COLOR}
        actual_color = Color.from_string(self.find_element(mobile_phase_text_dictionary[wash_solvent]).value_of_css_property('background-color'))
        return actual_color

import time
from urllib import parse

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import TUVConditionCardConstants
from web_framework.kiosk.common.Constants.dashboard_constants import SystemStateConstants
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class DashBoardScreen(BasePage):
    dashboard_icons = {
        "system": DashBoardsScreenPageLocators.INSTRUMENT,
        "maintain": DashBoardsScreenPageLocators.MAINTAIN,
        "health": DashBoardsScreenPageLocators.HEALTH,
        "plots": DashBoardsScreenPageLocators.PLOTS,
        "commands": DashBoardsScreenPageLocators.COMMANDS,
        "setup": DashBoardsScreenPageLocators.SETUP,
        "notification": DashBoardsScreenPageLocators.NOTIFICATION,
        "user_settings": DashBoardsScreenPageLocators.USER_SETTINGS,
        "home": DashBoardsScreenPageLocators.HOME
    }

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.URL = parse.urljoin(base_url, "dashboard/home")
        self.logger = Logger(self.__class__.__name__)
        self.current_system_pressure = None

    def tap_commands(self):
        self.tap(DashBoardsScreenPageLocators.COMMANDS)

    def tap_home(self):
        self.tap(DashBoardsScreenPageLocators.HOME)

    def tap_system(self):
        self.tap(DashBoardsScreenPageLocators.INSTRUMENT)

    def tap_setup(self):
        self.tap(DashBoardsScreenPageLocators.SETUP)

    def tap_maintain(self):
        self.tap(DashBoardsScreenPageLocators.MAINTAIN)

    def tap_diagnose(self):
        self.tap(DashBoardsScreenPageLocators.HEALTH)

    def is_home_icon_displayed(self):
        return self.is_displayed(DashBoardsScreenPageLocators.HOME)

    def tap_column_manager_read_back_card(self):
        self.tap(TopLevelDashBoardScreenLocators.COLUMN_MANAGER_READ_BACK_CARD)

    def tap_column_manager_schematic_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.COLUMN_ICON)

    def tap_solvent_manager_schematic_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.SOLVENT_ICON)

    def tap_sample_manager_schematic_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.SAMPLE_ICON)

    def tap_tuv_schematic_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.TUV_ICON)

    def tap_solvent_bottle_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.BOTTLE_ICON)

    def tap_tuv_read_back_card(self):
        self.tap(TopLevelDashBoardScreenLocators.TUV_DETECTOR_READ_BACK_CARD)

    def tap_solvent_manager_read_back_card(self):
        self.tap(TopLevelDashBoardScreenLocators.SOLVENT_MANAGER_READ_BACK_CARD)

    def tap_sample_manager_read_back_card(self):
        self.tap(TopLevelDashBoardScreenLocators.SAMPLE_MANAGER_READ_BACK_CARD)

    def select_icon(self, icon: str):
        if icon in DashBoardScreen.dashboard_icons:
            locator = DashBoardScreen.dashboard_icons[icon]
            self.tap(locator)
            return
        assert False, f"Invalid icon => {icon}"

    def validate_inactive_icon(self, icon: str):

        self.validate_dashboard_screen()
        assert icon in DashBoardScreen.dashboard_icons, f"Invalid icon => {icon}"

        icon_element = self.get_element(DashBoardScreen.dashboard_icons[icon])
        assert icon_element is not None, f"Unable to locate the given {icon} icon."

        active_icon_class_value = None
        icon_class_string = None
        start_time = time.time()
        while time.time() - start_time < 5:

            icon_class_string = icon_element.get_attribute("class")
            self.logger.info(f"attribute of class =====>{icon_class_string}")
            active_icon_class_value = "selected"

            if active_icon_class_value not in icon_class_string:
                break
            time.sleep(1)
        assert active_icon_class_value not in icon_class_string, f"The given {icon} icon is  highlighted"
        return

    def validate_active_icon(self, icon):
        assert icon in DashBoardScreen.dashboard_icons, f"Invalid icon => {icon}"

        icon_element = self.get_element(DashBoardScreen.dashboard_icons[icon])
        assert icon_element is not None, f"Unable to locate the given {icon} icon."

        start_time = time.time()
        active_icon_class_value = None
        icon_class_string = None
        while time.time() - start_time < 5:
            icon_class_string = icon_element.get_attribute("class")
            active_icon_class_value = "selected"

            if active_icon_class_value in icon_class_string:
                break
            time.sleep(1)

        assert active_icon_class_value in icon_class_string, f"The given {icon} icon is not  highlighted"
        return

    def validate_white_background(self, current_background_color):
        assert current_background_color == "fff" or current_background_color == "rgba(0, 0, 0, 0)", f"Current background color is not white/highlighted | Current: {current_background_color}"

    def validate_default_icon_highlight(self):
        icon_color_dictionary = {
            "Bottle Icon": self.get_element_background_color(TopLevelDashBoardScreenLocators.BOTTLE_ICON),
            "Solvent Icon": self.get_element_background_color(TopLevelDashBoardScreenLocators.SOLVENT_ICON),
            "Sample Icon": self.get_element_background_color(TopLevelDashBoardScreenLocators.SAMPLE_ICON),
            "Column Icon": self.get_element_background_color(TopLevelDashBoardScreenLocators.COLUMN_ICON),
            "TUV Icon": self.get_element_background_color(TopLevelDashBoardScreenLocators.TUV_ICON)}

        for color in icon_color_dictionary:
            assert icon_color_dictionary[color] != "fff" and icon_color_dictionary[
                color] != "rgba(0, 0, 0, 0)", f"Icon is highlighted when it should not be. Icon highlighted: {color}"

    def select_notification_icon(self):
        # This will be removed once we get the correct requirement for the notification toast
        time.sleep(30)
        # as of now it occurs sporadically and it is hard coded on development side
        # As we don't have any triggering mechanism to make the notification visible.once it is integrated with the bridges we
        # will have a mechanism to have notification at will to test this  functionality
        icon_element = self.get_element(DashBoardsScreenPageLocators.NOTIFICATION)
        icon_class_string = icon_element.get_attribute("class")
        assert "tray-icon-circle" in icon_class_string, "Invalid status {status}"
        assert "available" in icon_class_string, "Invalid status {status}"
        self.tap(DashBoardsScreenPageLocators.NOTIFICATION)

    def validate_lock_icon(self):
        locator = DashBoardsScreenPageLocators.LOCK_ICON
        screen_name = "lock icon"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_dashboard_screen(self):
        locator = DashBoardsScreenPageLocators.HOME
        screen_name = "lock icon"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_top_level_dashboard(self):
        locator = TopLevelDashBoardScreenLocators.BOTTLE_ICON
        screen_name = "Top level dashboard"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_user_settings_icon(self):
        self.tap(DashBoardsScreenPageLocators.USER_SETTINGS)

    def tap_plots_icon(self):
        self.tap(DashBoardsScreenPageLocators.PLOTS)

    def get_current_flow(self):
        return self.get_current_flow_rate(TopLevelDashBoardScreenLocators.FLOW_READ_BACK_MESSAGE)

    def get_current_flow_units(self):
        return self.get_current_flow_unit(TopLevelDashBoardScreenLocators.FLOW_UNITS)

    def get_column_position_read_back(self):
        column_position = self.get_text(TopLevelDashBoardScreenLocators.COLUMN_POSITION)
        return column_position

    def get_sample_temperature(self):
        sample_temperature = self.get_temperature(TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE,
                                                  TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE_AFTER_DECIMAL)
        return TypeConverter.to_float(sample_temperature)

    def get_sample_temperature_setpoint(self):
        sample_temperature_setpoint = self.get_temperature(TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE_SETPOINT,
                                                           TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE_SETPOINT_AFTER_DECIMAL)
        return TypeConverter.to_float(sample_temperature_setpoint)

    def get_column_temperature(self):
        column_temperature = self.get_temperature(TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE,
                                                  TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE_AFTER_DECIMAL)
        return TypeConverter.to_float(column_temperature)

    def get_column_temperature_units(self):
        return self.get_temperature_units(TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE_UNITS)

    def get_column_temperature_actual(self):
        column_temperature_actual = self.get_temperature(TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE_ACTUAL,
                                                         TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE_ACTUAL_AFTER_DECIMAL)
        return TypeConverter.to_float(column_temperature_actual)

    def get_system_pressure_solvent_card_reader(self):
        self.wait_time_to_load_value(TopLevelDashBoardScreenLocators.SOLVENT_CARD_NUMBER_VALUE)
        self.wait_time_to_load_value(TopLevelDashBoardScreenLocators.SOLVENT_CARD_DECIMAL_VALUE)
        return self.get_system_pressure(
            TopLevelDashBoardScreenLocators.SOLVENT_CARD_NUMBER_VALUE,
            TopLevelDashBoardScreenLocators.SOLVENT_CARD_DECIMAL_VALUE)

    def get_system_pressure_card_reader_unit(self):
        time.sleep(1)
        return self.get_text(TopLevelDashBoardScreenLocators.SOLVENT_CARD_PRESSURE_UNIT)

    def get_system_pressure_with_units(self):
        current_system_pressure = self.get_system_pressure_solvent_card_reader()
        current_system_pressure = str(current_system_pressure)
        current_pressure_unit = self.get_system_pressure_card_reader_unit()
        current_pressure_unit = str(current_pressure_unit)
        self.logger.info(f"current_pressure_unit =={current_pressure_unit}")
        current_system_pressure = current_system_pressure + ' ' + current_pressure_unit
        current_system_pressure = current_system_pressure.strip()
        return current_system_pressure

    def get_valve_position_sample_card_reader(self):
        return BasePage.get_text(self, TopLevelDashBoardScreenLocators.SAMPLE_CARD_VALVE_POSITION)

    def get_lamp_state(self):
        return self.get_text(TopLevelDashBoardScreenLocators.LAMP_STATE)

    def get_channel_a_absorbance_value(self):
        return self.get_condition_card_value(TopLevelDashBoardScreenLocators.CHANNEL_A_ABSORBANCE_VALUE_BEFORE_DECIMAL,
                                             TopLevelDashBoardScreenLocators.CHANNEL_A_ABSORBANCE_VALUE_AFTER_DECIMAL)

    def get_channel_b_absorbance_value(self):
        return self.get_condition_card_value(TopLevelDashBoardScreenLocators.CHANNEL_B_ABSORBANCE_VALUE_BEFORE_DECIMAL,
                                             TopLevelDashBoardScreenLocators.CHANNEL_B_ABSORBANCE_VALUE_AFTER_DECIMAL)

    def get_single_wavelength_value(self):
        self.logger.info("Inside the get first wavelength")
        first_wavelength_value = self.get_container_text(TopLevelDashBoardScreenLocators.WAVE_LENGTH_1_READ_BACK_VALUE)
        first_wavelength_unit = self.get_container_text(TopLevelDashBoardScreenLocators.WAVE_LENGTH_1_READ_BACK_UNITS)
        self.logger.info(f"first_wavelength_value===>>>>>  {first_wavelength_value}")
        self.logger.info(f"first_wavelength_unit===>>>>>  {first_wavelength_unit}")
        first_wavelength = str(first_wavelength_value) + ' ' + first_wavelength_unit
        first_wavelength = first_wavelength.strip()
        return first_wavelength

    def get_dual_wavelength_value(self):
        self.logger.info("Inside the get first wavelength")
        second_wavelength_value = self.get_container_text(TopLevelDashBoardScreenLocators.WAVE_LENGTH_2_READ_BACK_VALUE)
        second_wavelength_unit = self.get_container_text(TopLevelDashBoardScreenLocators.WAVE_LENGTH_2_READ_BACK_UNITS)
        self.logger.info(f"first_wavelength_value===>>>>>  {second_wavelength_value}")
        self.logger.info(f"first_wavelength_unit===>>>>>  {second_wavelength_unit}")
        first_wavelength = str(second_wavelength_value) + ' ' + second_wavelength_unit
        second_wavelength = first_wavelength.strip()
        return second_wavelength

    def validate_lamp_off_for_dual_wavelength(self, expected_second_wave_length):
        """
        This function validates the tuv card reader when the lamp is off and wavelength is in dual mode
        :param expected_second_wave_length: Expected second wavelength
        :return: Void
        """
        # TODO The assertions are commented out because of the defect ins-18751
        self.logger.info("when the lamp is off and wavelength  is Dual")
        actual_single_observance_value = self.get_channel_a_absorbance_value()
        expected_absorbance_value = TUVConditionCardConstants.NoAbsorbanceValue
        assert actual_single_observance_value == expected_absorbance_value, f"The actual single absorbance value {actual_single_observance_value}"
        actual_dual_observance_value = self.get_channel_b_absorbance_value()
        assert actual_dual_observance_value == expected_absorbance_value, f"The actual dual absorbance value {actual_dual_observance_value}"
        actual_dual_wavelength = self.get_dual_wavelength_value()
        # assert actual_dual_wavelength == expected_second_wave_length, f"The actual dual wavelength value {actual_dual_wavelength}"

    def validate_lamp_off_for_single_wavelength(self):
        """
        This function validates the tuv card reader when the lamp is off and wavelength is in single mode
        :return: Void
        """
        self.logger.info("when the lamp is off and wavelength  is single")
        actual_single_observance_value = self.get_channel_a_absorbance_value()
        expected_a_value = TUVConditionCardConstants.NoAbsorbanceValue
        assert actual_single_observance_value == expected_a_value, f"The actual single absorbance value {actual_single_observance_value}"

    def validate_lamp_on_for_dual_wavelength(self):
        """
        This function validates the tuv card reader when the lamp is on and wavelength is in dual mode
        :return: Void
        """
        self.logger.info("when the lamp is on and wavelength  is Double")
        # TODO The assertions are commented out because of the defect ins-18751
        actual_single_absorbance_value = self.get_channel_a_absorbance_value()
        actual_dual_absorbance_value = self.get_channel_b_absorbance_value()
        channel_a_absorbance_unit = self.get_container_text(
            TopLevelDashBoardScreenLocators.CHANNEL_A_ABSORBANCE_UNITS)
        assert channel_a_absorbance_unit == TUVConditionCardConstants.AbsorbanceUnits, f"channel_a_absorbance_unit is {channel_a_absorbance_unit}"
        channel_b_absorbance_unit = self.get_container_text(
            TopLevelDashBoardScreenLocators.CHANNEL_B_ABSORBANCE_UNITS)
        assert channel_b_absorbance_unit == TUVConditionCardConstants.AbsorbanceUnits, f"channel_a_absorbance_unit is {channel_b_absorbance_unit}"
        # assert actual_single_absorbance_value in numpy.arange(TUVConditionCardConstants.MinAbsorbanceValue,
        #                                                       TUVConditionCardConstants.MaxAbsorbanceValue)
        # assert actual_dual_absorbance_value in numpy.arange(TUVConditionCardConstants.MinAbsorbanceValue,
        #                                                       TUVConditionCardConstants.MaxAbsorbanceValue)

        actual_dual_wavelength = self.get_dual_wavelength_value()
        # assert actual_dual_wavelength == expected_second_wave_length

    def validate_lamp_state_on_for_single_wavelength(self):
        """
        This function validates the tuv card reader when the lamp is on and wavelength is in dual mode
        :return: Void
        """
        # TODO The assertions are commented out because absorbance value is hardcode in the ui side.
        self.logger.info("when the lamp is on and wavelength  is single")
        channel_a_absorbance_unit = self.get_container_text(
            TopLevelDashBoardScreenLocators.CHANNEL_A_ABSORBANCE_UNITS)
        assert channel_a_absorbance_unit == TUVConditionCardConstants.AbsorbanceUnits, f"channel_a_absorbance_unit is {channel_a_absorbance_unit}"
        actual_single_absorbance_value = self.get_channel_a_absorbance_value()
        # assert actual_single_absorbance_value in numpy.arange(TUVConditionCardConstants.MinAbsorbanceValue,
        #                                                       TUVConditionCardConstants.MaxAbsorbanceValue)

        is_dual_wavelength_visible = self.is_displayed(
            TopLevelDashBoardScreenLocators.WAVE_LENGTH_2_READ_BACK_UNITS)
        self.logger.info(f" ===is_dual_wavelength_visible===>>>>{is_dual_wavelength_visible}")
        assert is_dual_wavelength_visible is False, "The channel B wavelength is visible"

    def tap_second_carosel_dot(self):
        self.tap(DashBoardsScreenPageLocators.HEALTH_PAGE_TWO)

    def get_sample_pressure_value(self):
        return self.get_condition_card_value(TopLevelDashBoardScreenLocators.SAMPLE_PRESSURE_VALUE,
                                             TopLevelDashBoardScreenLocators.SAMPLE_PRESSURE_AFTER_DECIMAL_VALUE)

    def get_sample_pressure_units(self):
        return self.get_text(TopLevelDashBoardScreenLocators.SAMPLE_PRESSURE_UNITS)

    def validate_idle_state(self):
        self.validate_simple_text_wait_condition(
            DashBoardsScreenPageLocators.SYSTEM_STATE,
            SystemStateConstants.IdleSystemState, SystemStateConstants.MaxiTimeToIdle)

    def validate_error_state(self):
        self.validate_simple_text_wait_condition(
            DashBoardsScreenPageLocators.SYSTEM_STATE,
            SystemStateConstants.ErrorSystemState, 10)

    def validate_resetting_state(self):
        self.validate_simple_text_wait_condition(
            DashBoardsScreenPageLocators.SYSTEM_STATE,
            SystemStateConstants.ResettingSystemState, SystemStateConstants.MaxiTimeToIdle)

    def set_current_system_pressure(self, current_system_pressure):
        self.current_system_pressure = current_system_pressure

    def get_current_system_pressure(self):
        return self.current_system_pressure

    def get_total_lamp_hours(self):
        total_lamp_hours = self.get_container_text(TopLevelDashBoardScreenLocators.LAMP_TOTAL_HOURS_READBACK_MESSAGE)
        total_lamp_hours = total_lamp_hours[1:]
        return total_lamp_hours

    def get_flow_state(self):
        locator = self.get_element(DashBoardsScreenPageLocators.FLOW_PATH_LINE)
        flow_state_class = locator.get_attribute("class")
        self.logger.debug(f" The flow state is {flow_state_class}")
        flow_state = flow_state_class.find("flowOn")
        if flow_state == -1:
            return False
        else:
            return True

    def get_sample_injection_count(self):
        return self.get_text(TopLevelDashBoardScreenLocators.SAMPLE_INJECTIONS_COUNT)

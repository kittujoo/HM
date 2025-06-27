# """
# File_Name: temperature_condition_card_base.py
# Desc: This file contains common function that can be used on all the temperature condition card
# __copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 03/29/2021
# --modified__ = "Sharmila Vairamani" Changed the function description common to all temperature condition cards - 04/06/2021
# __modified__ "Sharmila Vairamani" Removed validate title icon color method - 04/20/2021
# __modified__ "Sharmila Vairamani" Added logging statement - 04/22/2021


# """

import time

from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import TemperatureConditionCardConstants
from web_framework.kiosk.common.Models.ConditionalCard.TemperatureConditionDetails import TemperatureConditionCardDetails
from web_framework.kiosk.common.Utilities.style_attribute_parser import StyleAttributeParser
from web_framework.kiosk.pages.base_page import BasePage


class TemperatureConditionCardBase(BasePage):
    def __init__(self, driver, base_url, assert_timeout: AssertTimeout, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.locators_class = None
        self._assert_timeout = assert_timeout

    def ignore_initial_conditional_card_details(self, test_page, ignore_initial_message,
                                                ignored_initial_message,
                                                max_time_to_reach_expected_temperature,
                                                max_time_to_ignore_initial_message,
                                                start_time):
        """
        desc: This function is to ignore the initial status read back message in the temperature of the condition card
             In some scenario, the user sets the temperature in a particular page and tap the "DONE" button.
            This will immediately take the user to the condition card where he can see the status.
            The test script is too quick so as soon as the done button is clicked it will pick up the previous state
            message ( for example it the column is switched off and turn it on to heat , then in the condition car
            d the initial message would be "OFF" ). but when we do this manually we cannot see the previous condition.
            Therefore I created this function which will remove some of the messages that gives incorrect information.
        @param test_page:
        @param ignore_initial_message:
        @param ignored_initial_message:
        @param max_time_to_reach_expected_temperature:
        @param max_time_to_ignore_initial_message:
        @param start_time:
        @return:
        """

        while time.time() - start_time < int(max_time_to_reach_expected_temperature):
            read_back_message = test_page.get_status_read_back()
            actual_temperature = test_page.get_current_temperature()
            self.logger.info(
                f"The current temperature from ignore initial conditional card ====> {actual_temperature}")
            self.logger.info(f"The current read back message ====>{read_back_message}<==")

            if not read_back_message or read_back_message.isspace():
                self.logger.debug(f"ignore_initial_conditional_card_details(), not is space")
                continue

            if not ignored_initial_message and read_back_message == ignore_initial_message:
                if time.time() - start_time > int(max_time_to_ignore_initial_message):
                    self.logger.debug(
                        "ignore_initial_conditional_card_details(), ignore initial message time limit is over")
                    break
                else:
                    self.logger.debug("ignore_initial_conditional_card_details(), to ignore initial message")
                continue

            if actual_temperature.startswith('Off'):
                self.logger.debug(f"ignore_initial_conditional_card_details(), actual_temperature starts with Off")
                continue

            break
        return

    def read_conditional_card_detail(self, test_page):
        """
        desc: This function gives the current temperature and current status read back of temperature condition card
        @param test_page:
        @return: Temperature Condition Card object
        """
        read_back_message = test_page.get_status_read_back()
        current_temperature = test_page.get_current_temperature()
        if current_temperature is None:
            return None
        current_temperature = float(current_temperature)
        title_icon_status = test_page.get_title_icon_status(self.locators_class.TEMPERATURE_TITLE_ICON)
        self.logger.info(f"current_title_icon_status==>>{title_icon_status}")
        progress_bar_start_point = test_page.get_progress_bar_left_point()
        progress_bar_end_point = test_page.get_progress_bar_right_point()

        return TemperatureConditionCardDetails(read_back_message, current_temperature, title_icon_status,
                                               progress_bar_start_point, progress_bar_end_point)

    def validate_read_back_messages(self, test_page,
                                    expected_conditional_card_detail,
                                    possible_messages,
                                    ignore_initial_message,
                                    max_time_to_reach_expected_temperature):
        """
        desc: This function is to validate the status read back message of the temperature condition card with the possible
        messages
        @param test_page:
        @param expected_conditional_card_detail:
        @param possible_messages:
        @param ignore_initial_message:
        @param max_time_to_reach_expected_temperature:
        @return: void
        """
        initial_actual_status_message = self.get_status_read_back()
        self.logger.info(f" Initial actual status message => {initial_actual_status_message}")
        start_time = time.time()
        ignored_initial_message = False

        # max_time_to_ignore_initial_message is the maximum extended time we can ignore the initial message.
        # We don't have any requirement at this point.
        # max_time_to_ignore_initial_message is calculated by taking 1/4 of the maximum time
        # to reach the expected temperature.

        max_time_to_ignore_initial_message = max_time_to_reach_expected_temperature / 4

        test_page.ignore_initial_conditional_card_details(test_page,
                                                          ignore_initial_message,
                                                          ignored_initial_message,
                                                          max_time_to_reach_expected_temperature,
                                                          max_time_to_ignore_initial_message,
                                                          start_time)
        self.logger.info(f" ignore_initial_conditional_card_details")

        actual_conditional_card_detail = self.read_conditional_card_details(expected_conditional_card_detail,
                                                                            test_page,
                                                                            max_time_to_reach_expected_temperature,
                                                                            possible_messages,
                                                                            start_time)

        self.validate_conditional_card_final_status(actual_conditional_card_detail, expected_conditional_card_detail)

    def validate_conditional_card_final_status(self, actual_conditional_card_detail, expected_conditional_card_detail):
        """
        desc: This function is to validate between actual and expected condition card details of the temperature
        @param actual_conditional_card_detail:
        @param expected_conditional_card_detail:
        @return: void
        """
        self.logger.info(f"The actual read card details======>>>{actual_conditional_card_detail.read_back_message}")
        self.logger.info(f"The expected read card details===>> {expected_conditional_card_detail.read_back_message} ")
        assert actual_conditional_card_detail.read_back_message == expected_conditional_card_detail.read_back_message
        actual_temperature = round(actual_conditional_card_detail.temperature)
        expected_temperature = round(expected_conditional_card_detail.temperature)
        assert actual_temperature <= expected_temperature, f"actual_temperature=={actual_temperature},expected_temperature =={expected_temperature} "

    def read_conditional_card_details(self, expected_conditional_card_detail, test_page,
                                      max_time_to_reach_expected_temperature, possible_messages, start_time):
        """
        desc:This function validates the temperature and the status read back messages for the given temperature
        forexample:if the temperature is changed from 20 c to 40 c then this function will validate, there is rise in temperature
        so the status read back message should be "HEATING IS ON" and  vice versa for the temperature other way around
        @param expected_conditional_card_detail:
        @param test_page:
        @param max_time_to_reach_expected_temperature:
        @param possible_messages:
        @param start_time:
        @return: conditional card detail object
        """

        time.sleep(2)  # TODO remove this time sleep and add a validation function
        self.logger.info(f"possible_messages => {possible_messages}")
        raise_in_temperature_set = False
        previous_conditional_card_detail = None
        current_conditional_card_detail = test_page.read_conditional_card_detail(
            test_page)
        self.logger.info(f"expected_conditional_card_detail.title_icon_status ====>>>> {expected_conditional_card_detail.title_icon_status}")
        self.logger.info(f"current_conditional_card_detail.title_icon_status ===>>> {current_conditional_card_detail.title_icon_status}")

        start_time = time.time()
        while time.time() - start_time < int(max_time_to_reach_expected_temperature):
            current_conditional_card_detail = test_page.read_conditional_card_detail(
                test_page)
            self.logger.info(f"current_conditional_card_detail===>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{current_conditional_card_detail.read_back_message}")
            self.logger.info(
                f"expected_conditional_card_detail===>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{expected_conditional_card_detail.read_back_message}")
            self.logger.info(f"current_title_icon_status============>>>>>>{current_conditional_card_detail.title_icon_status}")

            if current_conditional_card_detail is not None:
                if not raise_in_temperature_set:
                    raise_in_temperature_set = True
                    raise_in_temperature = self.set_conditional_card_expectations(current_conditional_card_detail,
                                                                                  expected_conditional_card_detail,
                                                                                  possible_messages)
                    self.logger.info(
                        f"current_conditional_card_detail===>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{current_conditional_card_detail.read_back_message}")

                self.validate_read_back_message(possible_messages, current_conditional_card_detail.read_back_message)

                if current_conditional_card_detail.read_back_message == expected_conditional_card_detail.read_back_message:
                    break

                self.validate_conditional_card_intermediate_status(raise_in_temperature,
                                                                   current_conditional_card_detail,
                                                                   expected_conditional_card_detail,
                                                                   previous_conditional_card_detail)
                previous_conditional_card_detail = current_conditional_card_detail
                time.sleep(.01)

        conditional_card_detail = TemperatureConditionCardDetails(current_conditional_card_detail.read_back_message,
                                                                  current_conditional_card_detail.temperature)
        return conditional_card_detail

    def set_conditional_card_expectations(self, current_conditional_card_detail, expected_conditional_card_detail,
                                          possible_messages):
        """
        This function sets the expected conditional card detail that needs to be validated while the column or sample
        manager is in heating or cooling mode
        @param current_conditional_card_detail: current details in the condition card
        @param expected_conditional_card_detail: expected detail in the condition card depending upon cooling or
        heating mode of the column manager/ sample manager
        @param possible_messages: possible read back messages in the condition card
        @return:
        """
        raise_in_temperature = expected_conditional_card_detail.temperature > current_conditional_card_detail.temperature
        self.logger.info(f"raise_in_temperature => {raise_in_temperature}, "
                         f"current_temperature = {current_conditional_card_detail.temperature}, "
                         f"target => {expected_conditional_card_detail.temperature},"
                         f" title icon status => {expected_conditional_card_detail.title_icon_status}")
        if raise_in_temperature:
            expected_conditional_card_detail.title_icon_status = TemperatureConditionCardConstants.TitleIconWarmStatus
            possible_messages.append(TemperatureConditionCardConstants.HeatingOnMessage)

        else:
            expected_conditional_card_detail.title_icon_status = TemperatureConditionCardConstants.TitleIconCoolStatus
            possible_messages.append(TemperatureConditionCardConstants.CoolingOnMessage)
        return raise_in_temperature

    def validate_read_back_message(self, possible_messages, read_back_message):
        """
        desc: This function to validate possible messages are in the status read back message of the temperature condition card
        @param possible_messages:
        @param read_back_message:
        @return: void
        """
        if read_back_message not in possible_messages:
            self.logger.debug(f"Unexpected message => {read_back_message}<-")
            assert False, f"Unexpected message => {read_back_message}"

    def validate_conditional_card_intermediate_status(self, raise_in_temperature, actual_conditional_card_detail,
                                                      expected_conditional_card_detail,
                                                      previous_conditional_card_detail):
        """
        desc:This function is to validate the increase or decrease of the temperature is linear in the progress bar ui component.
            When temp increases, right stays same and left increases, finally left is unset.
            When temp decreases, left stays same  and right increases, finally  right is unset

        @param raise_in_temperature:
        @param actual_conditional_card_detail:
        @param expected_conditional_card_detail:
        @param previous_conditional_card_detail
        @return: void
        """

        assert actual_conditional_card_detail.validate_progress_bar_values(previous_conditional_card_detail,
                                                                           raise_in_temperature)
        self.logger.info(f"raise_in_temperature===>>{raise_in_temperature}")
        raise_in_temperature = bool(raise_in_temperature)
        self.logger.info(f"actual_conditional_card_detail.temperature==={actual_conditional_card_detail.temperature}")
        self.logger.info(f"expected_conditional_card_detail.temperature==={expected_conditional_card_detail.temperature}")
        self.logger.info("After asserting raise in temperature")
        self.logger.info(f"previous conditional card detail=======>{previous_conditional_card_detail}")

        if raise_in_temperature:
            self.logger.info(f" Inside the raise in tmeperature")
            assert actual_conditional_card_detail.temperature <= expected_conditional_card_detail.temperature + 5, f" The actual temperature is {actual_conditional_card_detail.temperature}"

        else:
            self.logger.info(f" Inside the raise in temperature false")
            assert actual_conditional_card_detail.temperature >= expected_conditional_card_detail.temperature, f" The actual temperature is {actual_conditional_card_detail.temperature}"

        # assert actual_conditional_card_detail.title_icon_status == expected_conditional_card_detail.title_icon_status, \
        #     f" The current title icon = >{actual_conditional_card_detail.title_icon_status}, The expected title icon => {expected_conditional_card_detail.title_icon_status}"

    def validate_temperature_units(self):
        """
        This function validates the read back units messages for the current and setpoint temperature in the
        temperature conditional card

        """
        actual_setpoint_temperature_units = self.get_setpoint_temperature_units()
        expected_setpoint_temperature_units = TemperatureConditionCardConstants.SetpointTemperatureUnits
        assert actual_setpoint_temperature_units == expected_setpoint_temperature_units, f"actual setpoint unit read back message => {actual_setpoint_temperature_units}"

        actual_current_temperature_units = self.get_current_temperature_units()
        expected_current_temperature_units = TemperatureConditionCardConstants.CurrentTemperatureUnits
        assert actual_current_temperature_units == expected_current_temperature_units, f"actual current unit read back message => {actual_current_temperature_units}"

    def validate_temperature_in_condition_card(self):
        """
        This function validates current temperature and set point temperature in the condition card
        @return: void
        """
        current_temperature = self.get_current_temperature()
        current_temperature = TypeConverter.to_float(current_temperature)
        setpoint_temperature = self.get_setpoint_temperature()
        setpoint_temperature = TypeConverter.to_float(setpoint_temperature)
        self.logger.info(f"The setpoint temperature is {setpoint_temperature}")
        assert (setpoint_temperature - 5) <= current_temperature <= (
                setpoint_temperature + 5), f"The actual set pointed temperature {setpoint_temperature},current_temperature ==>{current_temperature}"

    def validate_final_title_icon_color(self, locator_to_validate, expected_color_code):
        """
        This function validates the title icon color in the conditional card once the set point temperature is reached
        @return: void
        """
        property_name = "color"
        actual_final_title_icon_color_code = self.get_title_icon_color_code(locator_to_validate, property_name)
        expected_final_title_icon_color_code = expected_color_code
        assert expected_final_title_icon_color_code in actual_final_title_icon_color_code, f"actual final icon is {actual_final_title_icon_color_code}"

    def get_current_temperature(self):
        """
        This function gets the current temperature from the conditional card
        @return: temperature
        """
        self._assert_timeout.are_not_equal(
            actual=lambda: self.get_temperature(self.locators_class.CURRENT_TEMPERATURE, self.locators_class.CURRENT_TEMPERATURE_AFTER_DECIMAL),
            expected='--',
            failure_message="Temperature is not displayed in the UI", timeout_in_seconds=15
        )
        current_temperature = self.get_temperature(self.locators_class.CURRENT_TEMPERATURE, self.locators_class.CURRENT_TEMPERATURE_AFTER_DECIMAL)
        return current_temperature

    def get_current_temperature_units(self):
        """
        This function gets the current temperature units from the conditional card
        @return: current temperature units
        """
        return self.get_temperature_units(self.locators_class.CURRENT_TEMPERATURE_UNITS)

    def get_setpoint_temperature(self):
        """
        This function gets the setpoint temperature in the conditional card
        @return: setpoint temperature
        """
        setpoint_temperature = self.get_temperature(self.locators_class.SETPOINT_TEMPERATURE,
                                                    self.locators_class.SETPOINT_TEMPERATURE_AFTER_DECIMAL)
        return setpoint_temperature

    def get_setpoint_temperature_units(self):
        """
        This function gets the setpoint temperature units from the conditional card
        @return: setpoint temperature units
        """
        return self.get_temperature_units(self.locators_class.SETPOINT_TEMPERATURE_UNITS)

    def validate_temperature(self, expected_temperature):
        """
        This function validates the setpoint temperature in the condition card is reached within the time frame
        @param expected_temperature:
        @return: void
        """
        start_time = time.time()
        actual_temperature = None
        while time.time() - start_time < int(TemperatureConditionCardConstants.MaxTimeToReachTemperature):
            actual_temperature = self.get_current_temperature()
            if actual_temperature == expected_temperature:
                break
            time.sleep(1)
        assert expected_temperature == actual_temperature, f" actual_temperature ==>> {actual_temperature}, " \
                                                           f"expected_temperature ==>> {expected_temperature}"

    def validate_off_setpoint_temperature(self):
        """
        This function is to validate no temperature is set in the conditional card
        @return:
        """
        setpoint_temperature = None
        start_time = time.time()
        while time.time() - start_time < int(TemperatureConditionCardConstants.MaxTimeToReachTemperature):
            setpoint_temperature = self.get_setpoint_temperature()
            if setpoint_temperature == TemperatureConditionCardConstants.NoSetpointTemperatureMessage:
                break
            time.sleep(1)
        assert setpoint_temperature == TemperatureConditionCardConstants.NoSetpointTemperatureMessage, f" The actual temperature set when the toggle button is switced off => {setpoint_temperature}"

    def get_status_read_back(self):
        """
        This function gets the read back messages in the conditional card which tells the user
        whether the temperature is increasing or decreasing
        @return: status_read_back_message
        """
        time.sleep(5)
        status_read_back_message = self.get_text(self.locators_class.STATUS_READ_BACK)
        return status_read_back_message.strip()

    def get_progress_bar_status(self):
        """
        This function gets the status of the progress bar in the conditional card
        @return: progress_bar_status
        """
        progress_bar_status = self.get_element(self.locators_class.PROGRESS_BAR_COMPONENT)
        progress_bar_status = progress_bar_status.get_attribute("style")
        return progress_bar_status

    def get_progress_bar_left_point(self):
        """
        This function gets the left point value of the progress bar which is use to validate
        whether temperature is increasing or decreasing
        @return: progress_bar_left_point_value
        """
        progress_bar_status = self.get_progress_bar_status()
        parser = StyleAttributeParser()
        style_dictionary = parser.parse(progress_bar_status, ";", ":")
        progress_bar_left_point_value = style_dictionary["left"]
        return progress_bar_left_point_value

    def get_progress_bar_right_point(self):
        """
        This function gets the right point value of the progress bar which is use to validate
        whether temperature is increasing or decreasing
        @return: progress_bar_right_point_value
        """
        progress_bar_status = self.get_progress_bar_status()
        parser = StyleAttributeParser()
        style_dictionary = parser.parse(progress_bar_status, ";", ":")
        progress_bar_right_point_value = style_dictionary["right"]
        return progress_bar_right_point_value

    def validate_setpoint_temperature_turned_on(self):
        """
        This function is to validate some temperature is set in the conditional card
        @return:
        """
        setpoint_temperature = None
        start_time = time.time()
        while time.time() - start_time < int(TemperatureConditionCardConstants.MaxTimeToReachTemperature):
            setpoint_temperature = self.get_setpoint_temperature()
            if setpoint_temperature != TemperatureConditionCardConstants.NoSetpointTemperatureMessage:
                break
            time.sleep(1)
        assert setpoint_temperature != TemperatureConditionCardConstants.NoSetpointTemperatureMessage, f"The actual temperature set when the toggle button is switced off => {setpoint_temperature}"

import os
import time
import traceback
from typing import List

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.workflow_common_constant import WorkflowCommonConstant
from web_framework.kiosk.common.Constants.UI.condition_card_constants import TUVConditionCardConstants
from web_framework.kiosk.common.Constants.dashboard_constants import SystemStateConstants
from web_framework.kiosk.pages.Handlers.input_stepper_handler import InputStepperHandler
from web_framework.kiosk.pages.Handlers.num_pad_handler import NumPadHandler
from web_framework.kiosk.pages.Handlers.onscreen_keyboard_handler import OnscreenKeyboardHandler
from web_framework.kiosk.pages.Handlers.picker_spinner_handler import PickerSpinnerHandler
from web_framework.kiosk.pages.Handlers.touch_actions_handler import TouchActionsHandler
from web_framework.kiosk.pages.Handlers.web_elements_handler import WebElementsHandler
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.commands_screen_locators import CommandsScreenPageLocators
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.Utilities.kiosk_utilities import KioskUtilities
from web_framework.web_driver_common.element import is_displayed, get_text

logger = Logger(os.path.basename(__file__))


class BasePage:
    """######################
    ##### CORE METHODS ########
    ######################"""

    # ##### CORE FUNCTIONAL

    def __init__(self, driver, base_url, **kwargs):
        """To initialize the _driver and URL
        :param driver:
        :param base_url:
        """
        self.URL = base_url
        self._driver = driver
        self.wait_time = 5
        self.long_wait_time = 10

    def set_driver(self, driver):
        self._driver = driver

    def get_driver(self):
        return self._driver

    def visit(self):
        """ To go to the URL that has been constructed in initializer method """
        logger.debug(f"Url to visit => {self.URL}")
        self._driver.get(self.URL)

    def get_current_url(self):
        """
        Gets the URL of the current page
        :return: current url
        """
        try:
            return self._driver.current_url
        except Exception:
            assert False, " The current url is not found "

    def delete_cookies(self):
        """
        Delete all cookies in the scope of the session.
        :return:
        """
        self._driver.delete_all_cookies()

    def wait_for_load(self, seconds):
        self._driver.set_page_load_timeout(seconds)

    def wait_for_element_load(self, element, max_wait_time):
        """
        This function is used to create wait time in order to wait for a specified element to be displayed/loaded into KIOSK
        @param element: The element to be waited on
        @param max_wait_time: The maximum amount of time (in seconds) for this function to look for the conditional change
        @return:
        """
        # sleep added due to issues with execution being faster than the element actually showing up in the application
        time.sleep(1)
        start_time = time.time()
        while time.time() - start_time < max_wait_time:

            if self.is_displayed(element):
                break
            time.sleep(1)
        assert self.is_displayed(element), f"The given target element was not found within the time allotted"

    def wait_for_element_enable(self, element, max_wait_time):
        """
        This function is used to create wait time in order to wait for a specified element to get enabled in KIOSK
        @param element: The element to be waited on
        @param max_wait_time: The maximum amount of time (in seconds) for this function to look for the conditional change
        @return:
        """
        start_time = time.time()
        while time.time() - start_time < max_wait_time:
            if not self.is_disabled(element):
                break
            time.sleep(1)
        assert not self.is_disabled(element), f"The given target element was not enabled within the time allotted"

    def validate_simple_text_wait_condition(self, text_element, target_text, max_wait_time):
        """
        This function is used to create wait time in order to look for a change in a text condition
        This simple version is used for instances where we DO NOT care about the previous text in an element
        @param text_element: The element with changing text
        @param target_text: The text in which the element should end with
        @param max_wait_time: The maximum amount of time (in seconds) for this function to look for the conditional change
        @return:
        """
        start_time = time.time()
        current_text = None
        while time.time() - start_time < max_wait_time:
            current_text = self.get_text(text_element)
            logger.debug(f"current_text===>>>{current_text}")

            if current_text == target_text:
                break
            time.sleep(1)
        assert current_text == target_text, f"The given target text was not found within the time allotted,  current_text ={current_text}"

    def validate_text_wait_condition(self, text_element, starting_text_constant, target_text_constant, max_wait_time):
        """
        This function is used to create wait time in order to look for a change in a text condition
        This version is used for instances where we DO care about the previous text in an element
        @param text_element: The element with changing text
        @param starting_text_constant: The constant text in which the text element starts with
        @param target_text_constant: The constant text in which the element should end with
        @param max_wait_time: The maximum amount of time (in seconds) for this function to look for the conditional change
        @return:
        """
        starting_text = self.get_text(text_element)
        assert starting_text == starting_text_constant

        start_time = time.time()
        current_text = None
        while time.time() - start_time < max_wait_time:
            current_text = self.get_text(text_element)

            if current_text == target_text_constant:
                break
            time.sleep(1)
        assert current_text == target_text_constant, f"The given target text was not found within the time allotted"

    def validate_element_wait_condition(self, starting_element, target_element, max_wait_time):
        """
        This function is used to create wait time in order to look for a change in element display condition
        @param starting_element: The starting element or control of the test
        @param target_element: The ending element to look for that should be present within wait time
        @param max_wait_time: The maximum amount of time (in seconds) for this function to look for the conditional change
        @return:
        """
        WebDriverWait(self._driver, 30).until(EC.visibility_of_element_located(starting_element))
        assert self.is_displayed(starting_element)
        logger.info(f"starting_element===>>>{starting_element}")

        start_time = time.time()
        while time.time() - start_time < max_wait_time:
            logger.info(f"target_element===>>>{target_element}")

            if self.is_displayed(target_element):
                logger.info(f"target_element===>>>{target_element}")
                break
            time.sleep(1)
        assert self.is_displayed(target_element), f"The given target element was not found within the time allotted"

    # TODO: Add in a true/false conditional wait [INS-24897]
    # def conditional_bool_wait(self, condition, target_boolean, wait_time):
    #     print()

    def close(self):
        """ To close the page i.e. to close the browser window """
        try:
            if self._driver is not None:
                # print("BasePage, within close()")
                self._driver.close()
                # print("BasePage, within close() to set None")
                self._driver = None
        except:
            self._driver = None

    def press_esc_key(self):
        """
        stimulates the user pressing of ESC key in the key board
        :return: void
        """
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.ESCAPE).perform()
        actions.key_down(keys.Keys.ESCAPE)
        actions.key_up(keys.Keys.ESCAPE)

    def add_xpath_to_locator(self, locator, xpath_addition):
        """
        This method takes base xpath locator, appends more xpath, and returns a new element locator
        @param locator: an xpath locator | ex: //ics-input-stepper
        @param xpath_addition: a string of xpath to be added to the locator | ex: //div[@id='input-plus']
        @return: new locator which combines base locator to the additional xpath | ex: //ics-input-stepper//div[@id='input-plus']
        """
        KioskUtilities(self._driver).add_xpath_to_locator(locator, xpath_addition)

    # ##### CORE VALIDATION ##########################################

    def validate_screen(self, locator, screen_name, wait_time):
        """
        This function is to validate any given screen before execution of the test scripts
        """
        screen_exists = False
        try:
            self.wait_for_element_visibility(wait_time, locator)
            screen_exists = self.is_displayed(locator)
        except Exception:
            time.sleep(wait_time)
            try:
                self.wait_for_element_visibility(wait_time, locator)
                screen_exists = self.is_displayed(locator)
            except Exception as generic_exception:
                traceback.print_exception(type(generic_exception), generic_exception, generic_exception.__traceback__)
        logger.debug(f"The {screen_name} is displayed => {screen_exists}")
        assert screen_exists, f"Failed to move to {screen_name} "

    def implicitly_wait(self):
        """
        Sets a sticky timeout to implicitly wait for an locator to be found,
           or a command to complete. This method only needs to be called one
           time per session.
        :return void:
        """
        self._driver.implicitly_wait(self.wait_time)

    def wait_element_to_be_clickable(self, locator, second_to_wait):
        """
        An Expectation for checking an locator is visible and enabled such that
        you can click it
        :param locator:
        :param second_to_wait:
        :return: void
        """

        try:
            wait = WebDriverWait(self._driver, second_to_wait)
            return wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            assert False, f" The click action on locator {locator} is not complete in enough time {second_to_wait} at basepage::wait_element_to_be_clickable"

    def wait_for_element_visibility(self, wait_time, locator):
        """
        An expectation for checking that all elements are present on the DOM of a
        page and visible. Visibility means that the elements are not only displayed
        but also has a height and width that is greater than 0.h
        :param wait_time:
        :param locator:
        :return:
        """
        try:
            WebDriverWait(self._driver, wait_time).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            assert False, " The locator is not visible in the given time."

    """#############################
    ##### ELEMENT INTERACTION ########
    #############################"""

    def click(self, locator):
        """
        Clicks the element
        :param: locator
        :return:
        """
        try:
            self._driver.find_element(*locator).click()
        except NoSuchElementException:
            assert False, f"The locator{locator}  not found to perform click action"

    def enter_value(self, number):
        """
        THis functions allows the user to enter any number in the numpad entry field
        :param number:
        :return:
        """
        NumPadHandler(self._driver).enter_value(number)

    def clear_num_pad_entries(self, text_field_locator):
        """
       This function clears the content in the numpad entry field
       :param text_field_locator:
       :return:
       """
        NumPadHandler(self._driver).clear_num_pad_entries(text_field_locator)

    def enter_string(self, string):
        """
        This functions allows the user to enter a string into a text area using the on-screen keyboard
        :@param string | ex: "The quick brown fox jumped over the something, I don't remember the rest"
        :return:
        """
        OnscreenKeyboardHandler(self._driver).enter_string(string)

    def clear_text_area(self, text_area_locator, length=1):
        """
        This function clears the content in the numpad entry field
         Args:
            text_area_locator: ex: //textarea
        NOTE: text field must be a text area element in order to pull the ng-reflect-model attribute value
        :return:


        """
        for _ in range(length):
            OnscreenKeyboardHandler(self._driver).clear_text_area(text_area_locator)

    def set_text(self, locator, value):
        """
        Clears the text if it's a text entry locator and Simulates typing into the locator
        :param : locator
        :param :A string for typing, or setting form fields.  For setting
              file inputs, this could be a local file path.
        """

        try:
            target_element = self._driver.find_element(*locator)
            target_element.clear()
            target_element.send_keys(value)
        except NoSuchElementException:
            assert False, f" The locator {locator} not found to perform send keys action"

    def send_keys(self, text):
        """
         Sends keys to current focused element.
        :param:A string
        :return: void
        """
        actions = ActionChains(self._driver)
        actions.send_keys(text).perform()

    def set_toggle_button(self, locator, toggle_button_enabled):
        """
        THis function set the toggle button to the user desired state(enable or disabled)
        :param locator: locator of the toggle button
        :param toggle_button_enabled: desired state( True or False) in boolean
        :return:
        """
        logger.debug(f"The value for the leak  sensor enable is  {toggle_button_enabled}")
        toggle_button_enabled = TypeConverter.to_bool(toggle_button_enabled)
        logger.debug(f"leak_sensor_enabled => {toggle_button_enabled}")
        currently_enabled = self.is_toggle_component_enabled(locator)
        logger.debug(f"currently enabled => {currently_enabled}")
        self.toggle_switch("Leak sensor monitor", locator,
                           currently_enabled, toggle_button_enabled)

    def toggle_switch(self, component_name, locator, current_status, new_status):
        """
        This function is used to turn on or off the toggle component in any kiosk page or screen
        @param component_name: any component that can be turned on or off using a toggle button
        @param locator: locator of the component's toggle button
        @param current_status: initial status of the component toggle button
        @param new_status: final status of the component toggle button
        """
        if current_status and not new_status:
            self.tap(locator)
            logger.debug(f'{component_name} is disabled now')
        elif not current_status and new_status:
            self.tap(locator)
            logger.debug(f'{component_name} is enabled now')
        elif current_status and new_status is True:
            logger.debug(f'{component_name} is already enabled')
        elif not current_status and not new_status:
            logger.debug(f'{component_name} is already disabled')

    """############################
    ##### ELEMENT VALIDATION ########
    ############################"""

    def find_element(self, locator):
        target_element = self._driver.find_element(*locator)
        return target_element
        # return self.wait_element_to_be_clickable(target_element, self.wait_time)

    def find_elements(self, locator) -> List[WebElement]:
        """
        Find elements given a By strategy and locator
        :return: list of WebElement
        """
        return self._driver.find_elements(*locator)

    def get_element(self, locator):
        """
        This function returns the element of the given locator. This method is used mainly when we need to
        manipulate data from the given locator of the webelement.
        :param locator:
        :return: element
        """
        return WebElementsHandler.get_element(self._driver, locator)

    def get_container_text(self, locator):
        """
        Returns the text of the locator from the div/span tags
        :param locator: locator for the web locator
        :return: text of the web locator        """

        return WebElementsHandler.get_container_text(self._driver, locator)

    def get_entered_value(self, locator):
        """
        This function returns the value entered by the user in the text box
        :param locator: locator of the edit field
        :return: value entered by the user
        """
        return WebElementsHandler.get_entered_value(self._driver, locator)

    def is_value_highlighted(self, locator):
        """
        This function verify the value in the edit field is highlighted
        @return : Bool
        """
        value_element = self.get_element(locator)
        value_element_class = value_element.get_attribute('class')
        logger.info(f"value_element_class=====>>>>>{value_element_class} ")
        active_button_state = value_element_class.find("active-background")
        if active_button_state == -1:
            return False
        else:
            return True

    def get_text(self, locator):
        """
        Returns the text of the given web locator
        :param locator: desired locator for getting text
        :return: text of the web locator
        """

        return get_text(self._driver, locator)

    def get_user_input_text(self, edit_field_locator):
        """
        This returns the text entered by the user in the text box
        :param edit_field_locator: locators of the edit field
        :return: input_text
        """
        edit_field = self.get_element(edit_field_locator)
        input_text = edit_field.get_attribute("ng-reflect-value")
        return input_text

    def get_subtitle_text(self, edit_field_locator):
        """
        This returns the text entered by the user in the text box
        :param edit_field_locator: locators of the edit field
        :return: input_text
        """
        edit_field = self.get_element(edit_field_locator)
        input_text = edit_field.get_attribute("ng-reflect-subtitle")
        return input_text

    def get_comments_text(self, locator):
        """
        This returns the text entered in the comment section
        :param locator:
        :return: The text entered in the comment section
        """
        comments_section_element = self.get_element(locator)
        comments_section_text = comments_section_element.get_attribute("ng-reflect-model")
        return comments_section_text

    def contains_text(self, locator, subtext):
        """
        Returns whether the subtext can be found in the locator text
        ex: Finding 'Prime' within 'Prime Set to 10m'
        :param locator:
        :param subtext:
        :return: Boolean
        """
        selected_element = self.get_element(locator)
        selected_element_text = selected_element.get_attribute("innerText")
        selected_element_subtext = selected_element_text.find(subtext)

        if selected_element_subtext != -1:
            return True
        return False

    def get_text_from_list(self, locator):
        links = []
        no_of_elements = self.find_elements(locator)

        for element in no_of_elements:
            time.sleep(1)  # This is required for the scroll action
            element_text = element.find_element_by_tag_name('span')
            text = element_text.text
            logger.info(f"text ==={text}")
            links.append(text)
        return links

    def get_text_from_table(self, locator):
        links = []
        no_of_elements = self.find_elements(locator)

        for element in no_of_elements:
            element_text = element.find_element_by_tag_name('div')
            text = element_text.text
            logger.info(f"text ==={text}")
            links.append(text)
        return links

    def get_title_icon_color_code(self, locator, property_name):
        """
        This function gets the color code of the title icon in any condition card
        @return:get_title_icon_color_code
        """
        title_icon_status = self.get_element(locator)
        get_title_icon_color_code = title_icon_status.value_of_css_property(property_name)
        return get_title_icon_color_code

    def get_element_background_color(self, element):
        """
        This function gets the background color of the given element
        @return: element_background_color | ex: hexcode values #FFF/#FFFFFF
        """
        return self.get_element(element).value_of_css_property("background-color")

    def is_edit_field_exists(self, edit_field_locator):
        """
        This function verify thetest put field exists in a particular screen
        @return: Bool
        """
        is_edit_field_exists = True
        try:
            is_edit_field_exists = self.is_displayed(edit_field_locator)
        except Exception as generic_exception:
            traceback.print_exception(type(generic_exception), generic_exception, generic_exception.__traceback__)
            logger.error(f"Caught exception while checking number pad existence")
        return is_edit_field_exists

    def is_edit_field_in_error_state(self, edit_field_state_locator):
        """
        This function returns True, when the edit field is red indicating an error state
        and returns False, when the edit field is blue indicating an error free state

        :param edit_field_state_locator: The locator in the edit field which shows the state
        :return: bool
        """
        flow_rate_edit_field_state_element = self.get_element(edit_field_state_locator)
        edit_field_state = flow_rate_edit_field_state_element.get_attribute("ng-reflect-ng-class")
        edit_field_state = edit_field_state.find('error')
        if edit_field_state != -1:
            return True
        return False

    def is_selected(self, locator):
        """
        Returns whether the locator is selected
        Can be used to check if a checkbox or radio button is selected.
        :param locator:
        :return: Boolean
        """
        return WebElementsHandler.is_selected(self._driver, locator)

    def is_displayed(self, locator):
        """
        Returns whether the locator locator is visible to user
        :param locator:
        :return: Boolean
        """
        return is_displayed(self._driver, locator)

    def is_enabled(self, locator):
        """
        Returns whether the locator is enabled to user
        :param locator:
        :return: Boolean
        """
        return WebElementsHandler.is_enabled(self._driver, locator)

    def is_active(self, locator):
        """
        Returns whether the locator is in an active state
        ex: a toggle button that is selected
        :param locator:
        :return: Boolean
        """
        active_element = self.get_element(locator)
        active_element_state = active_element.get_attribute("class")
        active_element_state = active_element_state.find("active")

        if active_element_state != -1:
            return True
        return False

    def is_option_selected(self, locator):
        active_element = self.get_element(locator)
        active_element_state_element = active_element.get_attribute("class")
        active_element_state = active_element_state_element.find("selected")
        logger.debug(f"The active_element_state==>>{active_element_state_element} ")

        if active_element_state != -1:
            return True
        return False

    def is_option_element_selected(self, element):
        active_element_state = element.get_attribute("class")
        active_element_state = active_element_state.find("selected")

        if active_element_state != -1:
            return True
        return False

    def is_checkbox_checked(self, element):
        """
        This function returns whether the checkbox of the given locator is checked or not
        @return: check_state T/F
        """
        checkbox = self.get_element(element)
        check_state = checkbox.get_attribute("ng-reflect-checked")
        check_state = check_state.find("true")

        if check_state == -1:
            return False
        return True

    def verify_qrcode_link(self, locator, expected_qrcode_link):
        qrcode_container = self.get_element(locator)
        ng_reflect_qrdata = qrcode_container.get_attribute("ng-reflect-qrdata")
        logger.debug(f" QR Data==>{ng_reflect_qrdata}")
        assert ng_reflect_qrdata == expected_qrcode_link, "The qrcode value does not match the expected value"

        return ng_reflect_qrdata

    def is_button_inactive(self, button_locator):
        """
        This function returns whether the button of the given locator is inactive or not
        @return: get_title_icon_status

        """
        active_button_element = self.get_element(button_locator)
        active_button_state = active_button_element.get_attribute("class")
        active_button_state = active_button_state.find("avai")

        if active_button_state == -1:
            return True
        return False

    def validate_button_inactive_state(self, button_locator):
        """
        This function validates that a button is not able to be clicked/interacted with
        @param button_locator:
        @return: assertion of button being inactive
        """
        active_button_element = self.get_element(button_locator)
        active_button_state = active_button_element.get_attribute("class")
        active_button_state = active_button_state.find("avai")
        assert active_button_state == -1, f"The {button_locator} is not inactive"

    def is_button_available(self, button_locator):
        """
        This function validates that a button is not able to be clicked/interacted with
        @param button_locator:
        @return: assertion of button being inactive
        """
        active_button_element = self.get_element(button_locator)
        active_button_state = active_button_element.get_attribute("class")
        active_button_state = active_button_state.find("avai")
        assert active_button_state != -1, f"The {button_locator} is available"

    def is_toggle_component_enabled(self, locator):
        """
        This function returns the current status of the toggle component
        @param locator: locator of the component's toggle button
        @return: Boolean
        """
        toggle_button = self.get_element(locator)
        is_toggle_button_on = toggle_button.get_attribute("ng-reflect-checked-toggle")
        logger.debug(f" The attribute of the toggle button==>{is_toggle_button_on}")
        is_toggle_button_on = TypeConverter.to_bool(is_toggle_button_on)
        return is_toggle_button_on

    def is_toggle_button_enabled(self, locator):
        logger.info(f"Inside the tap@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ toggle button")
        toggle_button = self.get_element(locator)
        is_toggle_button_state = toggle_button.get_attribute("class")
        logger.info(f" The attribute of the toggle button==>{is_toggle_button_state}")

        get_check_box_state = is_toggle_button_state.find("checked")
        # value not found -1
        if get_check_box_state != -1:
            return True
        return False

    def tap_toggle_button_on(self, locator):
        is_toggle_button_turn_on = self.is_toggle_button_enabled(locator)
        logger.info(f"is_toggle_button_turn_on=={is_toggle_button_turn_on}")

        if not is_toggle_button_turn_on:
            time.sleep(1)
            logger.debug("*** Toggle button is not enabled")
            self.tap(locator)

        else:
            logger.debug("*** Toggle button is enabled")
            time.sleep(1)
        assert self.is_toggle_button_enabled(locator), 'Toggle button is switched off'

    def tap_toggle_button_off(self, locator):
        is_toggle_button_turn_on = self.is_toggle_button_enabled(locator)

        if is_toggle_button_turn_on:
            logger.debug("*** Toggle button is not enabled")
            self.tap(locator)

        else:
            logger.debug("*** Toggle button is enabled")
            time.sleep(1)
        assert not self.is_toggle_button_enabled(locator), 'Toggle button is switched off'

    def is_disabled(self, locator):
        disabled_element = self.get_element(locator)
        element_state = disabled_element.get_attribute("ng-reflect-disabled")
        logger.debug(f"element_state===>>>>{element_state}")

        if element_state == "false":
            return False
        return True

    def validate_unchecked_solvent_line(self, solvent_line, solvent_dict):

        for solvents_line in solvent_dict:
            if solvents_line != solvent_line:
                locator = solvent_dict[solvent_line]
                logger.debug(
                    f"The solvent line {solvents_line} selected is {self.is_radio_button_selected(locator)}")
                assert self.is_radio_button_selected(locator) is False

    """#######################
    ##### TOUCH ACTIONS ########
    #######################"""

    def tap(self, locator):
        """
        Taps on a given locator.
        :param locator:
        :return: void
        """
        TouchActionsHandler.tap(self._driver, locator)

    def tap_spinner_component_options(self, target_element):
        """
        Taps on a given locator.
        :param target_element:
        :return: void
        """
        TouchActionsHandler.tap_spinner_component_options(self._driver, target_element)

    def double_tap(self, locator):
        """
        Double taps the locator
        :param on locator:
        :return:
        """
        self._driver.find_element(*locator).double_tap()

    def tap_delete_button(self, no_of_times):
        """
        Tap delete button for a given number of times.
        :param no_of_times:
        :return: void
        """
        index = 0
        locator = BasePageLocators.NUM_PAD_DELETE_BUTTON
        while index < no_of_times:
            time.sleep(.1)
            TouchActionsHandler.tap_text_field(self._driver, locator)
            index += 1

    def tap_done_button(self):
        """
        Taps on the done button in any page of the kiosk application
        :return:
        """
        self.tap(BasePageLocators.DONE_BUTTON)

    def tap_cancel_button(self):
        """
        Taps on the cancel button in any page of the kiosk application
        :return:
        """
        self.tap(BasePageLocators.CANCEL_BUTTON)

    def tap_stop_button(self):
        """
        Taps on the cancel button in any page of the kiosk application
        :return:
        """
        self.tap(BasePageLocators.STOP_BUTTON)

    # tap_stop_button
    def tap_back_button(self):
        """
        Taps on the back button in any page of the kiosk application
        :return:
        """
        self.tap(BasePageLocators.BACK_BUTTON)

    def tap_for_dictionary_value(self, text_key, text_dictionary, assert_message):
        """
        This function selects the text in the given dictionary and taps on the locator corresponding to
        the selected text
        @param text_key:
        @param text_dictionary:
        @param assert_message:
        """

        if text_key in text_dictionary:
            locator = text_dictionary[text_key]
            self.tap_text_field(locator)
        else:
            assert False, f"{assert_message} => {text_key}"

    def long_press(self, locator):
        TouchActionsHandler.long_press(self._driver, locator)

    def tap_and_hold(self, xcord, ycord):
        """
        This function taps and holds on a given point via x and y value
        @param xcord:
        @param ycord:
        @return: void
        """

        TouchActionsHandler.tap_and_hold(self._driver, xcord, ycord)

    def release(self, xcord, ycord):
        """
        This function releases a held tap on a given point via x and y value
        This should be used in conjunction with tap_and_hold()
        @param xcord:
        @param ycord:
        @return: void
        """
        TouchActionsHandler.release(self._driver, xcord, ycord)

    def scroll_from_element(self, locator, xoffset, yoffset):
        """
       Touch and scroll starting at on_element, moving by xoffset and yoffset.
        :param locator: The element where scroll starts.
        :param xoffset: X offset to scroll to.
        :param yoffset: Y offset to scroll to.
        :return:

        """
        TouchActionsHandler.scroll_from_element(self._driver, locator, xoffset, yoffset)

    def scroll(self, xcord, ycord):
        """
        This function releases a held tap on a given point via x and y value
        This should be used in conjunction with tap_and_hold()
        @param xcord:
        @param ycord:
        @return: void
        """

        TouchActionsHandler.scroll(self._driver, xcord, ycord)

    def scroll_to_view(self, locator):
        """
        This function scroll to view the element of the locator
        :param locator: Locator of the element that need to be viewed and selected
        :return: Void
        """

        element = self.get_element(locator)
        self._driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        self.tap(locator)

    def scroll_to_element(self, locator):
        """
        This function scroll to view the element of the locator
        :param locator: Locator of the element that need to be viewed and selected
        :return: Void
        """

        element = self.get_element(locator)
        self._driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def scroll_to_view_element(self, element):
        """
        This function scroll to view the element of the locator
        :param element: Locator of the element that need to be viewed and selected
        :return: Void
        """

        self._driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        self.tap_spinner_component_options(element)

    def tap_text_field(self, locator):
        """
        Taps on a given text input field. This function should be used when the user wants to tap on the text
        :param locator:
        :return: void
        """
        TouchActionsHandler.tap_text_field(self._driver, locator)

    """#######################
    ##### KIOSK METHODS ########
    #######################"""

    # ##### KIOSK FUNCTIONAL

    def enter_value_for_specific_module(self, text_field_locators, value):
        """
        This function sets any given value in any given text field
        @param text_field_locators: locators of the text field
        @param value: Any Value
        @return:

        """
        self.clear_num_pad_entries(text_field_locators)
        self.enter_value(value)
        logger.debug(f" &&&&&&& After entering the solvent composition")

    def set_time_stepper(self, stepper_locator, unit_value, desired_value):
        """
        This method is to handle the time stepper component to get it to a given/desired value
        NOTE: Currently only works for time steppers using the 30sec unit 0/0/21
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param unit_value: the value of the stepper buttons ex: 30sec, 15sec
        @param desired_value: the desired time value ex: 05:30
        @return: void
        """
        InputStepperHandler(self._driver).set_time_stepper(stepper_locator, unit_value, desired_value)

    def set_numeric_stepper(self, stepper_locator, desired_value):
        """
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param desired_value: the desired numeric value ex: 25
        @return: void
        """
        InputStepperHandler(self._driver).set_numeric_stepper(stepper_locator, desired_value)

    # TODO: Create the input stepper method for the float variant of the component. Currently not implemented in the KIOSK 9/27/21
    def set_float_stepper(self):
        InputStepperHandler(self._driver).set_float_stepper()

    def stepper_increment(self, stepper_locator, tap_amount):
        """
        This method taps on the stepper component's increment button to increase value
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param tap_amount: numerical value that determines the tap() execution times
        @return: void
        """
        InputStepperHandler(self._driver).stepper_increment(stepper_locator, tap_amount)

    def stepper_decrement(self, stepper_locator, tap_amount):
        """
        This method taps on the stepper component's decrement button to decrease value
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param tap_amount: numerical value that determines the tap() execution times
        @return: void
        """
        InputStepperHandler(self._driver).stepper_decrement(stepper_locator, tap_amount)

    def stepper_reset(self, stepper_locator):
        """
        This method taps on the stepper component's reset button to default value
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @return: void
        """
        InputStepperHandler(self._driver).stepper_reset(stepper_locator)

    def scroll_to_spinner_options(self, option, date_format_style_dictionary):
        """
        This function can be used to scroll and view any option in the spinner/wheel component
        :param option: The visible text in the spinner component
        :param date_format_style_dictionary: locator lookup dictionary of the spinner component
        :return: Void
        """

        if option in date_format_style_dictionary:
            locator = date_format_style_dictionary[option]
            self.scroll_to_view(locator)
            # There is a transition animation on the selection wheel when choosing a new option
            time.sleep(2)
            self.tap(locator)
            return

        assert False, f"Unexpected screen saver style => {option}"

    def select_spinner_options(self, option, option_dictionary):
        """
        This function can be used to select any option in the spinner/wheel component
        :param option: The visible text in the spinner component
        :param option_dictionary: locator lookup dictionary of the spinner component
        :return: Void
        """

        if option in option_dictionary:
            locator = option_dictionary[option]
            self.tap(locator)
            # There is a transition animation on the selection wheel when choosing a new option
            time.sleep(1)
            return

        assert False, f"Unexpected screen saver style => {option}"

    def set_spinner_value(self, spinner_locator, desired_value):
        """
        This method takes in a desired value and selects that value within a spinner/picker component
        :param spinner_locator: xpath locator for the spinner/picker list. This must be an ics-picker-base, and a ul element within that base
        example: //ics-picker-base[@ng-reflect-id='ispp-id-instrument-startup-sam']//div//div//div[1]//ul
        :param desired_value: the value to be selected. this should match the format of what is within the spinner/picker list
        example: 25.0 or 10
        :return: void
        """

        PickerSpinnerHandler(self._driver).set_spinner_value(spinner_locator, desired_value)

    def select_spinner_text(self, spinner_locator, desired_value):
        """
        This method takes in a desired value and selects that value within a spinner/picker component
        :param spinner_locator: xpath locator for the spinner/picker list. This must be an ics-picker-base, and a ul element within that base
        example: //ics-picker-base[@ng-reflect-id='ispp-id-instrument-startup-sam']//div//div//div[1]//ul
        :param desired_value: the value to be selected. this should match the format of what is within the spinner/picker list
        example: Any text
        :return: void
        """

        PickerSpinnerHandler(self._driver).select_spinner_text(spinner_locator, desired_value)

    def select_spinner_text_for_plots(self, spinner_locator, desired_value):
        PickerSpinnerHandler(self._driver).select_spinner_text_plots(spinner_locator, desired_value)

    # ##### KIOSK VALIDATION

    def is_numpad_exists(self):
        """
        This function verify the numpad exists in a particular screen
        @return: Bool
        """
        number_pad_exists = True
        try:
            number_pad_exists = self.is_displayed(BasePageLocators.NUM_PAD_1_BUTTON)
        except Exception as generic_exception:
            traceback.print_exception(type(generic_exception), generic_exception, generic_exception.__traceback__)
            logger.error(f"Caught exception while checking number pad existence")
        return number_pad_exists

    def is_numpad_active(self):
        """
        This function verifies if the numpad is active
        @return:
        """
        numpad_container = self.get_element(BasePageLocators.NUM_PAD_CONTAINER)
        numpad_class = numpad_container.get_attribute("class")
        numpad_active_state = numpad_class.find("inactive")

        if numpad_active_state != -1:
            return False
        return True

    def get_condition_card_value(self, before_decimal_value_locator, after_decimal_value_locator):
        """
        This method get number value and unit type of the any condition card depending upon the locator provided
        :param after_decimal_value_locator: locator of the value after the decimal point
        :param before_decimal_value_locator: locator of the value before the decimal point
        :return: readback value in the condition card
        """

        before_decimal_value_locator = self.get_container_text(before_decimal_value_locator)
        after_decimal_value_locator = self.get_container_text(after_decimal_value_locator)
        logger.debug(f"before_decimal_value_locator===>>>>>  {before_decimal_value_locator}")
        logger.debug(f"after_decimal_value_locator===>>>>>  {after_decimal_value_locator}")

        whole_value = TypeConverter.to_str(before_decimal_value_locator) + TypeConverter.to_str(
            after_decimal_value_locator)
        return whole_value

    def get_title_icon_status(self, locator):
        """
        This function gets the status of title icon in the any condition card.
        @return: get_title_icon_status
        """
        title_icon_status = self.get_element(locator)
        get_title_icon_status = title_icon_status.get_attribute("ng-reflect-svg-icon")
        return get_title_icon_status

    def get_current_flow_rate(self, value_locator):
        """
        This function returns the flow rate  in any screen
        :param value_locator:
        :return: flow_rate_value
        """
        flow_rate_read_back_element = self.get_element(value_locator)
        flow_rate_value = flow_rate_read_back_element.get_attribute("ng-reflect-value")
        return flow_rate_value

    def get_current_flow_unit(self, unit_locator):
        """
        This function returns the flow unitrate read back message in any screen
        :param unit_locator:
        :return: flow_rate_units
        """

        flow_rate_units = self.get_container_text(unit_locator)
        return flow_rate_units

    def is_radio_button_selected(self, button_locator):
        """
        This function returns true if the radio button is selected
        :param button_locator:
        :return:
        """

        active_button_element = self.get_element(button_locator)
        active_button_state = active_button_element.get_attribute("class")
        active_button_state = active_button_state.find("radio-checked")

        if active_button_state == -1:
            return False
        return True

    def is_default_value_button_disabled(self, default_button_locator):
        """
            This function returns true if any set default button is disabled
            :param default_button_locator:
            :return: bool
            """

        active_button_element = self.get_element(default_button_locator)
        active_button_state = active_button_element.get_attribute("class")
        active_button_state = active_button_state.find("disabled")

        if active_button_state == -1:
            return False
        return True

    def get_solvent_composition(self, composition_locator):
        solvent_composition_read_back_element = self.get_element(composition_locator)
        solvent_composition_read_back_element("")

    def get_temperature(self, before_decimal_temperature_locator, after_decimal_temperature_locator):
        """
        This function gets the temperature of the column manager in any screen of the Kiosk application
        depending upon the locator provided
        :param before_decimal_temperature_locator: locator of the temperature before the decimal
        :param after_decimal_temperature_locator: locator of the temperature after the decimal
        :return: The temperature displayed in the screen
        """
        temperature_before_decimal = self.get_container_text(before_decimal_temperature_locator)
        temperature_after_decimal = self.get_container_text(after_decimal_temperature_locator)
        if temperature_before_decimal is None or temperature_after_decimal is None:
            return None
        temperature_string = str(temperature_before_decimal) + str(temperature_after_decimal)
        logger.debug(f"current_temperature_string ==========={temperature_string}")
        return temperature_string

    def get_temperature_units(self, temperature_unit_locator):
        """
        This function gets the temperature units of the column manager in any screen of the Kiosk application
        depending upon the locator provided
        :param temperature_unit_locator: locator of the temperature units
        :return: column temperature unit
        """
        logger.debug(f"temperature_unit_locator ==========={temperature_unit_locator}")
        column_temperature_units_readback_message = self.get_container_text(temperature_unit_locator)
        column_temperature_units_readback_message = column_temperature_units_readback_message.strip()
        return column_temperature_units_readback_message

    def get_units(self, unit_locator):
        """
        This function gets the temperature units of the column manager in any screen of the Kiosk application
        depending upon the locator provided
        :param unit_locator: locator of the temperature units
        :return: column temperature unit
        """
        units_readback_message = self.get_container_text(unit_locator)
        readback_message = units_readback_message.strip()
        return readback_message

    def get_system_pressure(self, pressure_whole_number, pressure_decimal_number):
        """
            This method the number values of the system pressure in any screen of the Kiosk application
            depending upon the locator provided
            :param pressure_whole_number: Locator for the number before the decimal point, and the decimal pont itself
            :param pressure_decimal_number: Locator for the number after the decimal point
            :return: The system pressure, both values together | ex: 17.5
            """
        # get the pressure value
        whole_number_pressure_value = self.get_container_text(pressure_whole_number)
        decimal_pressure_value = self.get_container_text(pressure_decimal_number)

        pressure_value = TypeConverter.to_str(whole_number_pressure_value) + TypeConverter.to_str(
            decimal_pressure_value)

        system_pressure = TypeConverter.to_float(pressure_value)

        return system_pressure

    def select_and_validate_spinner_range(self, spinner_option_range, option_locator, expected_text_locator):
        """
        This function is to validate when there is a spinner component and when user selects an option in the spinner component
        and the corresponding option selects is displayed anywhere in the same screen.
        @param spinner_option_range: The range of the options in the spinner component that needs to be validates
        @param option_locator: locator of the options in the spinner component
        @param expected_text_locator: locator of the label which displays the selected option in the spinner component
        @return: Void
        """

        for x in spinner_option_range:
            picker_locator = (By.XPATH, f"{option_locator}li[{x}]")
            logger.debug(f"The list of locators ===>>>{picker_locator}")
            self.wait_for_element_visibility(5, picker_locator)
            self.tap(picker_locator)
            time.sleep(1)
            assert self.is_option_selected(picker_locator), f"The {picker_locator} is not selected"
            actual_text = self.get_text(picker_locator)
            time.sleep(1)
            expected_text = self.get_text(expected_text_locator)
            self.validate_text(actual_text, expected_text)

    def validate_text(self, actual_text, expected_text):
        """
        Function is to validate any text in the screen
        @param actual_text:
        @param expected_text:
        @return:
        """
        actual_text = str(actual_text)
        actual_text = actual_text.strip()
        expected_text = str(expected_text)
        expected_text = expected_text.strip()
        logger.debug(f"The actual text  ===>{actual_text}")
        logger.debug(f"The expected text  ===>{expected_text}")
        assert actual_text == expected_text, f" The actualtext is ==>> {actual_text}"

    def is_scroll_window_exists(self, scroll_window_locator):
        """
        This function verify the existence of a scroll window in a particular screen
        @return: Bool
        """
        is_scroll_window_exists = True
        try:
            is_scroll_window_exists = self.is_displayed(scroll_window_locator)
        except Exception as generic_exception:
            traceback.print_exception(type(generic_exception), generic_exception, generic_exception.__traceback__)
            logger.error(f"Caught exception while checking number pad existence")
        return is_scroll_window_exists

    def validate_done_button_inactive(self):
        """
        This function verifies if the numpad is active
        @return:
        """
        numpad_container = self.get_element(BasePageLocators.DONE_BUTTON)
        is_done_button_inactive = numpad_container.get_attribute("ng-reflect-available")
        logger.debug(f"is_done_button_inactive==>>>{is_done_button_inactive}")
        is_done_button_inactive = TypeConverter.to_bool(is_done_button_inactive)

        assert is_done_button_inactive is False

    def select_check_box(self, locator):
        """
        This function selects the checkbox
        :param locator: checkbox component
        :return: Void
        """
        current_check_box_state = self.is_check_box_selected(locator)

        if current_check_box_state:
            logger.debug("The check box is already selected")
        else:
            self.tap(locator)

    def deselect_check_box(self, locator):
        """
        This function selects the checkbox
        :param locator: checkbox component
        :return: Void
        """
        current_check_box_state = self.is_check_box_selected(locator)

        if current_check_box_state:
            self.tap(locator)

        else:
            logger.debug("The check box is already selected")

    def is_check_box_selected(self, locator):
        """
        This function returns true , if the check box is selected and return
        False if the checkbox is not selected
        :param locator: check box
        :return: Void
        """

        check_box_element = self.get_element(locator)
        check_box_state = check_box_element.get_attribute("class")
        logger.debug(f" The state of check box {check_box_state}")
        get_check_box_state = check_box_state.find("checked")
        if get_check_box_state == -1:
            return False
        else:
            return True

    def is_flow_on(self, locator):
        """
        This function returns true when there is a flow simulation (like marching ants) seen in the schemation icon
        :param locator: locator of the flow path component
        :return: Bool
        """
        schematic_icon_element = self.get_element(locator)
        schematic_icon_flow_state = schematic_icon_element.get_attribute("ng-reflect-flow-state")
        schematic_icon_flow_state = TypeConverter.to_bool(schematic_icon_flow_state)
        if schematic_icon_flow_state:
            return True
        else:
            return False

    def is_condition_met(self, locator):

        """
        This function is to validate any conditions like" lamp is ON", "The door is close" etc is met or not
        :param locator: loactor of the check box, which will be selected if the condiion is met
        :return: Bool
        """
        condition_state_element = self.get_element(locator)
        edit_field_state = condition_state_element.get_attribute("data-mat-icon-name")
        edit_field_state = edit_field_state.find('ready')
        return edit_field_state != -1

    def wait_time_to_load_value(self, locator, ignore_message="--"):
        """
        This function waits for the value/text to be loading on the screen corresponding to the given locator
        :param ignore_message: message to be ignored
        :param locator: locator of the value/text that needs to be fully loaded
        :return: Value/text of the locator
        """

        time_ignore_initial_message = 300
        start_time = time.time()
        action_text = None
        while time.time() - start_time < time_ignore_initial_message:
            action_text = self.get_container_text(locator)
            logger.debug(f" action_text ===> {action_text}")
            logger.debug(f" ignore_message ===> {ignore_message}")

            if action_text != ignore_message:
                logger.debug(f"Locator [{locator}] text was [{action_text}]")
                break
        return action_text

    def wait_till_element_is_invisible(self, locator, second_to_wait):
        """
        This function waits for the given locator to go invisible
        :param locator: locator of the value/text that needs to go invisible
        :param second_to_wait: time to wait for the action to be performed
        :return: void
        """
        try:
            wait = WebDriverWait(self._driver, second_to_wait)
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            assert False, f" The wait for element to be invisible action on locator {locator} is not complete in enough time {second_to_wait} at basepage" \
                          f"::wait_till_element_is_invisible "

    def wait_till_condition_met(self, locator, expected_condition, error_message, wait_time):
        """
        This function wait until the tex/value of the given locator matches the expected condition
        :param locator: Text or value of the locator
        :param expected_condition: expected condition that should be met
        :param error_message: error message display in case of condition not met
        :param wait_time: Duration to wait for
        :return: bool
        """

        start_time = time.time()
        transition_action_text = None
        while time.time() - start_time < wait_time:
            logger.debug("The timer starts now")
            transition_action_text = self.get_container_text(locator)
            logger.debug(f"transition_action_text====>>>>>>{transition_action_text}")
            logger.debug(f"expected_condition====>>>>>>{expected_condition}")
            if transition_action_text == expected_condition:
                break
            time.sleep(1)
        assert transition_action_text == expected_condition, f"{error_message} transition_action_text= {transition_action_text}"

    def tap_and_hold_at_specific_point(self, locator):
        """
        This function gets the coordinates of the given locator and perform tap and hold functionality
        :param locator: locator of the point where the tap and hold should be performed
        :return: VOid
        """
        button_element = self.get_element(locator)
        location = button_element.location
        logger.debug(f" the coordinates of the command button are {location}")
        location_dict = location
        xcord = location_dict["x"]
        ycord = location_dict["y"]
        self.tap_and_hold(xcord, ycord)

    def validate_hint_message(self, locator, expected_hint_message):
        actual_hint_message = self.get_text(locator)
        logger.debug(f"actual_hint_message====>>>>{actual_hint_message}")
        logger.debug(f"expected_hint_message====>>>>{expected_hint_message}")
        assert actual_hint_message == expected_hint_message, \
            f"actual_hint_message====>>>>{actual_hint_message}, expected_hint_message====>>>>{expected_hint_message}"

    def validate_condition(self, actual_condition, expected_condition, error_message, wait_time):
        """
        This function wait until the tex/value of the given locator matches the expected condition
        :param actual_condition: Text or value for actual condition
        :param expected_condition: expected condition that should be met
        :param error_message: error message display in case of condition not met
        :param wait_time: Duration to wait for
        :return: bool
        """

        start_time = time.time()
        while time.time() - start_time < wait_time:
            logger.info("The timer starts now")
            logger.info(f"transition_action_text====>>>>>>{actual_condition}")
            logger.info(f"expected_condition====>>>>>>{expected_condition}")
            if actual_condition == expected_condition:
                break
            time.sleep(1)
        assert actual_condition == expected_condition, f"{error_message} transition_action_text= {actual_condition}"

    def validate_idle_state(self):
        """
        This function validates that the system is in idle condition
        """
        self.validate_simple_text_wait_condition(
            DashBoardsScreenPageLocators.SYSTEM_STATE,
            SystemStateConstants.IdleSystemState, SystemStateConstants.MaxiTimeToIdle)

    def wait_for_busy_state(self):
        """
        This function runs until the system is in busy condition
        """
        try:
            self.validate_simple_text_wait_condition(
                DashBoardsScreenPageLocators.SYSTEM_STATE,
                SystemStateConstants.BusySystemState, self.wait_time)
        except AssertionError as e:
            logger.info(e)

    def validate_abort_status_screen(self):
        """
        This function validates any workflow that is aborted, if not catches the exception and fails the test and navigates from the workflow terminated screen
        """
        self.validate_simple_text_wait_condition(
            BasePageLocators.RESULTS_HEADER,
            SystemStateConstants.StoppedValidateText, SystemStateConstants.MaxiTimeToAbort)

        try:
            start_time = time.time()
            while time.time() - start_time < SystemStateConstants.MaxiTimeToAbort:
                button_state = self.is_button_inactive(
                    BasePageLocators.STOP_BUTTON_STATE)
                logger.info(f"button_state===>>>{button_state}")
                time.sleep(1)  # TODO Remove it later after alliance 1.1 and find a solution to avoid sleep time

                if button_state is False:
                    read_back_message = self.get_text(BasePageLocators.WORKFLOW_DISPLAY_MESSAGE)
                    expected_message = WorkflowCommonConstant.WorkflowCompleteMessageAfterAbort
                    logger.info(f"read_back_message===>>>======{read_back_message}=======")
                    logger.info(f"expected_message===>>>======{expected_message}=======")
                    assert read_back_message == expected_message

                    self.tap_close_button()

                    break
                time.sleep(1)

        except Exception as e:
            logger.info(f"exception caught===>>>{e}")
            self.validate_workflow_interrupted_screen()
            self.tap_close_button()
            assert False, f"The workflow does not abort successfully"

        finally:
            self.set_idle_state()

    def validate_workflow_interrupted_screen(self):
        """
        This function validate the screen when workflow interrupts due to system error
        induced during abort process
        """
        read_back_message = self.get_text(BasePageLocators.WORKFLOW_DISPLAY_MESSAGE)
        logger.info(f"validate_workflow_interrupted_screen read_back_message===>>>======{read_back_message}=======")

        expected_message = WorkflowCommonConstant.WorkflowInterruptedMessageDuringAbort
        logger.info(f"validate_workflow_interrupted_screen expected_message===>>>======{expected_message}=======")
        assert read_back_message == expected_message, f"Failed to display workflow interrupted screen"

    def set_idle_state(self):
        """
        This function fix the system state to idle state , if the system is in the error state

        """

        current_system_state = self.get_text(DashBoardsScreenPageLocators.SYSTEM_CURRENT_STATE)
        logger.info(f"current_system_state==={current_system_state}=======")
        if current_system_state == SystemStateConstants.ErrorSystemState:
            self.tap(DashBoardsScreenPageLocators.COMMANDS)
            self.tap(CommandsScreenPageLocators.RESET_SYSTEM)
        logger.info(f"current_system_state===>>>======{current_system_state}=======")
        self.validate_idle_state()

    def tap_next_button(self):
        """
        This is the common method for tapping next button anywhere in the kiosk app
        """
        start_time = time.time()
        while time.time() - start_time < 30:
            current_button_state = self.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)
            if current_button_state:
                self.tap(BasePageLocators.NEXT_BUTTON)
                break
            time.sleep(1)

    def tap_close_button(self):
        start_time = time.time()
        while time.time() - start_time < 30:
            current_button_state = self.is_button_active(BasePageLocators.CLOSE_BUTTON)
            if current_button_state:
                self.tap(BasePageLocators.CLOSE_BUTTON)
                break
            time.sleep(1)

    def tap_start_button(self):
        start_time = time.time()
        while time.time() - start_time < 30:
            current_button_state = self.is_button_active(BasePageLocators.START_BUTTON)
            if current_button_state:
                self.tap(BasePageLocators.CLOSE_BUTTON)
                break
            time.sleep(1)

    def is_button_active(self, locator):
        """
        This function verifies if the button is active
        @return:bool
        """
        numpad_container = self.get_element(locator)
        is_button_active = numpad_container.get_attribute("ng-reflect-available")
        logger.info(f"is_done_button_inactive==>>>{is_button_active}")
        is_done_button_inactive = TypeConverter.to_bool(is_button_active)
        return is_done_button_inactive

    def is_button_selected(self, locator):
        """
        This function verifies if the button is selected
        @return:bool
        """
        numpad_container = self.get_element(locator)
        is_button_selected = numpad_container.get_attribute("ng-reflect-selected")
        verify_button_selected = TypeConverter.to_bool(is_button_selected)
        return verify_button_selected

    def is_result_shown(self, locator):
        """
        This function return  true if the result were shown in the result screen after the execution of
        any workflow
        """
        current_arrow = self.get_element(locator)
        current_arrow_state = current_arrow.get_attribute("ng-reflect-icon")
        logger.info(f"current_arrow_state===>{current_arrow_state}")
        if current_arrow_state == "ics-img-arrow-up":
            return True
        else:
            return False

    def validate_lamp_hours_state(self, locator, lamp_hours_used, total_lamp_hours):
        """This function validate the state of the progressbar/indicator depending upon the ratio between the 
            used lamp hours and total lamp hours. 
        """
        lamp_hours_used = TypeConverter.to_float(lamp_hours_used)
        total_lamp_hours = TypeConverter.to_float(total_lamp_hours)

        self.wait_for_element_load(locator, TUVConditionCardConstants.ProgressBarLoadTime)
        current_lamp_hours_state_element = self.get_element(locator)
        lamp_state_class = current_lamp_hours_state_element.get_attribute("class")

        if lamp_hours_used > total_lamp_hours:
            lamp_state = lamp_state_class.find("error")
            assert lamp_state != -1, "The progress bar is not showing error state"
        elif total_lamp_hours * 0.9 <= lamp_hours_used <= total_lamp_hours:
            lamp_state = lamp_state_class.find("warn")
            assert lamp_state != -1, "The progress bar is not showing warning state"
        else:
            lamp_state = lamp_state_class.find("ready")
            assert lamp_state != -1, "The progress bar is not showing ready state"

    def lamp_hours_separator(self, locator, string_separator):
        text_to_split = self.get_container_text(locator)
        text_split = text_to_split.split(string_separator)
        lamp_usage = text_split[0].strip()
        lamp_total = text_split[1].strip()
        lamp_total = lamp_total[:-6]
        lamp_values = [lamp_usage, lamp_total]
        return lamp_values

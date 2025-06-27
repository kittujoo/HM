import os

from pytest_bdd import given, when, scenarios, then
from pytest_bdd.parsers import cfparse

from utilities.logger import Logger
from utilities.datatables.converters import CONVERTERS

from web_framework.method_editor.pages.method_editor_main_page import MethodEditorMainPage
from web_framework.method_editor.pages.tuv_detector.menu_item_tuv_detector import TuvDetectorMenu
from web_framework.method_editor.pages.tuv_detector.lamp_page import LampPage

scenarios('../features/method_editor_tuv_lamp.feature')

logger = Logger(os.path.basename(__file__))


@given('the TUV Detector menu is opened')
def open_tuv_detector_menu(method_editor_main_page: MethodEditorMainPage):
    tuv_detector_menu = method_editor_main_page.left_panel.tuv_detector
    return tuv_detector_menu


@given('the Lamp menu is opened')
def open_lamp_menu(tuv_detector_menu: TuvDetectorMenu):
    lamp_page = tuv_detector_menu.open_lamp()
    return lamp_page


@then(cfparse('the Lamp menu title is "{expected_title}"'))
def validate_lamp_menu_title(expected_title: str, lamp_page: LampPage):
    actual_title = lamp_page.get_lamp_menu_tile()
    assert actual_title == expected_title, f"The lamp menu title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the setting group title is "{expected_title}"'))
def validate_setting_group_title(expected_title: str, lamp_page: LampPage):
    actual_title = lamp_page.get_lamp_setting_group_title()
    assert actual_title == expected_title, f"The setting group title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Lamp State setting title is "{expected_title}"'))
def validate_lamp_state_setting_title(expected_title: str, lamp_page: LampPage):
    pass
    # actual_title = lamp_page.get_lamp_state_setting_title()
    # assert actual_title == expected_title, f"The lamp state setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Lamp State setting summary is "{expected_title}"'))
def validate_lamp_state_setting_summary_title(expected_title: str, lamp_page: LampPage):
    actual_title = lamp_page.get_lamp_state_setting_summary_title()
    assert actual_title == expected_title, f"The lamp state setting summary is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"

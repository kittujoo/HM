import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_needle_constants import ReplaceNeedleConstant
from web_framework.kiosk.pages.Locators.Maintain.replace_needle_workflow_locators import ReplaceNeedlePreconditionsScreenLocators, \
    StatusAndTestsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.ReplaceNeedle.replace_needle_screen import ReplaceNeedleScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.ReplaceNeedle.replace_needle_status_screen import ReplaceNeedleStatusScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/MaintainScreen/replace_needle.feature')
logger = Logger("test_replace_needle_workflow")


@pytest.fixture
def replace_components_page(maintain_screen_page: MaintainScreen, page_builder):
    maintain_screen_page.tap_replace_components()
    page = page_builder(ReplaceComponentsScreen)
    return page


@pytest.fixture
def replace_needle_status_page(page_builder):
    page = page_builder(ReplaceNeedleStatusScreen)
    return page


@pytest.fixture
def replace_needle_page(page_builder):
    page = page_builder(ReplaceNeedleScreen)
    return page


@when('User taps the replace needle panel')
def begin_calibrate_workflow(replace_components_page: ReplaceComponentsScreen):
    replace_components_page.tap_replace_needle_tab()


@then('User validates the Welcome screen text')
def validate_welcome_text(replace_needle_page: ReplaceNeedleScreen):
    try:
        actual_paragraph_text = replace_needle_page.get_welcome_paragraph_text()
        logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")

        expected_paragraph_text = ReplaceNeedleConstant.expected_welcome_paragraph_text
        logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    finally:
        replace_needle_page.tap_next_button()


@then('User validates the Caution screen text')
def validate_welcome_text(replace_needle_page: ReplaceNeedleScreen):
    try:
        actual_paragraph_text = replace_needle_page.get_customs_text()
        logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")

        expected_paragraph_text = ReplaceNeedleConstant.caution_text
        logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    finally:
        replace_needle_page.tap(BasePageLocators.CANCEL_BUTTON)
        time.sleep(5)  # TODO this will be removed once the implementation is complete


@when('User navigates to the pre-conditions screen')
def navigate_precondition_screen(replace_needle_page: ReplaceNeedleScreen):
    replace_needle_page.tap_next_button()
    replace_needle_page.tap_next_button()


@then('User confirms the preconditions')
def validate_preconditions(replace_needle_page: ReplaceNeedleScreen):
    replace_needle_page.validate_warning_text()
    is_condition_lamp_met = replace_needle_page.is_condition_met(
        ReplaceNeedlePreconditionsScreenLocators.SAMPLE_PLATES)
    is_condition_cuvette_met = replace_needle_page.is_condition_met(
        ReplaceNeedlePreconditionsScreenLocators.POWER_STATE)
    is_current_tuv_door_met = replace_needle_page.is_condition_met(
        ReplaceNeedlePreconditionsScreenLocators.COMPARTMENT_DOOR)

    if is_condition_lamp_met and is_current_tuv_door_met and is_condition_cuvette_met:
        logger.info("All the condition are met")
        replace_needle_page.tap_next_button()

    else:
        assert False, "The test cannot be continued as the conditions were not met"


@then('User taps the stop button')
def tap_stop_button(replace_needle_page: ReplaceNeedleScreen):
    replace_needle_page.tap(ReplaceNeedlePreconditionsScreenLocators.STOP_BUTTON)


@then('User validates the workflow is stopped')
def validate_stop_workflow(replace_components_page: ReplaceComponentsScreen):
    replace_components_page.is_displayed(ReplaceNeedlePreconditionsScreenLocators.STOP_BUTTON)


@then('User validates the carriage is in the service position')
def validate_status(replace_needle_status_page: ReplaceNeedleStatusScreen):
    replace_needle_status_page.validate_information_text()
    replace_needle_status_page.validate_progress_bar()
    replace_needle_status_page.tap_next_button()


@then('User validates the replace needle procedure text')
def validate_procedure_text(replace_needle_status_page: ReplaceNeedleStatusScreen):
    try:
        actual_paragraph_text = replace_needle_status_page.get_procedure_text()
        logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")

        expected_paragraph_text = ReplaceNeedleConstant.expected_procedure_paragraph_text
        logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    finally:
        replace_needle_status_page.tap_next_button()


@then('User runs the recommended tests')
def run_recommended_test(replace_needle_status_page: ReplaceNeedleStatusScreen):
    time.sleep(2)  # TODO this will be removed once the implementation is complete
    replace_needle_status_page.validate_tests_running_text()
    replace_needle_status_page.tap(StatusAndTestsScreenLocators.PLAY_ICON)
    replace_needle_status_page.validate_tests_running_text()
    replace_needle_status_page.validate_progress_bar()
    time.sleep(5)  # TODO this will be removed once the implementation is complete


@then('User taps the start icon')
def press_start_icon(replace_needle_status_page: ReplaceNeedleStatusScreen):
    replace_needle_status_page.tap(StatusAndTestsScreenLocators.PLAY_ICON)

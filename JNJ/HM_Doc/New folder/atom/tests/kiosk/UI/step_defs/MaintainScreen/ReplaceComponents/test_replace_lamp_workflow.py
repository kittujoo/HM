import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_lamp_workflow_constants import ReplaceLampWorkflowConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_components_locators import ReplaceComponentsScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_lamp_workflow_locators import ReplaceLampWorkflowFinishLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.ReplaceLamp.replace_lamp_workflow_setup_screen import ReplaceLampWorkflowSetupScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/MaintainScreen/ReplaceComponents/replace_lamp_workflow.feature')

logger = Logger(__name__)


@pytest.fixture
def replace_lamp_setup_screen(page_builder):
    page = page_builder(ReplaceLampWorkflowSetupScreen)
    return page


@given('User navigates to the replace components HUB area')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen, maintain_screen: MaintainScreen):
    logger.info("The user profile settings screen test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_maintain()
    maintain_screen.tap(MaintainScreenPageLocators.REPLACE_PANEL)


@when('User taps the replace lamp panel')
def tap_replace_lamp_panel(replace_components_hub_screen: ReplaceComponentsScreen):
    replace_components_hub_screen.tap(ReplaceComponentsScreenPageLocators.REPLACE_LAMP)


@when('User validates the context in the welcome screen')
def validate_welcome_screen_information(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    replace_lamp_setup_screen.validate_welcome_screen()

    actual_paragraph_text = replace_lamp_setup_screen.get_welcome_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceLampWorkflowConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_lamp_setup_screen.tap_next_button()


@when('User validates the context in the caution screen')
def validate_caution_screen_information(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    replace_lamp_setup_screen.validate_cautions_screen()

    actual_paragraph_text = replace_lamp_setup_screen.get_caution_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceLampWorkflowConstants.expected_caution_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_lamp_setup_screen.tap_next_button()


@when('User validates the context and conditions in the preconditions screen')
def validate_preconditions_screen_information(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    replace_lamp_setup_screen.validate_cautions_screen()

    assert replace_lamp_setup_screen.validate_precondition_states(), f"One of the preconditions is not in check status"

    actual_paragraph_text = replace_lamp_setup_screen.get_preconditions_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceLampWorkflowConstants.expected_preconditions_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_lamp_setup_screen.tap_next_button()


@when('User validates the context in the removal screen')
def validate_removal_screen_information(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    replace_lamp_setup_screen.validate_removal_screen()

    actual_paragraph_text = replace_lamp_setup_screen.get_removal_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceLampWorkflowConstants.expected_removal_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_lamp_setup_screen.tap_next_button()


@when('User validates the context in the first installation screen')
def validate_first_installation_screen_information(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    replace_lamp_setup_screen.validate_first_installation_screen()

    actual_paragraph_text = replace_lamp_setup_screen.get_first_installation_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceLampWorkflowConstants.expected_first_installation_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_lamp_setup_screen.tap_next_button()


@when('User validates the context in the second installation screen')
def validate_second_installation_screen_information(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    replace_lamp_setup_screen.validate_second_installation_screen()

    actual_paragraph_text = replace_lamp_setup_screen.get_second_installation_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceLampWorkflowConstants.expected_second_installation_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_lamp_setup_screen.tap_next_button()


@then('User validates the lamp hours in the finalization screen')
def validate_lamp_hours(replace_lamp_setup_screen: ReplaceLampWorkflowSetupScreen):
    assert replace_lamp_setup_screen.validate_lamp_hours_range(), f"The lamp hours has exceeded the maximum allowed"
    replace_lamp_setup_screen.tap(ReplaceLampWorkflowFinishLocators.DONE_BUTTON)

import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_seal_workflow_constants import ReplaceSealWorkflowConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_components_locators import ReplaceComponentsScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_seal_workflow_locators import ReplaceSealWorkflowLocators, \
    ReplaceSealWorkflowCautionLocators, ReplaceSealWorkflowPreconditionsLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.ReplaceSeal.replace_seal_workflow_setup_screen import ReplaceSealWorkflowSetupScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../../UI/features/MaintainScreen/ReplaceComponents/replace_seal_workflow.feature')

logger = Logger(__name__)


@pytest.fixture
def replace_seal_setup_screen(page_builder):
    page = page_builder(ReplaceSealWorkflowSetupScreen)
    return page


@given('User navigates to the replace components HUB area')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen, maintain_screen: MaintainScreen):
    logger.info("The user profile settings screen test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_maintain()
    maintain_screen.tap(MaintainScreenPageLocators.REPLACE_PANEL)


@when('User taps the replace seal panel')
def tap_replace_lamp_panel(replace_components_hub_screen: ReplaceComponentsScreen):
    replace_components_hub_screen.tap(ReplaceComponentsScreenPageLocators.REPLACE_SEAL)


@when('User validates the context in the welcome screen')
def validate_welcome_screen_information(replace_seal_setup_screen: ReplaceSealWorkflowSetupScreen):
    replace_seal_setup_screen.validate_welcome_screen()

    actual_paragraph_text = replace_seal_setup_screen.get_welcome_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceSealWorkflowConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_seal_setup_screen.tap_next_button()


@when('User validates the context in the caution screen')
def validate_caution_screen_information(replace_seal_setup_screen: ReplaceSealWorkflowSetupScreen):
    replace_seal_setup_screen.validate_cautions_screen()

    actual_paragraph_text = replace_seal_setup_screen.get_text(ReplaceSealWorkflowCautionLocators.CAUTION_TEXT)
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceSealWorkflowConstants.CautionText
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_seal_setup_screen.tap_next_button()


@when('User validates the preconditions are in a passing state')
def validate_precondition_states(replace_seal_setup_screen: ReplaceSealWorkflowSetupScreen):
    replace_seal_setup_screen.validate_preconditions_screen()
    assert replace_seal_setup_screen.is_condition_met(ReplaceSealWorkflowPreconditionsLocators.DOOR_STATE_STATUS), f"Door condition is not in passing state"
    assert replace_seal_setup_screen.is_condition_met(ReplaceSealWorkflowPreconditionsLocators.POWER_STATE_STATUS), f"Power condition is not in passing state"


@when('User validates the carriage service process completes')
def validate_carriage_service_process(replace_seal_setup_screen: ReplaceSealWorkflowSetupScreen):
    replace_seal_setup_screen.validate_preconditions_screen()
    replace_seal_setup_screen.tap(ReplaceSealWorkflowLocators.START_BUTTON)
    replace_seal_setup_screen.validate_carriage_status_screen()
    replace_seal_setup_screen.validate_element_wait_condition(ReplaceSealWorkflowLocators.CARRIAGE_STATUS_BANNER,
                                                              ReplaceSealWorkflowLocators.PROCEDURE_ONE_BANNER, WaitTimeConstants.MidWait)


@when('User validates the context in the first procedure screen')
def validate_first_procedure_information(replace_seal_setup_screen: ReplaceSealWorkflowSetupScreen):
    replace_seal_setup_screen.validate_procedure_one_screen()

    actual_paragraph_text = replace_seal_setup_screen.get_procedure_one_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceSealWorkflowConstants.expected_procedure_one_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_seal_setup_screen.tap_next_button()

import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_flow_cell_workflow_constants import \
    ReplaceFlowCellWorkflowConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_components_locators import ReplaceComponentsScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_flow_cell_workflow_locators import ReplaceFlowCellWorkflowLocators, \
    ReplaceFlowCellConditioningLocators, ReplaceFlowCellStatusScreenLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.ReplaceFlowCell.replace_flow_cell_workflow_setup_screen import ReplaceFlowCellWorkflowSetupScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/MaintainScreen/ReplaceComponents/replace_flow_cell_workflow.feature')

logger = Logger(__name__)


@pytest.fixture
def replace_flow_cell_setup_screen(page_builder):
    page = page_builder(ReplaceFlowCellWorkflowSetupScreen)
    return page


@given('User navigates to the replace components HUB area')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen, maintain_screen: MaintainScreen):
    logger.info("The replace flow cell workflow test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_maintain()
    maintain_screen.tap(MaintainScreenPageLocators.REPLACE_PANEL)


@when('User taps the replace flow cell panel')
def tap_replace_column_panel(replace_components_hub_screen: ReplaceComponentsScreen):
    replace_components_hub_screen.tap(ReplaceComponentsScreenPageLocators.REPLACE_FLOWCELL)


@when('User validates the context in the welcome screen')
def validate_welcome_screen_information(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_welcome_screen()

    actual_paragraph_text = replace_flow_cell_setup_screen.get_welcome_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceFlowCellWorkflowConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_flow_cell_setup_screen.tap_next_button()


@when('User validates the context in the caution screen')
def validate_caution_screen_information(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_caution_screen()

    actual_paragraph_text = replace_flow_cell_setup_screen.get_caution_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceFlowCellWorkflowConstants.expected_caution_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_flow_cell_setup_screen.tap_next_button()


@when('User starts the preconditions process validating the conditions')
def start_preconditions_process(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_preconditions_summary_screen()
    replace_flow_cell_setup_screen.tap(ReplaceFlowCellWorkflowLocators.START_BUTTON)
    replace_flow_cell_setup_screen.validate_preconditions_status_screen()
    replace_flow_cell_setup_screen.validate_preconditions_process(WaitTimeConstants.SmallWait)
    replace_flow_cell_setup_screen.tap_next_button()


@when('User validates the context in the removal screen')
def validate_removal_screen_information(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_removal_screen()
    time.sleep(1)
    actual_paragraph_text = replace_flow_cell_setup_screen.get_removal_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceFlowCellWorkflowConstants.expected_removal_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_flow_cell_setup_screen.tap_next_button()


@when('User validates the context in the first installation screen screen')
def validate_first_installation_screen_information(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_first_installation_screen()
    time.sleep(1)
    actual_paragraph_text = replace_flow_cell_setup_screen.get_first_installation_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceFlowCellWorkflowConstants.expected_first_installation_page_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_flow_cell_setup_screen.tap_next_button()


@when('User validates the context in the second installation screen screen')
def validate_first_installation_screen_information(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_second_installation_screen()
    time.sleep(1)
    actual_paragraph_text = replace_flow_cell_setup_screen.get_second_installation_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceFlowCellWorkflowConstants.expected_second_installation_page_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_flow_cell_setup_screen.tap_next_button()


@when(cfparse('User enters the "{flow_rate}" and "{flow_duration}"'))
def enter_flow_values(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen, flow_rate, flow_duration):
    replace_flow_cell_setup_screen.validate_flow_conditioning_screen()
    time.sleep(1)
    replace_flow_cell_setup_screen.tap(ReplaceFlowCellConditioningLocators.FLOW_RATE_FIELD)
    replace_flow_cell_setup_screen.enter_value(flow_rate)
    replace_flow_cell_setup_screen.tap(ReplaceFlowCellConditioningLocators.FLOW_DURATION_FIELD)
    replace_flow_cell_setup_screen.enter_value(flow_duration)


@then('User validates that flow settings screen is in error state')
def validate_flow_error_state(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_flow_conditioning_screen()
    assert replace_flow_cell_setup_screen.is_edit_field_in_error_state(
        ReplaceFlowCellConditioningLocators.FLOW_RATE_FIELD_STATUS), f"The flow rate field is accepting an invalid value"
    assert replace_flow_cell_setup_screen.is_edit_field_in_error_state(
        ReplaceFlowCellConditioningLocators.FLOW_DURATION_FIELD_STATUS), f"The flow duration field is accepting an invalid value"
    replace_flow_cell_setup_screen.validate_next_button_inactive()


@when(cfparse('User selects the "{solvent}"'))
def select_solvent(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen, solvent):
    replace_flow_cell_setup_screen.validate_solvent_conditioning_screen()
    # TODO: solvent selection [INS-25967]
    replace_flow_cell_setup_screen.tap_next_button()


@then('User validates the flow cell conditioning process')
def validate_flow_cell_conditioning(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_status_screen()
    replace_flow_cell_setup_screen.validate_simple_text_wait_condition(ReplaceFlowCellStatusScreenLocators.STATUS_LABEL, "Completed", WaitTimeConstants.MidWait)
    replace_flow_cell_setup_screen.tap_next_button()


@then('User validates the finish screen')
def validate_finish(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.validate_finish_screen()

    replace_flow_cell_setup_screen.tap(ReplaceFlowCellWorkflowLocators.DONE_BUTTON)


@when('User taps next')
def navigate_next(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.tap_next_button()


# TODO can be removed when pytest-bdd will be updated to latest version ATOM-80
@when('User taps cancel')
@then('User taps cancel')
def tap_cancel(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.tap(ReplaceFlowCellWorkflowLocators.CANCEL_BUTTON)


@then('User taps done')
def tap_done(replace_flow_cell_setup_screen: ReplaceFlowCellWorkflowSetupScreen):
    replace_flow_cell_setup_screen.tap(ReplaceFlowCellWorkflowLocators.DONE_BUTTON)


@then('User navigates back to dashboard')
def navigate_dashboard_screen(session_dash_board_screen_page: DashBoardScreen, maintain_screen: MaintainScreen):
    maintain_screen.tap(MaintainScreenPageLocators.BACK_BUTTON)
    session_dash_board_screen_page.tap_home()

import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.pump_maintenance_workflow_constants import PumpMaintenanceWorkflowConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.pump_maintenance_workflow_locators import PumpMaintenanceFlowOptionsLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_components_locators import ReplaceComponentsScreenPageLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.PumpMaintenence.pump_maintenance_workflow_setup_screen import PumpMaintenanceWorkflowSetupScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/MaintainScreen/ReplaceComponents/pump_maintenance_workflow.feature')

logger = Logger(__name__)


@pytest.fixture
def pump_maintenance_setup_screen(page_builder):
    page = page_builder(PumpMaintenanceWorkflowSetupScreen)
    return page


@given('User navigates to the replace components HUB area')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen, maintain_screen: MaintainScreen):
    logger.info("The user profile settings screen test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_maintain()
    maintain_screen.tap(MaintainScreenPageLocators.REPLACE_PANEL)


@when('User taps the pump maintenance panel')
def tap_replace_lamp_panel(replace_components_hub_screen: ReplaceComponentsScreen):
    replace_components_hub_screen.scroll_to_view(ReplaceComponentsScreenPageLocators.PUMP_MAINTENANCE)


@when('User validates the context in the welcome screen')
def validate_welcome_screen_information(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen):
    pump_maintenance_setup_screen.validate_welcome_screen()

    actual_paragraph_text = pump_maintenance_setup_screen.get_welcome_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = PumpMaintenanceWorkflowConstants.expected_welcome_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    pump_maintenance_setup_screen.tap_next_button()


@when('User validates the context in the caution screen')
def validate_caution_screen_information(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen):
    pump_maintenance_setup_screen.validate_cautions_screen()

    actual_paragraph_text = pump_maintenance_setup_screen.get_caution_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = PumpMaintenanceWorkflowConstants.expected_caution_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    pump_maintenance_setup_screen.tap_next_button()


@when('User validates the context in the procedure screen')
def validate_procedure_screen_information(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen):
    pump_maintenance_setup_screen.validate_procedure_screen()

    actual_paragraph_text = pump_maintenance_setup_screen.get_procedure_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = PumpMaintenanceWorkflowConstants.expected_procedure_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    pump_maintenance_setup_screen.tap_next_button()


@when(cfparse('User sets the flush duration time as "{flush_duration}"'))
def set_flush_duration(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen, flush_duration):
    pump_maintenance_setup_screen.validate_flush_options_screen()

    if not pump_maintenance_setup_screen.is_toggle_component_enabled(PumpMaintenanceFlowOptionsLocators.FLUSH_DURATION_TOGGLE):
        pump_maintenance_setup_screen.tap(PumpMaintenanceFlowOptionsLocators.FLUSH_DURATION_TOGGLE)

    pump_maintenance_setup_screen.enter_value(flush_duration)

    pump_maintenance_setup_screen.tap_next_button()


@when(cfparse('User selects a "{solvent}"'))
def select_solvent(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen, solvent):
    pump_maintenance_setup_screen.validate_solvent_options_screen()
    # TODO: solvent selection is wonky because radio groups - INS-25967
    pump_maintenance_setup_screen.tap_next_button()


@when(cfparse('User validates the "{flush_duration}" in summary details'))
def validate_summary_details(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen,
                             flush_duration):
    pump_maintenance_setup_screen.validate_summary_screen()
    pump_maintenance_setup_screen.validate_flush_parameters(flush_duration)


@then('User validates the flush duration field is in error state')
def validate_flush_duration_error_state(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen):
    assert pump_maintenance_setup_screen.is_edit_field_in_error_state(
        PumpMaintenanceFlowOptionsLocators.FLUSH_DURATION_FIELD), f"The flush duration field is accepting invalid values"


@then('User sets the field to the default value')
def set_flush_duration_default(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen):
    pump_maintenance_setup_screen.tap(PumpMaintenanceFlowOptionsLocators.DEFAULT_VALUE_BUTTON)


@then(cfparse('User validates the "{default_value}" has been set'))
def validate_default_flush_value(pump_maintenance_setup_screen: PumpMaintenanceWorkflowSetupScreen, default_value):
    current_flush_value = pump_maintenance_setup_screen.get_entered_value(PumpMaintenanceFlowOptionsLocators.FLUSH_DURATION_FIELD_VALUE)
    assert current_flush_value == default_value, f"The flush value was not set to the default. | Current: {current_flush_value} Expected: {default_value}"

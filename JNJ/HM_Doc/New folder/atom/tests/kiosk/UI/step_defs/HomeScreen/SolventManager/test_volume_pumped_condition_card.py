import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import VolumePumpedConditionCard
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.volume_pump_settings_screen import PumpVolumeSettingsScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.sm_home_screen import SolventManagerHomeScreenLocators as sml
from web_framework.kiosk.pages.Locators.Home.SolventManager.volume_pumped_condition_card_locators import \
    VolumePumpSettingsScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SolventManager/volume_pumped_condition_card.feature')

logger = Logger("test_flow_path_condition_card")


@pytest.fixture
def pump_volume_settings_screen_page(page_builder):
    page = page_builder(PumpVolumeSettingsScreen)
    page.implicitly_wait()
    return page


@given('User navigates to the third solvent manager page')
def navigate_solvent_manager_third_page(solvent_manager_home_screen_page: SolventManagerHomeScreen):
    logger.info("**************************The flow path condition card test starts**********************")
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap_third_page()
    solvent_manager_home_screen_page.tap(sml.VOLUME_PUMP_CONDITION_CARD)


@when(cfparse('User sets the threshold volume to "{threshold_volume}"'))
def navigate_1flow_path_card(pump_volume_settings_screen_page: PumpVolumeSettingsScreen, threshold_volume):
    time.sleep(2)
    pump_volume_settings_screen_page.tap_toggle_button_on(VolumePumpSettingsScreenLocators.FLOW_TOGGLE_BUTTON)
    pump_volume_settings_screen_page.clear_num_pad_entries(VolumePumpSettingsScreenLocators.FLOW_RATE_EDIT_FIELD)
    pump_volume_settings_screen_page.enter_value(threshold_volume)


@when('User confirms the settings for threshold volume')
def tap_done_button(pump_volume_settings_screen_page: PumpVolumeSettingsScreen):
    pump_volume_settings_screen_page.tap_done_button()


@then('User validates the system displays readback message when the threshold volume is meet')
def validate_volume_pumped(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                           dashboard_screen_page: DashBoardScreen):
    solvent_manager_home_screen_page.wait_time_to_load_value(sml.THRESHOLD_VOLUME_LABEL, "")
    threshold_volume = solvent_manager_home_screen_page.get_volume(
        sml.THRESHOLD_VOLUME_LABEL)
    current_volume_pumped = solvent_manager_home_screen_page.get_volume(
        sml.CURRENT_VOLUME_PUMP)

    while current_volume_pumped < threshold_volume:
        logger.info(f"Inside first while loop current_volume_pumped ==>>>{current_volume_pumped}")

        current_volume_pumped = solvent_manager_home_screen_page.get_volume(
            sml.CURRENT_VOLUME_PUMP)

        current_readback_value = solvent_manager_home_screen_page.get_text(
            sml.READ_BACK_MESSAGE)
        logger.info(f"Inside first while loop current_readback_value ==>>>{current_readback_value}")

        if current_readback_value == VolumePumpedConditionCard.NearThresholdReadBackMessage:
            logger.info(f"Exiting the first while loop")
            break
        time.sleep(1)

    start_time = time.time()
    while time.time() - start_time < VolumePumpedConditionCard.TimetoReachOverThresholdValue:
        logger.info(f"Inside second while loop")
        current_volume_pumped = solvent_manager_home_screen_page.get_volume(
            sml.CURRENT_VOLUME_PUMP)

        if current_volume_pumped >= threshold_volume:
            current_readback_value = solvent_manager_home_screen_page.get_text(
                sml.READ_BACK_MESSAGE)

            assert current_readback_value == VolumePumpedConditionCard.ThresholdReachedReadBackMessage or current_readback_value == VolumePumpedConditionCard.OverMaximumReadbackMessage
            logger.info(f"Exiting the second, while loop current_readback_value===>>>{current_readback_value}")
            break

        time.sleep(1)
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_solvent_manager_schematic_icon()
    logger.info(f'The test ran successful')


@then(cfparse('User validate the edit field state "{is_error_state}"'))
def validate_edit_field(pump_volume_settings_screen_page: PumpVolumeSettingsScreen,
                        is_error_state, dashboard_screen_page: DashBoardScreen):
    try:
        edit_field_error_state = pump_volume_settings_screen_page.is_edit_field_in_error_state(
            VolumePumpSettingsScreenLocators.FLOW_RATE_EDIT_FIELD_STATE)
        error_state = TypeConverter.to_bool(is_error_state)
        assert edit_field_error_state == error_state, f" actual edit field error state is ==>> {edit_field_error_state}"
    finally:
        pump_volume_settings_screen_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_solvent_manager_schematic_icon()


@then("User validates the hint messages for the empty flow edit field")
def validate_flow_helper_message(pump_volume_settings_screen_page: PumpVolumeSettingsScreen,
                                 dashboard_screen_page: DashBoardScreen):
    try:
        hint_locator = VolumePumpSettingsScreenLocators.FLOW_HINT_LOCATOR
        expected_hint_message = VolumePumpedConditionCard.EmptyEditFieldMessage
        pump_volume_settings_screen_page.validate_hint_message(hint_locator, expected_hint_message)

    finally:
        pump_volume_settings_screen_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_solvent_manager_schematic_icon()


@then("User validates the hint messages for the flow edit field")
def validate_flow_helper_message(pump_volume_settings_screen_page: PumpVolumeSettingsScreen,
                                 dashboard_screen_page: DashBoardScreen):
    try:
        hint_locator = VolumePumpSettingsScreenLocators.FLOW_HINT_LOCATOR
        expected_hint_message = VolumePumpedConditionCard.FlowHintMessage
        pump_volume_settings_screen_page.validate_hint_message(hint_locator, expected_hint_message)

    finally:
        pump_volume_settings_screen_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_solvent_manager_schematic_icon()

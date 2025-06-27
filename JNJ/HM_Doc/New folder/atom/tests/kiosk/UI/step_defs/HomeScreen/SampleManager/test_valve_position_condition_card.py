from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from utilities.datatables.headless_datatable import headlesstable
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SampleManager.sm_home_screen import SampleManagerHomeScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SampleManager/valve_position_condition_card.feature')


@given('User navigates to the sample manager screen')
def navigate_sample_manager_home_screen(sample_manager_home_screen_page: SampleManagerHomeScreen):
    sample_manager_home_screen_page.validate_injector_valve_position_card()


@when('User obtains the current valve position')
def get_current_valve_position(context, sample_manager_home_screen_page: SampleManagerHomeScreen):
    sample_manager_home_screen_page.wait_time_to_load_value(SampleManagerHomeScreenLocators.DISPLAYED_VALVE_POSITION_CONDITIONAL_CARD, "---")
    context['current_valve_position'] = sample_manager_home_screen_page.get_valve_position_conditional_card()


@then(headlesstable("User validates that the current valve position is one of expected:"))
def validate_current_valve_position(context, table):
    valve_positions_list = table
    assert any(context['current_valve_position'] in valve for valve in valve_positions_list), f"Expected valve positions: {valve_positions_list}. " \
                                                                                              f"Actual valve position:{context['current_valve_position']}"

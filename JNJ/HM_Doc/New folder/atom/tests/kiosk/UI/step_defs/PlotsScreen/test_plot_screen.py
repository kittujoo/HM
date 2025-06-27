import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse

from utilities.assert_timeout import AssertTimeout
from utilities.datatables.converters import CONVERTERS
from utilities.string_utility import is_text_present
from web_framework.kiosk.common.Constants.UI.plots import PlotsConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Plots.plots_screen_locators import PlotScreenLocators, PlotsSettingsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.PlotsScreen.plots_screen import PlotsScreen
from web_framework.kiosk.pages.PlotsScreen.plots_settings_screen import PlotsSettingsScreen
from web_framework.kiosk.pages.PlotsScreen.plots_settings_screen_locators_lookup import PlotsSettingsLookup

if __name__ == Path(__file__).stem:
    scenarios('../../features/PlotsScreen/plots_screen.feature')


@pytest.fixture
def plots_screen_page(session_dash_board_screen_page: DashBoardScreen, page_builder):
    session_dash_board_screen_page.tap_plots_icon()
    page = page_builder(PlotsScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def plots_settings_screen_page(page_builder):
    page = page_builder(PlotsSettingsScreen)
    page.implicitly_wait()
    return page


@given('User turns off all the enabled plots')
def set_prerequisites(plots_screen_page: PlotsScreen, plots_settings_screen_page: PlotsSettingsScreen):
    plots_screen_page.validate_plot_screen()
    plots_screen_page.clear_plots_list(plots_settings_screen_page)
    plots_screen_page.clear_plots_color_list(plots_settings_screen_page)
    plots_screen_page.tap(PlotScreenLocators.SETTINGS_ICON)
    plots_settings_screen_page.validate_plot_settings_screen()
    plots_settings_screen_page.turn_off_plots()
    plots_settings_screen_page.tap_done_button()
    plots_settings_screen_page.wait_till_element_is_invisible(BasePageLocators.DONE_BUTTON, plots_settings_screen_page.long_wait_time)


@when('User pause the plots to change the settings')
def tap_pause_icon(plots_screen_page: PlotsScreen):
    plots_screen_page.validate_plot_screen()
    plots_screen_page.pause_plots()


@when(cfparse('User change the time range to "{time_window}" in the settings screen'))
def select_time_window(time_window: str, plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.validate_plot_settings_screen()
    if time_window == "Custom":
        plots_settings_screen_page.select_time_window(time_window)
        plots_settings_screen_page.set_default_hour()
    else:
        plots_settings_screen_page.select_time_window(time_window)


@when('User taps the settings icon')
def navigate_to_settings_screen(plots_screen_page: PlotsScreen):
    plots_screen_page.wait_element_to_be_clickable(PlotScreenLocators.SETTINGS_ICON, plots_screen_page.wait_time)
    plots_screen_page.tap(PlotScreenLocators.SETTINGS_ICON)


@when('The user confirms the time window selection')
@then('The user confirms the time window selection')
def tap_done_button(plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.tap_done_button()
    plots_settings_screen_page.wait_till_element_is_invisible(BasePageLocators.DONE_BUTTON, plots_settings_screen_page.long_wait_time)


@when(cfparse('User taps the settings icon of the plot "{settings_icon}"'))
def navigate_to_plots_settings_screen(settings_icon: str, plots_settings_screen_page: PlotsSettingsScreen,
                                      plots_screen_page: PlotsScreen):
    plots_screen_page.validate_plot_screen()
    plots_settings_screen_page.tap_plots_settings_icons(settings_icon)


@when('User taps the plot screen')
def tap_plots_screen(plots_screen_page: PlotsScreen):
    plots_screen_page.wait_for_element_load(PlotScreenLocators.PLOT_SCREEN, plots_screen_page.wait_time)
    plots_screen_page.tap(PlotScreenLocators.PLOT_SCREEN)


@when(cfparse('User selects the "{time_in_hours}" "{time_in_minutes}" from the time wheel component'))
def select_time(time_in_hours: str, time_in_minutes: str, plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.validate_plot_settings_screen()
    plots_settings_screen_page.set_default_hour()
    plots_settings_screen_page.set_spinner_value(PlotsSettingsScreenLocators.HOURS_PICKER_WHEEL, time_in_hours)
    plots_settings_screen_page.scroll_to_spinner_options(time_in_minutes, PlotsSettingsLookup.time_in_minutes_dictionary)


@when(cfparse('User selects the "{plot_number}" plot to display "{plot_name}" in "{color}" for "{plot_option}"'))
def select_first_plots(plot_number: str, plot_name: str, color: str, plot_option: str, plots_settings_screen_page: PlotsSettingsScreen):
    if plot_number == "First":
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_ONE_TAB, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_ONE_TAB)
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_ONE_TOGGLE_BUTTON, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap_toggle_button_on(PlotsSettingsScreenLocators.PLOT_ONE_TOGGLE_BUTTON)
        plots_settings_screen_page.select_plot_options(plot_option)
        plots_settings_screen_page.select_spinner_text_for_plots(PlotsSettingsScreenLocators.PLOTS_SPINNER_LOCATOR, plot_name)
        plots_settings_screen_page.add_previous_plot(plot_name)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_ONE_COLOR_TAB)
        plots_settings_screen_page.select_plot_color(color)
        plots_settings_screen_page.add_previous_plot_color(color)

    elif plot_number == "Second":
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_TWO_TAB, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_TWO_TAB)
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_TWO_TOGGLE_BUTTON, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap_toggle_button_on(PlotsSettingsScreenLocators.PLOT_TWO_TOGGLE_BUTTON)
        plots_settings_screen_page.select_plot_options(plot_option)
        plots_settings_screen_page.select_spinner_text_for_plots(PlotsSettingsScreenLocators.PLOTS_SPINNER_LOCATOR,
                                                                 plot_name)
        plots_settings_screen_page.add_previous_plot(plot_name)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_TWO_COLOR_TAB)
        plots_settings_screen_page.select_plot_color(color)
        plots_settings_screen_page.add_previous_plot_color(color)

    elif plot_number == "Third":
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_THREE_TAB, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_THREE_TAB)
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_THREE_TOGGLE_BUTTON, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap_toggle_button_on(PlotsSettingsScreenLocators.PLOT_THREE_TOGGLE_BUTTON)
        plots_settings_screen_page.select_plot_options(plot_option)
        plots_settings_screen_page.select_spinner_text_for_plots(PlotsSettingsScreenLocators.PLOTS_SPINNER_LOCATOR,
                                                                 plot_name)
        plots_settings_screen_page.add_previous_plot(plot_name)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_THREE_COLOR_TAB)
        plots_settings_screen_page.select_plot_color(color)
        plots_settings_screen_page.add_previous_plot_color(color)

    elif plot_number == "Fourth":
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_FOUR_TAB, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_FOUR_TAB)
        plots_settings_screen_page.wait_for_element_load(PlotsSettingsScreenLocators.PLOT_FOUR_TOGGLE_BUTTON, plots_settings_screen_page.wait_time)
        plots_settings_screen_page.tap_toggle_button_on(PlotsSettingsScreenLocators.PLOT_FOUR_TOGGLE_BUTTON)
        plots_settings_screen_page.select_plot_options(plot_option)
        plots_settings_screen_page.select_spinner_text_for_plots(PlotsSettingsScreenLocators.PLOTS_SPINNER_LOCATOR,
                                                                 plot_name)
        plots_settings_screen_page.add_previous_plot(plot_name)
        plots_settings_screen_page.tap(PlotsSettingsScreenLocators.PLOT_FOUR_COLOR_TAB)
        plots_settings_screen_page.select_plot_color(color)
        plots_settings_screen_page.add_previous_plot_color(color)


@when('User play the plots')
@then('User play the plots')
def play_plots(plots_screen_page: PlotsScreen):
    plots_screen_page.validate_plot_screen()
    plots_screen_page.play_plots()


@when(cfparse('user taps the plot "{number}" more action icon'))
@then(cfparse('user taps the plot "{number}" more action icon'))
def tap_more_action_icon(number: str, plots_settings_screen_page: PlotsSettingsScreen, plots_screen_page: PlotsScreen):
    plots_screen_page.validate_plot_screen()
    plots_settings_screen_page.select_more_action_icons(number)


@then(cfparse('User validate the visibility of time wheel scroll component "{expected_time_wheel_visibility: bool}"', CONVERTERS))
def validate_wheel_visibility(expected_time_wheel_visibility: bool, plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.validate_plot_settings_screen()
    actual_time_wheel_visibility = plots_settings_screen_page.is_time_wheel_visible()
    assert actual_time_wheel_visibility is expected_time_wheel_visibility, f"The time wheel visibility is not as expected. \
                                                                            Expected: {expected_time_wheel_visibility}. Actual: {actual_time_wheel_visibility}"


@then(cfparse('User validates the plots showing for the selected time "{expected_time_window}"'))
def validate_plots_time_window(expected_time_window: str, plots_screen_page: PlotsScreen):
    plots_screen_page.validate_plot_screen()
    actual_start_time = plots_screen_page.get_start_time_window_value()
    actual_end_time = plots_screen_page.get_end_time_window_value()
    actual_time_unit = plots_screen_page.get_text(PlotScreenLocators.TIME_UNIT)
    expected_end_time = PlotsConstants.EndTime
    expected_time_unit = PlotsConstants.TimeUnit

    assert actual_start_time == expected_time_window, f"Start time in plots is not as expected. \
                                                        Expected Start Time: {expected_time_window}. Actual start time: {actual_start_time}"
    assert actual_end_time == expected_end_time, f"End time in plots is not as expected. \
                                                        Expected End Time: {expected_end_time}. Actual end time: {actual_end_time}"
    assert actual_time_unit == expected_time_unit, f"Time Unit in plots is not as expected. \
                                                        Expected Time unit: {expected_time_unit}. Actual end time: {actual_time_unit}"


@then(cfparse('User validates the custom time "{expected_time}" in the selector component'))
def validate_custom_time(expected_time: str, assert_timeout: AssertTimeout, plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.validate_plot_settings_screen()
    assert_timeout.are_equal(lambda: plots_settings_screen_page.get_selected_time_window_options(), expected_time,
                             f"The custom time from the selector component is not as expected. \
                                        Expected Time: {expected_time} Actual Time: {plots_settings_screen_page.get_selected_time_window_options()}",
                             timeout_in_seconds=plots_settings_screen_page.wait_time,
                             polling_period_in_seconds=1)


@then(cfparse('User validate the only plot "{number}" more action icon is extended'))
def validate_action_icon_extended(number: str, plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.validate_more_action_icon_extended(number)


@then('User taps on plot title text')
def tap_plot_text(plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.tap(PlotScreenLocators.TIME_WINDOW_COMPONENT)


@then('validate all the plots more action icons are retracted')
def validate_icons_retracts(plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.validate_action_icons_retracted()


@then(cfparse('User taps on navigation "{icon}" in the dashboard screen'))
def tap_navigation_icon(icon: str, dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.select_icon(icon)


@then(cfparse('User validates the "{text_to_find}" text is "{expected_text_presence: bool}"', CONVERTERS))
def validate_text_presence(text_to_find: str, expected_text_presence: bool, plots_settings_screen_page: PlotsSettingsScreen):
    actual_text = plots_settings_screen_page.get_text(PlotsSettingsScreenLocators.CUSTOM_TIME_WINDOW)
    actual_text_presence = is_text_present(actual_text, text_to_find)
    assert actual_text_presence == expected_text_presence, f" The string is not present. Expected: {expected_text_presence}. Actual: {actual_text_presence}"


@then(cfparse('Validate the given time window option is selected as "{expected_time_option}"'))
def validate_time_option_displayed(expected_time_option: str, plots_screen_page: PlotsScreen):
    plots_screen_page.validate_plot_screen()
    plots_screen_page.tap(PlotScreenLocators.SETTINGS_ICON)
    plots_screen_page.validate_time_option_selected(expected_time_option)
    plots_screen_page.tap_cancel_button()


@then(cfparse('Validate the play button is displayed "{expected_play_button_value: bool}" for settings screen', CONVERTERS))
def validate_play_pause_button(expected_play_button_value: bool, plots_settings_screen_page: PlotsSettingsScreen):
    actual_play_button_value = plots_settings_screen_page.is_play_button_displayed()
    assert actual_play_button_value == expected_play_button_value, f"Play button displayed is not as expected. Expected: {expected_play_button_value}. \
                                                                    Actual: {actual_play_button_value}"


@then(cfparse('User Validate the play button is displayed "{expected_plot_screen_value: bool}" in the plots screen', CONVERTERS))
def validate_plots_screen_play_pause_button(expected_plot_screen_value: bool, plots_screen_page: PlotsScreen):
    plots_screen_page.wait_for_element_load(PlotScreenLocators.PLAY_PAUSE_ELEMENT, plots_screen_page.wait_time)
    actual_play_button_value = plots_screen_page.is_play_button_displayed()
    assert actual_play_button_value == expected_plot_screen_value, f"Play button displayed is not as expected. \
                                                                    Expected: {expected_plot_screen_value}. Actual: {actual_play_button_value}"


@then('User taps the play-pause centre button')
def tap_play_pause_center_button(plots_settings_screen_page: PlotsSettingsScreen):
    plots_settings_screen_page.tap(PlotsSettingsScreenLocators.CENTER_PLAY_PAUSE_BUTTON)


@then('User validates the plots displayed in the plot hub screen')
def validate_plots(plots_screen_page: PlotsScreen, plots_settings_screen_page: PlotsSettingsScreen):
    plots_screen_page.validate_plot_graph_screen()
    expected_plots = plots_screen_page.get_text_from_list(PlotScreenLocators.CHART_ELEMENTS)
    current_plots_color = plots_screen_page.get_color_code_list(PlotScreenLocators.PLOTS_GRAPH)

    actual_plots = plots_screen_page.get_previous_plots(plots_settings_screen_page)
    actual_plots_color = plots_screen_page.get_previous_plots_color(plots_settings_screen_page)

    plots_screen_page.validate_color(actual_plots_color, current_plots_color)
    plots_screen_page.validate_graph(PlotScreenLocators.PLOTS_GRAPH)
    assert actual_plots == expected_plots, f"Plots displayed are not as expected. Expected plots: {expected_plots}. Actual plots: {actual_plots}"

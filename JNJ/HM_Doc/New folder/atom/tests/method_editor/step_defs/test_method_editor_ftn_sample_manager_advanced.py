from pytest_bdd import given, when, scenarios, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from web_framework.method_editor.pages.sample_manager.menu_item_sample_manager import SampleManagerMenu
from web_framework.method_editor.pages.sample_manager.sample_manager_advanced_page import SampleManagerAdvancedPage

scenarios('../features/method_editor_ftn_sample_manager_advanced.feature')


@when('the Sample Manager Advanced menu is opened', target_fixture="sample_manager_advanced_page")
@given('the Sample Manager Advanced menu is opened', target_fixture="sample_manager_advanced_page")
def open_sample_manager_advanced_menu(sample_manager_menu: SampleManagerMenu):
    sample_manager_advanced_page = sample_manager_menu.open_advanced()
    return sample_manager_advanced_page


@then(cfparse('the Sample Manager Advanced menu title is "{expected_title}"'))
def validate_sample_manager_advanced_menu_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_sample_manager_advanced_title()
    assert actual_title == expected_title, f"The Sample Manager Advanced menu title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the setting group title is "{expected_title}"'))
def validate_sample_manager_advanced_settings_group_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_sample_manager_advanced_setting_group_title()
    assert actual_title == expected_title, f"The Sample Manager Advanced menu settings title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Values setting title is "{expected_title}"'))
def validate_sample_manager_advanced_values_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_sample_manager_advanced_values()
    assert actual_title == expected_title, f"The Sample Manager Advanced values title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Values setting description is "{expected_title}"'))
def validate_sample_manager_advanced_values_summary(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_sample_manager_advanced_summary()
    assert actual_title == expected_title, f"The Sample Manager Advanced values summary is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Default selector title is "{expected_title}"'))
def validate_sample_manager_advanced_default_selector(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_sample_manager_advanced_default()
    assert actual_title == expected_title, f"The Sample Manager Advanced default selector is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Custom selector title is "{expected_title}"'))
def validate_sample_manager_advanced_custom_selector(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_sample_manager_advanced_custom()
    assert actual_title == expected_title, f"The Sample Manager Advanced custom selector is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then('the Default selector is selected')
def check_default_selector_highlighted(sample_manager_advanced_page: SampleManagerAdvancedPage):
    # TODO currently there is no possibility to determine that a selector is highlighted
    pass


@then('the Custom selector is selected')
def check_custom_selector_highlighted(sample_manager_advanced_page: SampleManagerAdvancedPage):
    # TODO currently there is no possibility to determine that a selector is highlighted
    pass


@then(cfparse('the setting titles Automatic Vial Bottom Detection title is "{expected_title}"'))
def validate_automatic_vial_bottom_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_vial_bottom_title()
    assert actual_title == expected_title, f"The Automatic Vial Bottom title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the setting titles Needle Placement from Bottom (mm) title is "{expected_title}"'))
def validate_needle_placement_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_needle_placement_title()
    assert actual_title == expected_title, f"The Needle Placement title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the setting titles Syringe Draw Rate (μL/min) title is "{expected_title}"'))
def validate_syringe_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_syringe_title()
    assert actual_title == expected_title, f"The Syringe title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@when('the Values selector is set to Default')
def select_default_selector(sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_default()


@when('the Values selector is set to Custom')
def select_custom_selector(sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_custom()


@then(cfparse('the Needle Placement from Bottom setting description is "{expected_title}"'))
def validate_needle_placement_description(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_needle_placement_summary()
    assert actual_title == expected_title, f"The  Needle Placement description is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Needle Placement from Bottom input hint text is "{expected_title}"'))
def validate_needle_placement_description(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_needle_placement_hint()
    assert actual_title == expected_title, f"The  Needle Placement hint is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Syringe Draw Rate input hint text is "{expected_title}"'))
def validate_syringe_title(expected_title, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_title = sample_manager_advanced_page.get_syringe_hint()
    assert actual_title == expected_title, f"The Syringe hint is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then("the Sample Manager Advanced setting group is displayed")
def validate_sample_manager_advanced_setting_group(sample_manager_advanced_page: SampleManagerAdvancedPage):
    assert sample_manager_advanced_page.is_sample_manager_advanced_displayed(), "Sample Manager Advanced is not displayed"


@then(cfparse('the Sample Manager Advanced menu summary is "{expected_value}"'))
def validate_sample_manager_advanced_menu_summary(expected_value, sample_manager_menu: SampleManagerMenu):
    actual_value = sample_manager_menu.get_advanced_state()
    assert actual_value == expected_value, f"The Sample Manager Advanced menu summary value is incorrect. Expected: [{expected_value}], Actual: [{actual_value}]"


@then(cfparse('the Automatic Vial Bottom Detection toggle is "{toggle_state:bool}" and "{is_active:str}"', CONVERTERS))
def check_automatic_vial_bottom_detection_toggle(toggle_state: bool, is_active: str, sample_manager_advanced_page: SampleManagerAdvancedPage):
    is_active_state = True if is_active == "active" else False
    sample_manager_advanced_page.validate_automatic_vial_bottom_detection_toggle_state(toggle_state)
    sample_manager_advanced_page.validate_automatic_vial_bottom_detection_toggle_is_enabled(is_active_state)


@then(cfparse('the "Needle Placement from Bottom" input is "{is_active:str}"', CONVERTERS))
@then(cfparse('the Needle Placement from Bottom input is "{is_active:str}"', CONVERTERS))
def check_needle_placement_editbox_is_active(is_active: str, sample_manager_advanced_page: SampleManagerAdvancedPage):
    state = True if is_active == "active" else False
    sample_manager_advanced_page.validate_needle_placement_editbox_is_enabled(state)


@then(cfparse('the "Syringe Draw Rate" input is "{is_active:str}"', CONVERTERS))
@then(cfparse('the Syringe Draw Rate input is "{is_active:str}"', CONVERTERS))
def check_syringe_editbox_is_active(is_active: str, sample_manager_advanced_page: SampleManagerAdvancedPage):
    state = True if is_active == "active" else False
    sample_manager_advanced_page.validate_syringe_editbox_is_enabled(state)


@when(cfparse('the Needle Placement from Bottom input is set to out of range value "{value}"'))
@when(cfparse('the Needle Placement from Bottom input is set to "{value}"'))
@when(cfparse('the Needle Placement from Bottom input is set to valid value "{value}"'))
def set_needle_placement_input(value, sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_needle_placement_editbox(value)


@when(cfparse('the Syringe Draw Rate input is set to out of range value "{value}"'))
@when(cfparse('the Syringe Draw Rate input is set to "{value}"'))
@when(cfparse('the Syringe Draw Rate input is set to valid value "{value}"'))
def set_syringe_input(value, sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_syringe_editbox(value)


@then(cfparse('the "Needle Placement from Bottom" input has value set to "{expected_value}"'))
@then(cfparse('the Needle Placement from Bottom input has value set to "{expected_value}"'))
def validate_needle_placement_editbox(expected_value, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_value = sample_manager_advanced_page.get_needle_placement_editbox()
    assert float(actual_value) == float(
        expected_value), f"The Needle Placement editbox value is incorrect. Expected: [{expected_value}], Actual: [{actual_value}]"


@then(cfparse('the "Syringe Draw Rate" input has value set to "{expected_value}"'))
@then(cfparse('the Syringe Draw Rate input has value set to "{expected_value}"'))
def validate_syringe_editbox(expected_value, sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_value = sample_manager_advanced_page.get_syringe_editbox()
    assert float(actual_value) == float(expected_value), f"The Syringe editbox value is incorrect. Expected: [{expected_value}], Actual: [{actual_value}]"


@then(cfparse('the Needle Placement from Bottom input is empty'))
def validate_needle_placement_editbox(sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_value = sample_manager_advanced_page.get_needle_placement_editbox()
    assert float(actual_value) == float(0), f"the Needle Placement from Bottom input is empty. Expected: [0], Actual: [{actual_value}]"


@then('the Syringe Draw Rate input is empty')
def validate_syringe_editbox(sample_manager_advanced_page: SampleManagerAdvancedPage):
    actual_value = sample_manager_advanced_page.get_syringe_editbox()
    assert float(actual_value) == float(0), f"the Syringe Draw Rate input is not empty. Expected: [0], Actual: [{actual_value}]"


@then("the Needle Placement from Bottom input is not in error")
def validate_needle_placement_not_in_error(sample_manager_advanced_page: SampleManagerAdvancedPage):
    # TODO currently there is no possibility to determine that needle placement editbox not in error state
    pass


@then("the Syringe Draw Rate input is not in error")
def validate_syringe_draw_rate_not_in_error(sample_manager_advanced_page: SampleManagerAdvancedPage):
    # TODO currently there is no possibility to determine that syringe editbox not in error state
    pass


@then("the Needle Placement from Bottom input is in error")
def validate_needle_placement_not_in_error(sample_manager_advanced_page: SampleManagerAdvancedPage):
    # TODO currently there is no possibility to determine that needle placement editbox in error state
    pass


@then("the Syringe Draw Rate input is in error")
def validate_syringe_draw_rate_in_error(sample_manager_advanced_page: SampleManagerAdvancedPage):
    # TODO currently there is no possibility to determine that syringe editbox in error state
    pass


@when('the Needle Placement from Bottom input is in error')
def set_needle_placement_not_in_error(sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_needle_placement_editbox(40)


@when('the Syringe Draw Rate input is in error')
@when('the "Syringe Draw Rate" input is in error')
def set_syringe_draw_rate_in_error(sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_syringe_editbox(5)


@when(cfparse('the Automatic Vial Bottom Detection toggle is set to "{toggle_state:bool}"', CONVERTERS))
def set_automatic_vial_bottom_detection_toggle(toggle_state: bool, sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.set_automatic_vial_bottom_detection_toggle(toggle_state)


@then(cfparse('the Automatic Vial Bottom Detection toggle is set to "{toggle_state:bool}"', CONVERTERS))
def validate_automatic_vial_bottom_detection_toggle(toggle_state: bool, sample_manager_advanced_page: SampleManagerAdvancedPage):
    sample_manager_advanced_page.validate_automatic_vial_bottom_detection_toggle_state(toggle_state)

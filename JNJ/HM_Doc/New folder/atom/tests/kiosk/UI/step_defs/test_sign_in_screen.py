from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.sign_in_screen_locators import SignInScreenLocators
from web_framework.kiosk.pages.lock_screen import LockScreen
from web_framework.kiosk.pages.sign_in_screen import SignInScreen

if __name__ == Path(__file__).stem:
    scenarios('../features/sign_in_screen_positive.feature',
              '../features/sign_in_screen_negative.feature')
logger = Logger("test_sign_in_screen")


@given('Sign in page is displayed', target_fixture="sign_in_screen_page")
def sign_in_screen_page(lock_screen_page: LockScreen, page_builder):
    lock_screen_page.press_esc_key()
    sign_in_page = page_builder(SignInScreen)
    return sign_in_page


@when(cfparse('The "{valid_pin}" is entered'))
def enter_the_pin(sign_in_screen_page: SignInScreen, valid_pin):
    # Logger.info("The valid pin entered to unlock the kiosk app is {0}".format(valid_pin))
    sign_in_screen_page.validate_sign_in_screen()
    logger.info(f"User enters the valid pin :{valid_pin}")
    sign_in_screen_page.enter_pin(valid_pin)


@when('User taps delete')
def tap_delete_button(sign_in_screen_page: SignInScreen):
    sign_in_screen_page.tap(SignInScreenLocators.DELETE_BUTTON)


@when('User deletes the PIN entries')
def delete_pin_entries(sign_in_screen_page: SignInScreen):
    sign_in_screen_page.validate_sign_in_screen()
    sign_in_screen_page.delete_pin_entries()


@then('Pin entry field must be empty')
def check_pin_entered(sign_in_screen_page: SignInScreen):
    pin_entered = sign_in_screen_page.get_pin_entered()
    logger.info(f"The pin in the pin entry field is {pin_entered}")
    logger.info("Pin entry field should be empty")
    assert (pin_entered == ""), \
        "Failed to clear the pin number , pin_entered" \
        "= {}".format(pin_entered)
    logger.info('\n************************** The test ends for the sign in screen of the kiosk app*******************')


@when('Tap the eye icon')
def tap_on_eye(sign_in_screen_page: SignInScreen):
    logger.info("User taps the eye icon ")
    sign_in_screen_page.tap_show_password_icon()


@then('The screen should display/show the pin number entered')
def check_pin_entered(sign_in_screen_page: SignInScreen):
    pin_entered = sign_in_screen_page.get_pin_entered()
    logger.info("The pin from the pin entry field after tapping the eye icon  is {0}".format(pin_entered))
    assert "1234" in pin_entered
    logger.info('\n************************** The test ends for the sign in screen of the kiosk app*******************')


@when('Tap the unlock button')
def tap_unlock_button(sign_in_screen_page: SignInScreen):
    sign_in_screen_page.validate_sign_in_screen()
    logger.info("User taps the unlock button ")
    sign_in_screen_page.tap_unlock_button()


@then('The dashboard page is displayed')
def sign_in_navigates_to_dashboard(dash_board_screen_page: DashBoardScreen):
    dash_board_screen_page.implicitly_wait()
    home_icon_exists = dash_board_screen_page.is_home_icon_exists()
    logger.info(f"Dashboard screen is displayed : {home_icon_exists}")
    assert home_icon_exists, "Failed to move to DashBoard screen"
    logger.info('\n************************* The test ends for the sign in screen of the kiosk app********************')


@when('Tap the "BACK" button in the lock screen')
def tap_back_button(sign_in_screen_page: SignInScreen):
    sign_in_screen_page.validate_sign_in_screen()
    logger.info('User taps the  back button')
    sign_in_screen_page.tap_back_button()


@when('Unlock the application')
def unlock_application(lock_screen_page: LockScreen):
    logger.info("User navigates to the signin screen")
    lock_screen_page.press_esc_key()


@then('The Screen should transit to unlock screen')
def sign_in_navigates_to_unlock_screen(lock_screen_page: LockScreen):
    swipe_to_unlock_component_exists = lock_screen_page.swipe_to_unlock_component_exists()
    logger.info("The unlock screen is displayed after tapping the back button :{}".
                format(swipe_to_unlock_component_exists))
    assert swipe_to_unlock_component_exists, "Failed to move to lock screen"
    logger.info('\n************************** The test ends for the sign in screen of the kiosk app*******************')


# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@when('The system should prompt incorrect pin')
@then('The system should prompt incorrect pin')
def system_prompt_incorrect_pin(sign_in_screen_page: SignInScreen):
    error_message = sign_in_screen_page.display_error_message()
    logger.info("The error message displayed is :{0}".format(error_message))
    assert error_message == 'Incorrect PIN', \
        "Failed to show correct pin display , error_message" \
        "= {}".format(error_message)
    assert sign_in_screen_page.is_edit_field_in_error_state(SignInScreenLocators.PIN_FIELD_STATE)
    logger.info('\n************************* The test ends for the sign in screen of the kiosk app********************')


@then('User verifies the entry field is not in error state')
def validate_non_error_state(sign_in_screen_page: SignInScreen):
    assert not sign_in_screen_page.is_edit_field_in_error_state(SignInScreenLocators.PIN_FIELD_STATE)


@when(cfparse('The "{invalid_pin}" is entered'))
def enter_invalid_pin(sign_in_screen_page: SignInScreen, invalid_pin):
    sign_in_screen_page.validate_sign_in_screen()
    logger.info("The invalid pin entered to unlock the kiosk app is {0}".format(invalid_pin))
    sign_in_screen_page.enter_pin(invalid_pin)


@then('The system should prompt "Pin Required" error message')
def system_prompt_pin_required_message(sign_in_screen_page: SignInScreen):
    error_message = sign_in_screen_page.display_error_message()
    logger.info("The error message displayed is :{0}".format(error_message))
    assert error_message == 'Pin Required', \
        "Failed to show valid error message , error_message" \
        "= {}".format(error_message)
    logger.info('\n************************ The test ends for the sign in screen of the kiosk app********************')

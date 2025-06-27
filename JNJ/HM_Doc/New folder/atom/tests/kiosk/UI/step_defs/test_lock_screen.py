from pathlib import Path
from pytest_bdd import scenarios, given, when, then

from web_framework.kiosk.pages.lock_screen import LockScreen

if __name__ == Path(__file__).stem:
    scenarios('../../UI/features/lock_screen.feature')


@given('Go to Kiosk lock screen page')
def navigate_to_lock_screen():
    pass
    # kiosk_lock_screen_page.implicitly_wait(5)
    # kiosk_lock_screen_page.visit()


@when('Swipe to 30% of the kiosk screen and release')
def swipe_up_unlock_component(lock_screen_page: LockScreen):
    pass


@then("The screen should navigate to sign in screen")
def check_for_sign_in_screen(lock_screen_page: LockScreen):
    pass

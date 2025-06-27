@kiosk @signIn @Link(https://code.waters.com/bitbucket/projects/OSQ/repos/orionisppintegrationtests/browse/Kiosk/tests/UI/features/sign_in_screen_negative.feature)
Feature: Kiosk | SignIn Screen


  Background:
    Given Sign in page is displayed

  Scenario: The user signs in with incorrect pin and system should prompt "Incorrect Pin"
    When The 9078 is entered
    And  Tap the unlock button
    Then The system should prompt incorrect pin

  Scenario: The user signs in with incorrect pin, then deletes to remove error condition
    When The 9078 is entered
    And  Tap the unlock button
    And The system should prompt incorrect pin
    And User taps delete
    Then User verifies the entry field is not in error state

  Scenario: User when not entering pin, tap the unlock button, the system should prompt "Pin Required" error message
    When Tap the unlock button
    Then The system should prompt "Pin Required" error message


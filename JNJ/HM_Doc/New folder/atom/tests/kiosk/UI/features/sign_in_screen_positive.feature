@kiosk @signIn @Link(https://code.waters.com/bitbucket/projects/OSQ/repos/orionisppintegrationtests/browse/Kiosk/tests/UI/features/sign_in_screen_positive.feature)
Feature: Kiosk | SignIn Screen

  Background:
    Given Sign in page is displayed

  Scenario: User taps the delete button to remove entries, the contents in the pin entry field should be cleared
    When The 1234 is entered
    And User deletes the PIN entries
    Then Pin entry field must be empty


  Scenario: User when tap the "show"(eye) icon, the pin in the pin entry field is shown
    When The 1234 is entered
    And Tap the eye icon
    Then The screen should display/show the pin number entered


  Scenario: User when signs in with correct pin, should see the dashboard screen
    When The 1234 is entered
    And  Tap the unlock button
    Then The dashboard page is displayed


  Scenario: This is to test whether the sign in screen resets itself
    When The 1234 is entered
    And Tap the "BACK" button in the lock screen
    And Unlock the application
    Then Pin entry field must be empty


  Scenario: User when taps the "Back" button, navigates to the unlock screen
    When Tap the "BACK" button in the lock screen
    Then The Screen should transit to unlock screen

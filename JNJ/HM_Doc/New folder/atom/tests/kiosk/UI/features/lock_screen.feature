@kiosk
Feature: Kiosk | Lock Screen

  Scenario: To check the functionality of swipe up unlock button
    Given Go to Kiosk lock screen page
    When Swipe to 30% of the kiosk screen and release
    Then The screen should navigate to sign in screen

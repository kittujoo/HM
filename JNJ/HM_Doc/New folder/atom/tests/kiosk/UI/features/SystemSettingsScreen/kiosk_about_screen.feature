@kiosk @kiosk_about_screen_feature @ALIST-228
Feature: Kiosk | About Screen

    #prerequisite:Product model, product variant, serial number and software version installed on the instrument should be known
  Background:
    Given User navigates to the About screen

  @real @daily
  Scenario: To verify about information - software
    Then Software icon is selected
    And User validates the Software version is correctly displayed

  @real @weekly
  Scenario: To verify about information - hardware
    When User selects hardware icon
    Then User validates the Product model, product variant and serial number are correctly displayed

  @real @monthly
  Scenario: To verify about information - support
    When User selects support icon
    Then User validates the manufacturer, support website and QR code are correctly displayed

  @real @monthly @manual @ignore
  Scenario: To verify that QR code leads the user to the Waters Alliance iS support page
    When User selects support icon
    And User scans the QR code
    Then the Waters Alliance iS support page is opened

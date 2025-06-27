@kiosk @ALIST-228 @calibrateaxes
Feature: Kiosk | Calibrate Axes workflow functionality

         # ------------------- #
         # --- Z-Axis Path --- #
         # ------------------- #

  @real @weekly
  Scenario: To validate the screens and features within Z-Axis path
    Given User sets pre-required date and time format
    When User taps the calibrate axes start
    And User taps the Z-Axis path
    Then User validates the welcome screen
    When User Taps Next
    Then User validates the Cautions screen
    When User taps next to the summary screen
    And User taps the confirmation check
    Then Start becomes enable
    When User taps start
    Then User validates the test was completed
    And User validates the Z-Axis results screen details
    When User enters the log screen
    Then User verifies the Calibrate Z-Axis log is generated


  # -------------------- #
  # --- Zp-Axis Path --- #
  # -------------------- #

  @real @weekly
  Scenario: To validate the screens and features within Zp-Axis path
    Given User sets pre-required date and time format
    When User taps the calibrate axes start
    And User taps the Zp-Axis path
    Then User validates the welcome screen
    When User Taps Next
    Then User validates the Cautions screen
    When User taps next to the summary screen
    And User taps the confirmation check
    Then Start becomes enable
    When User taps start
    Then User validates the test was completed
    And User validates the Zp-Axis results screen details
    When User enters the log screen
    Then User verifies the Calibrate Zp-Axis log is generated


  # -------------------- #
  # --- Platter Path --- #
  # -------------------- #

  @weekly  @manual @ignore
  Scenario: To validate the screens and features within Platter path
    When User taps the calibrate axes start
    And User taps the Platter path
    Then User validates the welcome screen
    When User Taps Next
    Then User validates the Cautions screen
    When User taps next
    Then User validates the Power off screen
    And User validates Power off button is enable
    When User taps platter power off button
    Then User validates the platter powered off
    And User validates he is unable to continue

#    --------------------manual intervention --------------------

    When User taps the confirmation check for sample plates are removed and plate 1 is in position
    And User taps Next
    And taps the confirmation check for plate 1 is in position and the door is closed
    Then the Start button becomes enable
    When User taps start
    And User validates the test was completed
    Then User validates the Platter results screen details
    When User taps next
    And User validates he is unable to continue

#   -------------------- manual intervention--------------------

    And User taps the confirmation check for plate drawer is pushed and the door is closed
    Then The Next button is enable
    When User taps next
    Then User validates the test was completed



  # --------------------- #
  # --- B-0-Axes Path --- #
  # --------------------- #

  @weekly  @manual @ignore
  Scenario: To validate the screens and features within B-0 path
    When User taps the calibrate axes start
    And User taps the B-0-Axes path
    Then User validates the welcome screen
    When User Taps Next
    Then User validates the Cautions screen
    When User taps next
    And User taps the confirmation check for sample plates are removed and the door is closed
    Then the Start button becomes enable
    When User taps start
    Then User validates he is unable to continue

#    -------------------- manual intervention --------------------

    When User taps the confirmation check for Adaptor is installed and the door is closed
    Then the Start button becomes enable
    When User taps Next
    And taps the confirmation check for Adaptor is installed and the door is closed
    Then the Start button becomes enable
    When User taps start
    And User validates the test was completed
    Then User validates the B-0-Axes results screen details
    When User taps next
    And User validates he is unable to continue

#   -------------------- manual intervention --------------------
    And  User taps Home
    Then User validates the test was completed


  # ---------------------- #
  # --- Hard Stop Path --- #
  # ---------------------- #

  @real @weekly
  Scenario: To validate the screens and features within Hard stop path
    When User taps the calibrate axes start
    And User taps the Hard-Stop path
    Then User validates the welcome screen
    When User Taps Next
    Then User validates the Cautions screen
    When User taps next to the summary screen
    And User taps the confirmation check
    Then Start becomes enable
    When User taps start
    And User validates the test was completed
    Then User validates the Hard-Stop results screen details

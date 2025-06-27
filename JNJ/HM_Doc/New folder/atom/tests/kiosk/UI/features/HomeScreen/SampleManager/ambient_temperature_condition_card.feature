@kiosk @ALIST-228
Feature: Kiosk | Ambient temperature condition card

  Background:
    Given Navigate to the ambient temperature settings screen
    And User validate the information text

  @real @daily
  Scenario Outline:  To verify the condition card displays temperature within the tolerance set by the user
    When User sets the "<ambient_tolerance_temperature>" and "<tolerance_range>"
    And User confirms the settings
    Then User validates the display info for "<ambient_tolerance_temperature>" and "<tolerance_range>"

    Examples:
      | ambient_tolerance_temperature | tolerance_range |
      | 20.0                          | 5.0             |
      | 15.0                          | 10.0            |
      | 26.0                          | 5.0             |

  @real @daily
  Scenario Outline: To verify the temperature selected is displayed in the settings screen
    When User sets the "<ambient_tolerance_temperature>" and "<tolerance_range>"
    Then User validates the displayed "<ambient_tolerance_temperature>" and "<tolerance_range>" in the settings screen

    Examples:
      | ambient_tolerance_temperature | tolerance_range |
      | 20.0                          | 8.0             |
      | 26.0                          | 5.0             |    


  @real @daily
  Scenario Outline: To verify the ambient temperature and tolerance temperature are not updated when the user taps the cancel button
    When User sets the "<actual_ambient_temperature>" and "<tolerance_range>"
    Then User validates the displayed "<actual_ambient_temperature>" and "<tolerance_range>" in the settings screen
    When User confirms the settings
    And  Navigate to the ambient temperature settings screen
    And User sets the ambient temperature as "28.0" and tolerance range as "7.0"
    And User cancels the settings
    Then User validates the display info for "<actual_ambient_temperature>" and "<tolerance_range>"

    Examples:
      | actual_ambient_temperature | tolerance_range |
      | 19.0                       | 5.0             |
      | 21.0                       | 9.0             |

  @real @daily
  Scenario: User validate the default button sets the default temperature
    When User taps the default button
    Then User validate the temperature set to default

  @simulation @daily
  Scenario: When the toggle button is switched of, the picker is hidden
    When User turns off the toggle button
    Then Validate the spinner component is invisible

  @real @Manual  @ignore #TODO Can be done only at system level
  Scenario: To verify the system receives notification when notification toggle button is switched on
    # This scenario can be test only by simulating very high or low temperature in the instrument dashboard through
    # cmdmon

  @real @Manual  @ignore #TODO Can be done only at system level
  Scenario: To verify the system does not receives notification when notification toggle button is switched off
   # This scenario can be test only by simulating very high or low temperature in the instrument dashboard through
   # cmdmon

  @real @Manual  @ignore #TODO Can be done only at system level
  Scenario: To validate the progress bar is inactive when the censor in the instrument is not detected
   # This scenario can be test only by removing censor or simulating no censor detection from the firmware. This
   # can be test only at system level.

  @real @Manual  @ignore #TODO Can be done only at system level
  Scenario: When Ambient Temperature is Not Available, tapping the condition card will not bring the user to the secondary page, as there would be no settings available.
   # This scenario can be test only by removing censor or simulating no censor detection from the firmware. This
   # can be test only at system level.

  @real @Manual  @ignore #TODO Can be done only at system level
  Scenario: To validate the condition displays alert message when the censor detects temperature which is out of tolerance
   # This scenario can be test only by simulating very high or low temperature in the instrument dashboard through
   # cmdmon



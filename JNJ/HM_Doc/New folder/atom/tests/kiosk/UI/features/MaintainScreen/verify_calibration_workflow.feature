@kiosk @verify @workFlow @ALIST-228 @kiosk_verify_calibration_feature
Feature: Kiosk | Verify Calibration workflow functionality

  @real @weekly
  Scenario Outline: To validate verify calibration workflow when the flush options were selected

    Given User sets pre-required date and time format
    And User navigates to Commands area
    And User set the lamp detector "On"
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the verify calibration
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | True        | True            | 1.0       |
      | True        | True            | 0.1       |
      | True        | False           | 1.0       |
      | True        | False           | 0.1       |

  @real @weekly
  Scenario Outline: To validate verify calibration workflow when the flush options were selected and retry option is selected

    Given User sets pre-required date and time format
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the verify calibration
    Then User validates the calibration passes
    When User taps retry
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | True        | True            | 1.0       |

  @real @weekly
  Scenario Outline: To validate verify calibration workflow when the flush options were not selected

    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the verify calibration
    Then User validates the calibration passes if all three deviations are less than 1nm

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | False       | False           | 1.0       |


  @real @daily
  Scenario: To validate verify calibration workflow completes

    Given User sets pre-required date and time format
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "True" and pre flush column "True"
    And User sets the flowrate as "1.0"
    And User taps the next button
    And User validates the summary screen details for "True" and "True" for "1.0"
    And User starts the verify calibration
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details


  @real @weekly
  Scenario Outline: To validate verify calibration workflow when user abort it

    Given User sets pre-required date and time format
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User taps the start button
    And User stops the workflow at different "<stop_time>"
    Then User validates the status stopped for the verify calibration workflow
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate | stop_time |
      | True        | True            | 0.5       | 10        |
      | True        | True            | 0.5       | 600       |
      | True        | True            | 0.5       | 21        |
      | True        | False           | 0.5       | 10        |
      | True        | False           | 0.5       | 600       |

  @real @daily
  Scenario: To validate the workflow abort process completes

    Given User sets pre-required date and time format
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "True" and pre flush column "True"
    And User sets the flowrate as "0.5"
    And User taps the next button
    And User validates the summary screen details for "True" and "True" for "0.5"
    And User taps the start button
    And User stops the workflow at different "3"
    Then User validates the status stopped for the verify calibration workflow
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

  @real @weekly
  Scenario Outline: To validate the flow edit field

    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify calibration
    When User selects the verify calibration function
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    Then Validate the flow edit field shows "<error_state>"

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate | error_state |
      | True        | True            | 1.0       | False       |
      | True        | True            | 0.1       | False       |
      | True        | True            | 0.5       | False       |
      | True        | True            | 0.09      | True        |
      | True        | True            | 1.1       | True        |
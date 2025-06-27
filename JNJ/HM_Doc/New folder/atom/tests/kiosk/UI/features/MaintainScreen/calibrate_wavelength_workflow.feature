@kiosk @ALIST-228 @calibrate_wavelength
Feature: Kiosk | Calibrate wavelength workflow functionality

  @real @daily @ignore #(INSISPP-8104)
  Scenario Outline: To verify calibrate wavelength workflow when the flush options were/were not selected
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the calibration for the wavelength
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | False       | False           | 1.0       |


  @real @weekly  @ignore #(INSISPP-8104)
  Scenario Outline: To verify calibrate wavelength workflow
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the calibration for the wavelength
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | True        | True            | 1.0       |
      | True        | False           | 1.0       |


  @real @weekly  @ignore #(INSISPP-8104)
  Scenario Outline: To verify Retry button when the flush options were/were not selected
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the calibration for the wavelength
    Then User validates the calibration passes
    When User taps retry
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | False       | False           | 1.0       |


  @real @weekly  @ignore #(INSISPP-8104)
  Scenario Outline: To verify Retry button
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the calibration for the wavelength
    Then User validates the calibration passes
    When User taps retry
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | True        | True            | 1.0       |
      | True        | False           | 1.0       |


  @real @weekly  @ignore #The Last calibration field functionality is not implemented; need to be decided if it will/will not be implemented
  Scenario Outline: Verify Last calibration field
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the calibration for the wavelength
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User taps the Calibrate Detector button
    Then on the welcome screen the Last calibration on is updated with the current date

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | False       | False           | 1.0       |


  @real @weekly  @ignore #The Last calibration field functionality is not implemented; need to be decided if it will/will not be implemented
  Scenario Outline: Verify Last calibration field
    When User taps Calibrate Detector option
    Then User validates the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User starts the calibration for the wavelength
    Then User validates the calibration passes if all three deviations are less than 1nm
    When User taps the Calibrate Detector button
    Then on the welcome screen the Last calibration on is updated with the current date

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate |
      | True        | True            | 1.0       |
      | True        | False           | 1.0       |


  @real @weekly
  Scenario Outline: To validate the flow edit field

    When User taps Calibrate Detector option
    Then User validates the welcome screen
    And Validates the recommendation text for the calibrate workflow
    And Validates the better results point in the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    Then Validate the flow edit field shows "<error_state>"

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate | error_state |
      | True        | True            | 1.0       | False       |
      | True        | True            | 0.5       | False       |
      | True        | True            | 0.1       | False       |
      | True        | True            | 1.1       | True        |
      | True        | True            | 0.01      | True        |


  @real @weekly  @ignore #(INSISPP-8104)
  Scenario Outline: To validate the verify calibrate wavelength workflow when user abort it

    When User taps Calibrate Detector option
    Then User validates the welcome screen
    When User taps the next button
    Then User validates the preconditions for the verify wavelength
    When User selects the Calibrate Wavelengths option
    And User turns the flush column "<is_flush_on>" and pre flush column "<is_pre_flush_on>"
    And User sets the flowrate as "<flow_rate>"
    And User taps the next button
    And User validates the summary screen details for "<is_flush_on>" and "<is_pre_flush_on>" for "<flow_rate>"
    And User taps the start button
    And User stops the workflow at different "<stop_time>"
    Then User validates the status stopped for the verify wavelength workflow

    Examples:
      | is_flush_on | is_pre_flush_on | flow_rate | stop_time |
      | True        | True            | 0.5       | 10        |
      | True        | True            | 0.5       | 660       |
      | True        | True            | 0.5       | 1260      |
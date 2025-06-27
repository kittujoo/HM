@kiosk @ALIST-228 @pre_run_checks_settings_feature @weekly
Feature: Kiosk | Pre-run checks setting screen

  Background:
    When User navigates to system screen
    And User configures the solvent
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab

  @simulation
  Scenario Outline: To verify the toggle buttons default settings
    When User navigates to the Pre-run Checks tab
    Then User validates that the status of "<toggle>" is "<toggle_status>"

    Examples:
      | toggle                              | toggle_status |
      | eConnected Column must be installed | Enabled       |
      | eConnected Column must match method | Disabled      |
      | No pending performance maintenance  | Disabled      |
      | System is qualified                 | Disabled      |
      | Mobile phase is not expired         | Enabled       |
      | Sample Plates must be installed     | Enabled       |
      | Sample Plates must match method     | Disabled      |
      | All vials present                   | Disabled      |

  @simulation
  Scenario: To verify the Sample Plates toggle buttons dependency
    When User navigates to the Pre-run Checks tab
    And User disables the Sample Plates must be installed toggle button
    Then User validates the Sample Plates must match method toggle button is disabled and non-editable
    When User enables the Sample Plates must be installed toggle button
    Then User validates the Sample Plates must match method toggle button is not disabled and editable
    When User enables the Sample Plates must match method toggle button
    And User saves the data
    And User navigates to the Pre-run Checks tab
    Then User validates the Sample Plates data was correctly saved

  @simulation
  Scenario: To verify when changing but cancelling the pre-run toggles, they are not saving
    When User navigates to the Pre-run Checks tab
    And User enables all toggles buttons
    And User saves the data
    And User navigates to the Pre-run Checks tab
    And User disables all toggles buttons
    And User cancels the changes
    And User navigates to the Pre-run Checks tab
    Then User validates that all toggle buttons are enabled

  @real
  Scenario: To verify the eConnected Column toggle buttons dependency
    When User navigates to the Pre-run Checks tab
    And User disables the eConnected Column must be installed toggle button
    Then User validates the eConnected Column must match method toggle button is disabled and non-editable
    When User enables the eConnected Column must be installed toggle button
    Then User validates the eConnected Column must match method toggle button is not disabled and editable
    When User enables the eConnected Column must match method toggle button
    And User saves the data
    And User navigates to the Pre-run Checks tab
    Then User validates the eConnected Column data was correctly saved

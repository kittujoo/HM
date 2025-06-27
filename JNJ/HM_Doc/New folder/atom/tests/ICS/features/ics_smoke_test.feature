@ics_smoke_test
Feature: ICS smoke test

  Background:
    Given the "ics_atom_project" project is available in Empower

  @ics_special @ics_smoke_test_create_system
  Scenario: Creating a chromatographic system
    Given configuration manager application is open
    When a system is created
    Then the system is successfully brought online


  @ics @ics_smoke_test_run_sample_workflow @collect_message_center_log
  Scenario: Running a sample from scratch with default values
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And run samples application is open for the current project and system
    When a new sample set method is created
    And sample set method and dissolution types are selected
    And the standard injections location is selected
    And the sample description is defined
    And a method editor window is opened
    And a method is saved with the default values
    And the instrument method is selected
    And the standards identification is defined
    And the runtime option is selected
    And the set method summary is confirmed
    And the component editor is confirmed
    And the acquisition starts
    Then the sample set acquisition completes successfully

  @ics @ics_instrument_method_report
  Scenario: Generate Instrument Method report
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And run samples application is open for the current project and system
    When single injection tab is opened
    And a single injection configuration is set
    And an instrument method is created
    And a method editor window is opened
    And method editor data channels are turned on
    And an instrument method is saved and exported
    And the instrument method is selected
    And the preparation is completed
    And the single injection is completed
    And the report publisher system is opened
    And the report is selected
    And the Instrument Method report is saved
    And the Instrument Method report is exported as pdf file
    Then the Instrument Method report is validated

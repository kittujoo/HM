  """
  Validate association of instrument method with an instrument system

  """
@ics @real_or_simulation @monthly @ics_association_im_system_feature @new @ignore
Feature: ICS Association of Instrument Method with Instrument System

  Background:
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And Alliance iS driver version "1.2.0" is installed
    And Alliance iS systems are connected to Empower
      | systems |
      | 1.0.0   |
      | 1.1.0   |
      | 1.2.0   |


  Scenario Outline: Create acquisition method from project and run it when multiple systems are connected
    Given a project is open
    When a new method is created for system "<system_name>"
    And the method is configured as below
      | parameter          | value |
      | Sample temperature | 10    |
    And the method is saved
    And Run Samples for system "<system_name>" is opened
    Then Control Panel shows "IDLE" state
    When a sample set is configured for the created method
    And the acquisition starts
    Then the sample set acquisition completes with state "System Idle - Sample Set Complete"

    Examples:
      | system_name |
      | 1.0.0       |
      | 1.1.0       |
      | 1.2.0       |


  Scenario Outline: Create acquisition method from project and run it when multiple systems are connected
    Given a project is open
    When a new method is created without selecting a system
    Then an empty Method Editor is displayed
    When from the empty Method Editor the system "<system_name>" is selected
    And the method is configured as below
      | parameter          | value |
      | Sample temperature | 10    |
    And the method is saved
    And Run Samples for system "<system_name>" is opened
    Then Control Panel shows "IDLE" state
    When a sample set is configured for the created method
    And the acquisition starts
    Then the sample set acquisition completes with state "System Idle - Sample Set Complete"

    Examples:
      | system_name |
      | 1.0.0       |
      | 1.1.0       |
      | 1.2.0       |


  Scenario Outline: Create acquisition method from Run Samples and run it when multiple systems are connected
    Given Run Samples for system "<system_name>" is opened
    Then Control Panel shows "IDLE" state
    When Edit is used to create a new method for system "<system_name>"
    And the method is configured as below
      | parameter          | value |
      | Sample temperature | 10    |
    And the method is saved
    And a sample set is configured for the created method
    And the acquisition starts
    Then the sample set acquisition completes with state "System Idle - Sample Set Complete"

    Examples:
      | system_name |
      | 1.0.0       |
      | 1.1.0       |
      | 1.2.0       |

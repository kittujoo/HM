@kiosk @scanwavelengthWorkflow @workFlow @FCS
Feature: Kiosk | Noise & Drift Workflow functionality

  @data
  Scenario Outline: To validate the scan wavelength workflow using cuvettes delivery method

    Given User navigates to TUV section within health troubleshoot area
    When User taps the scan wavelength panel
    And  User validates the welcome context in the welcome screen
    And User selects the "<delivery_method>"
    And User validates the materials needed for "<delivery_method>"
    And User validates the preparation text
    And User confirms the preconditions
    And User sets the first flush with "<flow_rate>" and "<flush_duration>"
    And User selects for the solvent "<line>" for the first flush
    And User sets the second flush with "<flow_rate>" and "<flush_duration>"
    And User selects for the solvent "<line>" for the second flush
    And User sets the wavelength range "<min_wavelength>", "<maxi_wavelength>" and "<date_rate>"
    Then User validates the "<min_wavelength>", "<maxi_wavelength>" and "<date_rate>" in the summary screen

    Examples:
      | delivery_method | flow_rate | flush_duration | line | min_wavelength | maxi_wavelength | date_rate |
      | cuvettes        | 5.00      | 09:00          | C    | 192            | 265             | 10        |
      | cuvettes        | 5.00      | 09:00          | A    | 198            | 269             | 10        |


  Scenario Outline: To validate the scan wavelength workflow using flow cell delivery method

    Given User navigates to TUV section within health troubleshoot area
    When User taps the scan wavelength panel
    And  User validates the welcome context in the welcome screen
    And User selects the "<delivery_method>"
    And User validates the materials needed for "<delivery_method>"
    And User confirms the preconditions
    And User sets the first flush with "<flow_rate>" and "<flush_duration>"
    And User selects for the solvent "<line>" for the first flush
    And User sets the second flush with "<flow_rate>" and "<flush_duration>"
    And User selects for the solvent "<line>" for the second flush
    And User sets the wavelength range "<min_wavelength>", "<maxi_wavelength>" and "<date_rate>"
    Then User validates the "<min_wavelength>", "<maxi_wavelength>" and "<date_rate>" in the summary screen

    Examples:
      | delivery_method | flow_rate | flush_duration | line | min_wavelength | maxi_wavelength | date_rate |
      | flow_cell       | 10.00     | 09:00          | B    | 192            | 265             | 10        |
      | flow_cell       | 10.00     | 09:00          | D    | 198            | 269             | 10        |


  Scenario Outline: To validate the functionality of stepper component

    Given User navigates to TUV section within health troubleshoot area
    When User taps the scan wavelength panel
    And  User validates the welcome context in the welcome screen
    And User selects the "<delivery_method>"
    And User validates the materials needed for "<delivery_method>"
    And User confirms the preconditions
    And User validates the stepper icon when the "<flush_duration>" is set

    Examples:
      | delivery_method | flush_duration |
      | flow_cell       | 20:00          |
      | flow_cell       | 8:00           |


  Scenario Outline: To validate the reset icon sets the  stepper component to the default value

    Given User navigates to TUV section within health troubleshoot area
    When User taps the scan wavelength panel
    And  User validates the welcome context in the welcome screen
    And User selects the "<delivery_method>"
    And User validates the materials needed for "<delivery_method>"
    And User confirms the preconditions
    Then User validates the reset icon "<is_disable>" when the "<flush_duration>" is set

    Examples:
      | delivery_method | is_disable | flush_duration |
      | flow_cell       | False      | 9:00           |
      | flow_cell       | True       | 10:00          |
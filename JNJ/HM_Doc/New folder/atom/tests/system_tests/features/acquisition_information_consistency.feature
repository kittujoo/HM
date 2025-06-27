@system @ALIST-231 @acquisition_information_consistency_feature
Feature: System | Acquisition information consistency

  Background:
    Given the "predefined_data" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state

  @real_or_simulation @weekly @new @ignore
  Scenario: Single sample set with five lines injections
    When The sample name field "<Sample Name>" is entered
    And Inject Sample is selected rom the dropdown menu for function
    And Isocratic UV is selected from dropdown menu for method set
    And The plate position "<Plate>" is added
    And Injection volume of 2 ul is added
    And Run time of 2 minutes is added
    Then The acquisition is running
    And User validates in Kiosk Time Remaining in upper banner
    And User validates in kiosk the Current Injection is "<expected_current_injection>"
    And User validates in kiosk the Injection Remaining is "<expected_injection_remaining>"
    And User validates in kiosk the Injections Completed is "<expected_injection_completed>"
    And User validates in kiosk the Current Injection Time Remaining
      #Current Batch Time Remaining in Kiosk will always be 2 minutes faster compared with Sample St Time Remaining from Empower window #INSSYS-48
    And User validates in kiosk the Current Batch Time Remaining
    Then User validates in kiosk "<current_injection_location>"
    And User validates in kiosk Sample Identifier name match with sample name from Empower
    And User validates in kiosk Method Identifier name match with method name from Empower

      | Sample_Name | Plate | expected_current_injection | expected_injection_remaining | expected_injection_completed | current_injection_location |
      | SS01        | 1:A,1 | 1                          | 5                            | 0                            | 1:A,1                      |
      | SS02        | 1:A,2 | 2                          | 4                            | 1                            | 1:A,2                      |
      | SS03        | 1:A,3 | 3                          | 3                            | 2                            | 1:A,3                      |
      | SS04        | 1:A,4 | 4                          | 2                            | 3                            | 1:A,4                      |
      | SS05        | 1:A,5 | 5                          | 1                            | 4                            | 1:A,5                      |

  @real_or_simulation @daily @new @ignore
  Scenario Outline: Time: Single sample set with one injection
    When The sample name field "<Sample Name>" is entered
    And Inject Sample is selected from the dropdown menu for function
    And Isocratic UV is selected from dropdown menu for method set
    And The plate position "<Plate>" is added
    And Injection volume of "2 ul" is added
    And Run time of "2 minutes" is added
    Then The acquisition starts
    And User validates in Kiosk Time Remaining in upper banner
    And User validates in kiosk the Current Injection is "<expected_current_injection>"
    And User validates in kiosk the Injection Remaining is "<expected_injection_remaining>"
    And User validates in kiosk the Injections Completed is "<expected_injection_completed>"
    And User validates in kiosk the Current Injection Time Remaining
      #Current Batch Time Remaining in Kiosk will always be 2 minutes faster compared with with Sample St Time Remaining from Empower window #INSSYS-48
    And User validates in kiosk the Current Batch Time Remaining
    Then User validates in kiosk "<current_injection_location>"
    And User validates in kiosk Sample Identifier name match with sample name from Empower
    And User validates in kiosk Method Identifier name match with method name from Empower

    Examples:
      | Sample_Name | Plate | expected_current_injection | expected_injection_remaining | expected_injection_completed | current_injection_location |
      | Blank       | 1:A,1 | 1                          | 1                            | 0                            | 1:A,1                      |

  @real_or_simulation @weekly @new @ignore
  Scenario: Injections: Multiple sample sets - one sample set with 3 injections and another sample set with 3 injection in a queue
    Given Samples tab is selected
    And New line is added in sample set
    When the sample set is configured with the following data
      | Function       | Method Set   | Plate_Position | Inj_Vol | Number_of_Inj | Processing | Run_Time | Data_Start | Next_Inj_Delay | Sample_Weight | Dilution |
      | Inject Samples | isocratic UV | "<Position 1>" | 2       | 3             | Normal     | 3        | 0          | 0              | 1             | 1        |
    And The sample set is saved with name "<Sample_Set_Name>"
    And The acquisition starts
    Then User validates in Kiosk Time Remaining in upper banner
    And User validates in kiosk the Current Injection is "<expected_current_injection>"
    And User validates in kiosk the Injection Remaining is "<expected_injection_remaining>"
      #Injections Completed are reset to zero after current sample set has been completed
    And User validates in kiosk the Injections Completed is "<expected_injection_completed>"
    And User validates in kiosk the Current Injection Time Remaining
      #Current Batch Time Remaining in Kiosk will always be 2 minutes faster compared with with Sample St Time Remaining from Empower window #INSSYS-48
    And User validates in kiosk the Current Batch Time Remaining
    And User validates in kiosk "<current_injection_location>"
    And User validates in kiosk Sample Identifier name match with sample name from Empower
    And User validates in kiosk Method Identifier name match with method name from Empower

      | Sample_Set_Name | Plate | expected_current_injection | expected_injection_remaining | expected_injection_completed | current_injection_location |
      | SS_Run_1        | 1:A,1 | 1                          | 6                            | 0                            | 1:A,1                      |
      | SS_Run_2        | 1:A,2 | 1                          | 3                            | 0                            | 1:A,2                      |

@system @ALIST-231
Feature: System | Mobile Phase is not expired

  Background:
    Given the solvents line A,B,C and D are configured and an instrument method that include all four solvents is available

  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Mobile phase expired and the button is enabled
    Given Pre-Run Checks window is opened
    And Mobile Phase is not expired toggle button is enable
    And User configures the mobile phase expire for mobile phase A, B, C and D as "<phase_A_expire>", "<phase_B_expire>", "<phase_C_expire>" and "<phase_D_expire>"
    And user runs an aquisition
    Then user verifies the aquisition is not started
    And user verifies an error message is displayed
    And user is informed that the sample set execution failed
    And user is asked to open message center for details
    And users verifes in message center the "<inform>" message is displayed
    And user verifies in Console, aquisition the Mobile phase is not expired is ON

    Examples:
      | phase_A_exipre | phase_B_expire | phase_C_expire | phase_D_expire | inform                       |
      | Yes            | Yes            | Yes            | Yes            | Solvent exire Bottle 1,2,3,4 |
      | Yes            | No             | No             | No             | Solvent exire Bottle 1       |
      | No             | Yes            | No             | No             | Solvent exire Bottle 2       |
      | No             | No             | Yes            | No             | Solvent exire Bottle 3       |
      | No             | No             | No             | Yes            | Solvent exire Bottle 4       |
      | Yes            | Yes            | No             | No             | Solvent exire Bottle 1,2     |
      | Yes            | Yes            | Yes            | No             | Solvent exire Bottle 1,2,3   |


  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Mobile phase expired and the button is disabled
    Given Pre-Run Checks window is opened
    And Mobile Phase is not expired toggle button is disabled
    And User configures the mobile phase expire for mobile phase A, B, C and D as "<phase_A_expire>", "<phase_B_expire>", "<phase_C_expire>" and "<phase_D_expire>"
    And user runs an aquisition
    Then user verifies the aquisition is sucesfully completed
    And user verifies in Console, aquisition the Mobile phase is not expired is OFF

    Examples:
      | phase_A_exipre | phase_B_expire | phase_C_expire | phase_D_expire |
      | Yes            | Yes            | Yes            | Yes            |
      | Yes            | No             | No             | No             |
      | No             | Yes            | No             | No             |
      | No             | No             | Yes            | No             |
      | No             | No             | No             | Yes            |
      | Yes            | Yes            | No             | No             |
      | Yes            | Yes            | Yes            | No             |
@system @ALIST-231
Feature: System | Mobile Phase is low

    Background:
        Given the solvents line A,B,C and D are configured and an instrument method that include all four solvents is available

    @real_or_simulation @weekly @new @ignore
    Scenario Outline: Mobile phase is low and the button is enabled
        Given Run Time Checks window is opened
        And Mobile Phase is low toggle button is enable
        And User configures the mobile phase level for mobile phase A, B, C and D as "<phase_A_level>", "<phase_B_level>", "<phase_C_level>" and "<phase_D_level>"
        And user runs an aquisition
        Then user verifies the aquisition is not started
        And user verifies an error message is displayed
        And user is informed that the sample set execution failed
        And user is asked to open message center for details
        And users verifes in message center the "<inform>" message is displayed
        And user verifies in Console, aquisition the Mobile phase is low is ON

    Examples:
        | phase_A_level | phase_B_level | phase_C_level | phase_D_level | inform                              |
        | Empty         | Empty         | Empty         | Empty         | Solvent level is low Bottle 1,2,3,4 |
        | Empty         | 1/8           | 1/4           | 3/8           | Solvent level is low Bottle 1       |
        | 1/2           | Empty         | 5/8           | 3/4           | Solvent level is low Bottle 2       |
        | 7/8           | Full          | Empty         | 1/2           | Solvent level is low Bottle 3       |
        | 1/8           | 5/8           | Full          | Empty         | Solvent level is low Bottle  4      |
        | Empty         | Empty         | 1/2           | 1/2           | Solvent level is low Bottle 1,2     |
        | Empty         | Empty         | Empty         | 1/8           | Solvent level is low Bottle  1,2,3  |


    @real_or_simulation @weekly @new @ignore
    Scenario Outline: Mobile phase is low and the button is disabled
        Given Run Time Checks window is opened
        And Mobile Phase is low toggle button is disabled
        And User configures the mobile phase level for mobile phase A, B, C and D as "<phase_A_level>", "<phase_B_level>", "<phase_C_level>" and "<phase_D_level>"
        And user runs an aquisition
        Then user verifies the aquisition is sucesfully completed
        And user verifies in Console, aquisition the Mobile phase is low is OFF

    Examples:
        | phase_A_level | phase_B_level | phase_C_level | phase_D_level |
        | Empty         | Empty         | Empty         | Empty         |
        | Empty         | 1/8           | 1/4           | 3/8           |
        | 1/2           | Empty         | 5/8           | 3/4           |
        | 7/8           | Full          | Empty         | 1/2           |
        | 1/8           | 5/8           | Full          | Empty         |
        | Empty         | Empty         | 1/2           | 1/2           |
        | Empty         | Empty         | Empty         | 1/8           |

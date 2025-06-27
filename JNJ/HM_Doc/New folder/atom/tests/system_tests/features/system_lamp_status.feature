@system @ALIST-231
Feature: System | Lamp status

  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Lamp state is correctly updated across all applications when state is changed from Console
    Given Run Samples window is opened
    And Console is opened
    When user sets the status of the lamp to "<value>" in Console Commands window
    Then user confirms that the status of the lamp in Console Commands window is "<value>"
    And user confirms that the status of the lamp in Control Panel is "<value>"
    And user confirms that the status of the lamp in Kiosk homepage is "<value>"
    And user confirms that the status of the lamp in Kiosk TUV condition card is "<value>"
    And user confirms that the status of the lamp in Kiosk Commands is "<value>"

    Examples:
      | value |
      | ON    |
      | OFF   |

  @real_or_simulation @weekly @new @ignore
  Scenario: Lamp state is correctly updated across all applications when state is changed from Kiosk
    Given Run Samples window is opened
    And Console is opened
    When user sets the status of the lamp to "<value>"  in Kiosk Commands
    Then user confirms that the status of the lamp in Kiosk Comands window is "<value>"
    And user confirms that the status of the lamp in Kiosk homepage is "<value>"
    And user confirms that the status of the lamp in Kiosk TUV condition card is "<value>"
    And user confirms that the status of the lamp in Control Panel is "<value>"
    And user confirms that the status of the lamp in Console Comands window is "<value>"

    Examples:
      | value |
      | ON    |
      | OFF   |

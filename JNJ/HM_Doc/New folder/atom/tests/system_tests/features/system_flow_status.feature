@system @ALIST-231
Feature: System | Flow status

  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Flow state is correctly updated across all applications when it is changed from Console
    Given Run Samples window is opened
    And Console is opened
    When user sets the status of the flow to "<value>" in Console Commands window
    Then user confirms that the status of the flow in Console Commands window is "<value>"
    And user confirms that the status of the flow in Control Panel is "<value>"
    And user confirms that the status of the flow in Kiosk homepage is "<value>"
    And user confirms that the status of the flow in Kiosk Flow condition card is "<value>"
    And user confirms that the status of the flow in Kiosk Commands is "<value>"

    Examples:
      | value |
      | ON    |
      | OFF   |

  @real_or_simulation @weekly @new @ignore
  Scenario: Flow state is correctly updated across all applications when it is changed from Kiosk
    Given Run Samples window is opened
    And Console is opened
    When user sets the status of the flow to "<value>" in Kiosk Commands
    Then user confirms that the status of the flow in Kiosk Commands window is "<value>"
    And user confirms that the status of the flow in Kiosk homepage is "<value>"
    And user confirms that the status of the flow in Kiosk Flow condition card is "<value>"
    And user confirms that the status of the flow in Control Panel is "<value>"
    And user confirms that the status of the flow in Console Commands window is "<value>"

    Examples:
      | value |
      | ON    |
      | OFF   |
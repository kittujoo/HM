@system @ALIST-231 @system_column_temperature_consistency_feature
Feature: System | Column Temperature Consistency

  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Column temperature value is correctly updated across all applications when it is set from Kiosk app.
    Given User navigates to the column temperature settings screen
    When User sets the value of the Column Temperature to "<column_value>"
    Then User confirms that the Column Temperature value in Kiosk column temperature condition card is "<column_value>"
    And User confirms that the Column Temperature value in Kiosk homepage is "<column_value>"
    And User confirms that the Column Temperature value in Control Panel is "<control_panel_value>"
    And User confirms that the Column Temperature value in Console is "<column_value>"

    Examples:
      | column_value | control_panel_value |
      | 35           | 35                  |
      | OFF          | ambient temp        |


  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Column temperature value is correctly updated across all applications when it is set in Instrument method
    Given Instrument method is created with column temperature "<column_value>"
    And Instrument method is saved with name "<instrument_method>"
    And Run samples application is open for the current project and system
    And Entry from dropdown instrument method is selected "<instrument_method>"
    When Setup run section is selected
    And Setup finishes successfully
    Then User confirms that the Column Temperature value in Kiosk column temperature condition card is "<column_value>"
    And User confirms that the Column Temperature value in Kiosk homepage is "<column_value>"
    And User confirms that the Column Temperature value in Control Panel is "<control_panel_column_value>"
    And User confirms that the Column Temperature value in Console is "<column_value>"

    Examples:
      | column_value | control_panel_column_value | instrument_method        |
      | 20           | 20                         | Column temperature value |
      | OFF          | ambient temp               | Column off               |
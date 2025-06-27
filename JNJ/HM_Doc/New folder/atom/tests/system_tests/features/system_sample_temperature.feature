@system @ALIST-231 @system_sample_temperature_consistency_feature
Feature: System | Sample Temperature Consistency

  @real_or_simulation @weekly @quarantine @defect:INSISPP-8261 @new @ignore
  Scenario Outline: Sample temperature value correctly updated on all applications when set on Kiosk app
    Given Navigate to the sample temperature settings screen
    When User sets the value of the Sample Temperature to "<sample_value>"
    Then User confirms that the Sample Temperature value in Kiosk sample manager condition card is "<sample_value>"
    And User confirms that the Sample Temperature value in Kiosk homepage is "<sample_value>"
    And User confirms that the Sample Temperature value in Control Panel is "<control_panel_value>"
    And User confirms that the Sample Temperature value in Console is "<sample_value>"

    Examples:
      | sample_value | control_panel_value |
      | 10           | 10                  |
      | OFF          | ambient temp        |


  @real_or_simulation @weekly @quarantine @defect:INSISPP-8261 @new @ignore
  Scenario Outline: Sample temperature value is correctly updated across all applications when it is set in Instrument method
    Given Instrument method is created with sample temperature parameter "<sample_value>"
    And Instrument method is saved with name "<instrument_method>"
    And Run samples application is open for the current project and system
    And "<instrument_method>" entry is selected from Instrument Method dropdown
    When Setup run section is selected
    And Setup finishes successfully
    Then User confirms that the Sample Temperature value in Kiosk sample manager condition card is "<sample_value>"
    And User confirms that the Sample Temperature value in Kiosk homepage is "<sample_value>"
    And User confirms that the Sample Temperature value in Control Panel is "<control_panel_sample_value>"
    And User confirms that the Sample Temperature value in Console is "<sample_value>"

    Examples:
      | sample_value | control_panel_sample_value | instrument_method        |
      | 20           | 20                         | Sample temperature value |
      | OFF          | ambient temp               | Sample off               |

@kiosk @ALIST-228 @kiosk_plots_screen_feature
Feature: Kiosk | Plots screen feature

  Background:
    Given User turns off all the enabled plots

  @simulation @daily
  Scenario Outline: To verify user able to navigate to plot screen and select different time window

    When User taps the settings icon
    And User change the time range to "<time_window>" in the settings screen
    And User selects the "First" plot to display "Ambient Temperature (°C)" in "Orange" for "alphabetic order"
    And The user confirms the time window selection
    And User play the plots
    Then User validates the plots showing for the selected time "<expected_time_window>"

    Examples:
      | time_window | expected_time_window |
      | Fifteen     | -15.0                |
      | Custom      | -60.0                |
      | Five        | -5.0                 |

  @simulation @daily
  Scenario Outline: To verify the visibility of time window wheel in settings screen

    When User taps the settings icon
    And User change the time range to "<time_window>" in the settings screen
    Then User validate the visibility of time wheel scroll component "<is_wheel_present>"
    And The user confirms the time window selection

    Examples:
      | time_window | is_wheel_present |
      | Fifteen     | False            |
      | Five        | False            |
      | Custom      | True             |

  @simulation @daily
  Scenario Outline: To verify the time range selected in settings screen is updated in the plots screen

    When User taps the settings icon
    And User change the time range to "<time_window>" in the settings screen
    And User selects the "First" plot to display "Ambient Temperature (°C)" in "Orange" for "alphabetic order"
    And The user confirms the time window selection
    When User pause the plots to change the settings
    Then User play the plots
    And User validates the plots showing for the selected time "<expected_time_window>"

    Examples:
      | time_window | expected_time_window |
      | Fifteen     | -15.0                |
      | Five        | -5.0                 |
      | Custom      | -60.0                |


  @real @daily @quarantine @defect:INSISPP-8395
  Scenario Outline: To verify the time range selected using more action icons is updated in the plots screen

    When User taps the settings icon
    And User change the time range to "<time_window>" in the settings screen
    And User selects the "<plot_number>" plot to display "Column Temperature (°C)" in "Red" for "alphabetic order"
    And The user confirms the time window selection
    And User play the plots
    And User taps the plot screen
    And User taps the settings icon of the plot "<plot_number>"
    And User change the time range to "<time_window>" in the settings screen
    And The user confirms the time window selection
    Then Validate the given time window option is selected as "<time_window>"
    And User play the plots
    And User validates the plots showing for the selected time "-15.0"

    Examples:
      | time_window | plot_number |
      | Fifteen     | First       |

  @real @daily
  Scenario Outline: To verify custom value selected using wheel component is updated in the slider component

    When User taps the settings icon
    And User change the time range to "<time_window>" in the settings screen
    Then User validate the visibility of time wheel scroll component "<is_wheel_present>"
    When User selects the "3" "Two" from the time wheel component
    Then User validates the custom time "3 h 2 min" in the selector component
    And User validates the "<time_window>" text is "<is_text_shown>"
    When User selects the "First" plot to display "Sample Pressure (psi)" in "Green" for "alphabetic order"
    And The user confirms the time window selection
    And User play the plots
    Then User validates the plots showing for the selected time "-182.0"

    Examples:
      | time_window | is_wheel_present  | is_text_shown |
      | Custom      | True              | True          |

  @real @weekly @quarantine @defect:ALIST-319
  Scenario Outline: To validate the coordination of play button in plots and settings screen when user pause the plots

    When User taps the settings icon
    And User selects the "First" plot to display "Composition D (%)" in "Orange" for "alphabetic order"
    And The user confirms the time window selection
    And User play the plots
    And User pause the plots to change the settings
    And User taps the plot screen
    Then Validate the play button is displayed "True" for settings screen
    And User taps the play-pause centre button
    And Validate the play button is displayed "<plot_screen_bool_value>" for settings screen
    And User Validate the play button is displayed "<plot_screen_bool_value>" in the plots screen

    Examples:
      | plot_screen_bool_value |
      | False                  |

  @real @weekly @quarantine @defect:ALIST-319
  Scenario Outline: To validate the coordination of play button in plots and settings screen when user plays the plots
    When User taps the settings icon
    And User selects the "Second" plot to display "Degasser Pressure (psi)" in "Pink" for "alphabetic order"
    And The user confirms the time window selection
    And User play the plots
    And User taps the plot screen
    Then Validate the play button is displayed "False" for settings screen
    And User taps the play-pause centre button
    And Validate the play button is displayed "<plot_screen_bool_value>" for settings screen
    And User Validate the play button is displayed "<plot_screen_bool_value>" in the plots screen

    Examples:
      | plot_screen_bool_value |
      | True                   |

  @real @weekly
  Scenario: To verify the 4 charts displayed in the plots hub screen

    When User taps the settings icon
    And User selects the "First" plot to display "Primary Leak Rate (nL/min)" in "Red" for "alphabetic order"
    And User selects the "Second" plot to display "Flow Rate (mL/Min)" in "Orange" for "alphabetic order"
    And User selects the "Third" plot to display "Primary Pressure (psi)" in "Pink" for "alphabetic order"
    And User selects the "Fourth" plot to display "Composition A (%)" in "Blue" for "alphabetic order"
    And The user confirms the time window selection
    Then User validates the plots displayed in the plot hub screen

  @real @weekly
  Scenario: To validate 3 charts are displayed in the plots hub

    When User taps the settings icon
    And User selects the "First" plot to display "Composition A (%)" in "Blue" for "alphabetic order"
    And User selects the "Second" plot to display "Composition B (%)" in "Green" for "alphabetic order"
    And User selects the "Third" plot to display "Composition C (%)" in "Pink" for "alphabetic order"
    And The user confirms the time window selection
    Then User validates the plots displayed in the plot hub screen

  @real @weekly
  Scenario: To validate 2 charts are displayed in the plots hub

    When User taps the settings icon
    And User selects the "First" plot to display "Degasser Pressure (psi)" in "Blue" for "alphabetic order"
    And User selects the "Second" plot to display "System Pressure (psi)" in "Green" for "alphabetic order"
    And The user confirms the time window selection
    Then User validates the plots displayed in the plot hub screen

  @real @weekly
  Scenario: To validate 1 chart are displayed in the plots hub

    When User taps the settings icon
    And User selects the "First" plot to display "Composition D (%)" in "Blue" for "alphabetic order"
    And The user confirms the time window selection
    Then User validates the plots displayed in the plot hub screen


            ### The below scenarios are as of now invalid as the more icon is removed from the screen
            ### but keeping the below scenario just in case can be used is the more icon is implemented again
  @ignore  #This more icon is removed from the screen, this scenario is not valid
  Scenario: The extended more action icon retracts when user tap taps on other more action icon

    When User pause the plots to change the settings
    And user taps the plot First more action icon
    Then User validate the only plot First more action icon is extended
    And user taps the plot Second more action icon
    And User validate the only plot First more action icon is extended


  @ignore  #This more icon is removed from the screen, this scenario is not valid
  Scenario: The extended more action retracts when the user taps on any part of the plots

    When User pause the plots to change the settings
    And user taps the plot Second more action icon
    Then User validate the only plot Second more action icon is extended
    And User taps on plot title text
    And validate all the plots more action icons are retracted


  @ignore  #This more icon is removed from the screen, this scenario is not valid
  Scenario: The extended more action retracts when the user taps on any navigation icon

    When User pause the plots to change the settings
    And user taps the plot Third more action icon
    Then User validate the only plot Third more action icon is extended
    And User taps on navigation home in the dashboard screen
    And User taps on navigation plots in the dashboard screen
    And validate all the plots more action icons are retracted
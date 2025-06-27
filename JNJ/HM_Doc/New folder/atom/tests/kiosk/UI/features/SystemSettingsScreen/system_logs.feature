@kiosk @kiosk_system_logs_feature @ALIST-228
Feature: Kiosk | System logs screen


  @simulation @weekly
  Scenario: To verify Next and Back buttons in logs screen
    Given User sets pre-required date and time format
    When User is at the system logs screen
    Then User validates the log entries are displayed in reverse chronological order
    And User validates the error logs are color coded in red
    When User press the Next button
    Then User validates the page "2" log entries are displayed
    When User keeps the scroll down
    And User press the Back button
    Then User validates the page "1" logs are displayed and the scroll is up


  @real @weekly
  Scenario Outline: To verify simple filters in system logs screen
    Given User sets pre-required date and time format
    When User is at the system logs screen
    Then User validates the log entries are displayed in reverse chronological order
    When User taps the filter icon
    And User swaps the data range filter to "<date_range_option>"
    And User swaps the simple filter to "<content_filter_option>"
    And User confirms the settings
    Then User validates the simple filter was applied and logs are filtered
    When User taps the filter icon
    Then User validates the "<date_range_option>" and "<content_filter_option>" are displayed

    Examples:
      | date_range_option | content_filter_option |
      | 1 Week            | All                   |
      | 1 Month           | Errors                |
      | All               | Warnings              |
      | All               | Information           |


  @simulation @weekly
  Scenario Outline: To verify when changing the filters but cancelling the data is not saved
    When User is at the system logs screen
    Then User validates the log entries are displayed in reverse chronological order
    When User taps the filter icon
    And User swaps the data range filter to "<default_range>"
    And User swaps the simple filter to "<default_filter>"
    And User confirms the settings
    And User taps the filter icon
    And User swaps the data range filter to "<date_range_option>"
    And User swaps the simple filter to "<content_filter_option>"
    And User cancels the change
    And User taps the filter icon
    Then User validates the "<default_range>" and "<default_filter>" are displayed


    Examples:
      | date_range_option | content_filter_option | default_range | default_filter |
      | 1 Week            | All                   | All           | All            |
      | 1 Month           | Errors                | All           | All            |
      | All               | Warnings              | All           | All            |
      | All               | Information           | All           | All            |


  @simulation @weekly
  Scenario Outline: To verify add entry feature in system logs screen
    When User is at the system logs screen
    Then User validates the log entries are displayed in reverse chronological order
    When User taps add entry icon
    And User enters any "<log_note>" and confirms the log entry
    Then User verifies new log entry is created with current date time, category and source


    Examples:
      | log_note         |
      | test123          |
      | P@th. find, 3r   |
      | KIOSKAPP         |
      | 12345            |
      | KIOSK1234%%kiosk |
      | ...456...        |
      | 234:890:456      |


  @simulation @weekly
  Scenario Outline: To verify add entry with more than 100 characters feature in system logs screen are not allowed
    When User is at the system logs screen
    Then User validates the log entries are displayed in reverse chronological order
    When User taps add entry icon
    And User enters "<log_note>"
    Then User validates that maximum 100 characters can be defined
    When User confirms the change
    Then User verifies new log entry is created with current date time, category and source

    Examples:
      | log_note                                                                                                      |
      | Each logged item shall include an optional detailed description. The log item detail view shall be displayed. |


  @simulation @weekly
  Scenario Outline: To verify when adding an entry but cancelling the data is not saved
    Given User sets pre-required date and time format
    When User is at the system logs screen
    And Last log details are stored
    And User taps add entry icon
    And User enters "<log_note>"
    And User cancels the change
    Then User validates the new entry is not added in the entry logs

    Examples:
      | log_note       |
      | test123        |
      | P@th. find, 3r |

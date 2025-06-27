@kiosk @ALIST-228 @kiosk_dashboard_screen_feature
Feature: Kiosk | Dash board screen

  @simulation @weekly
  Scenario Outline: To validate only one icon is highlighted in the left navigation panel at a time
    When The user taps the "<first_icon_selected>" icon
    And The user taps the "<second_icon_selected>" icon
    Then The "<first_icon_selected>" should not be highlighted
    And The "<second_icon_selected>" should be highlighted

    Examples:
      | first_icon_selected | second_icon_selected |
      | home                | setup                |
      | setup               | plots                |
      | plots               | maintain             |
      | maintain            | health               |
      | health              | system               |
      | system              | commands             |
      | commands            | home                 |


  @simulation @weekly
  Scenario Outline: To validate only left panel  icon is highlighted when the user navigates back to dashboard page from the user settings icon
    When The user taps the "<first_icon_selected>" icon
    And The user taps on the user settings icon
    And The user cancels the settings
    Then The "user_settings" should not be highlighted
    And The "<expected_icon>" should be highlighted

    Examples:
      | first_icon_selected | expected_icon |
      | home                | home          |
      | setup               | setup         |
      | plots               | plots         |
      | maintain            | maintain      |
      | health              | health        |
      | system              | system        |
      | commands            | commands      |


  @kiosk_access
  Scenario: User can access the system
    Then the dashboard home page is displayed
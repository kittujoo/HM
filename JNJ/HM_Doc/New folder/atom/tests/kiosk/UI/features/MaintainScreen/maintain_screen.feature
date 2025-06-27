@kiosk @maintainScreen
Feature: Kiosk | Maintain Screen functionality

  #TODO: All current scenarios will need more functionality once each screen has been developed

  Scenario Outline: To reach the replace screen
    When User taps the "<navigation_panel>"
    Then User cancels the changes

    Examples:
      | navigation_panel |
      | replace          |

  Scenario Outline: To reach the calibrate screen
    When User taps the "<navigation_panel>"
    Then User cancels the changes

    Examples:
      | navigation_panel |
      | calibrate        |

  Scenario Outline: To reach the service screen
    When User taps the "<navigation_panel>"
    Then User cancels the changes

    Examples:
      | navigation_panel |
      | service          |
@kiosk @ALIST-228 @leak_sensors_feature
Feature: Kiosk | Leak sensors settings screen
  # the system level testing FF should be added: details on https://code.waters.com/confluence/display/TER/TER-145+Leak+Detection

  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF sm leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    When User toggles the SM leak sensor to <expected_state>
    And User navigates to the configuration settings screen
    Then User validates the SM configure leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |

  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF sm leak sensor from module configuration tab
    Given User navigates to the SM configuration settings screen
    When  User toggles SM configure leak sensor to <expected_state>
    And   User navigates to the leak sensors screen
    Then  User validates the SM leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |


  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF TUV leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    When User toggles the TUV leak sensor to <expected_state>
    And User navigates to the configuration settings screen
    Then User validates the TUV configure leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |

  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF TUV leak sensor from module configuration tab
    Given User navigates to the TUV configuration settings screen
    When  User toggles TUV configure leak sensor to <expected_state>
    And   User navigates to the leak sensors screen
    Then  User validates the TUV leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |


  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF Column leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    When User toggles the Column leak sensor to <expected_state>
    And User navigates to the configuration settings screen
    Then User validats the Column configure leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |

  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF Column leak sensor from module configuration tab
    Given User navigates to the Column configuration settings screen
    When  User toggles Column configure leak sensor to <expected_state>
    And   User navigates to the leak sensors screen
    Then  User validates the Column leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |

  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF pump leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    When User toggles the pump leak sensor to <expected_state>
    And User navigates to the configuration settings screen
    Then User validates the pump configure leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |

  @real @weekly @new
  Scenario Outline: To verify turning ON/OFF pump leak sensor from module configuration tab
    Given User navigates to the pump configuration settings screen
    When  User toggles Column configure leak sensor to <expected_state>
    And   User navigates to the leak sensors screen
    Then  User validates the pump leak sensor state is <expected_state>

    Examples:
      | expected_state |
      | ON             |
      | OFF            |


  @simulation @weekly @new
  Scenario Outline: To verify when changing but cancelling the leak sensor toggles, they are not saving
    When User navigates to the leak sensors screen
    And  User switches the config toggle to OFF for <sensor>
    And User cancels the change
    And User navigates to the leak sensors screen
    Then User validates the <expected_config_toggle> change was not saved


    Examples:
      | sensor | config_toggle | expected_config_toggle_state |
      | pump   | OFF           | ON                           |
      | Column | OFF           | ON                           |
      | TUV    | OFF           | ON                           |
      | SM     | OFF           | ON                           |


  @manual @monthly @new
  Scenario Outline: To verify if sensor is disconnected, the user cannot enable nor disable the sensor
    When User navigates to the leak sensors screen
    And  User disconnects the <sensor>
    Then System is showing a leak sensor is not present
    And The user cannot enable nor disable the sensor
    And The <sensor> is red color coded

    Examples:
      | sensor |
      | pump   |
      | Column |
      | TUV    |
      | SM     |


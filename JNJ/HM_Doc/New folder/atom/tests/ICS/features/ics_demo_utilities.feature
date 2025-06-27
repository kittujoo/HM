  """
Feature to demonstrate some utility scripts. It should be removed once the mechanism is used in real scenarios
  """

@ics_demo_utility
Feature: ICS Demo Utility

  @network_card_demo
  Scenario: Disable and enable second network card on Windows OS
    Given the current configuration contain network card "Ethernet1"
    When disable the "Ethernet1" network card
    Then the "Ethernet1" is disabled
    When enable the "Ethernet1" network card
    Then the "Ethernet1" is enabled

  @clock_change_demo
  Scenario: Clock change on Windows OS
    Given the current clock time is saved
    When change the clock by add one hour and five minutes
    Then the new system time is updated with plus one hour and five minutes
    When sleep ten seconds
    And change the clock by subtract one hour and five minutes
    Then the new system time is updated with minus one hour and five minutes

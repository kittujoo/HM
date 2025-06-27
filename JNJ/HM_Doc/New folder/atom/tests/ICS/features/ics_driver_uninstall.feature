  """
  __documentation__ = "https://code.waters.com/confluence/pages/viewpage.action?spaceKey=OIS&title=Things+to+verify+on+ICS+installation"

  """

@ics_special @ALIST-229 @daily @real_or_simulation @ics_driver_uninstall_feature
Feature: ICS driver uninstall

  Scenario: Uninstallation of the ICS software
    Given the driver is already installed
    When the uninstaller is executed
    Then the 'Alliance iS System Setup' page is displayed
    And the page contians "Repair" button
    And the page contians "Uninstall" button
    And the page contians "Close" button
    When 'Uninstall' button is pressed
    Then the page contains "Setup progress"
    And the page contains "Processing:"
    And the page contians "Cancel" button
    And the page contains "Uninstall Successfully Completed"
    When 'Close' button is pressed
    Then the "Alliance iS System Setup" window is closed
    And the software should be completely removed from my machine

  @uninstall_if_present
  Scenario: Control panel
    When the user checks the control pannel programs and features list
    Then the user should not have 'Alliance iS System Setup' entry

  @uninstall_if_present
  Scenario: Registry entries
    When the user checks the registry entries for the installed software
    Then the user should not have the following registry keys:
      | Registry Key                                                             |
      | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Waters\Instruments\\Alliance iS  |
      | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Waters\Instruments\\Orion        |
      | HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Waters\Instruments\\Setup\\Orion |

  @uninstall_if_present
  Scenario: Alliance iS running services
    When the user checks the running services for the installed software
    Then the user should not have the following services running:
      | Service name                 |
      | Waters DHCP Server           |
      | WatersNGINXInstrumentService |

  @uninstall_if_present
  Scenario: Method editor files
    When the user checks the 'Method editor' folder for the installed software
    Then the files should not be present

  @uninstall_if_present
  Scenario: Report template files
    When the user checks the 'Template report' folder files
    Then the files should not be present

  @uninstall_if_present
  Scenario: Installation files
    When the user checks the 'ICS' folder for the installed software
    Then the files should not be present

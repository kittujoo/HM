  """
  Prerequisites: Microsoft UAC (User Account Control) needs to be set to "Never notify"
  __documentation__ = "https://code.waters.com/confluence/pages/viewpage.action?spaceKey=OIS&title=Things+to+verify+on+ICS+installation"
  """

@ics @ALIST-229 @daily @real_or_simulation @ics_driver_install_verification_feature
Feature: ICS driver installation verification

  Background:
    Given the driver is already installed

  @ics_services
  Scenario: Alliance iS running services
    Then the user should identify the following services running:
      | Service name                 |
      | Waters DHCP Server           |
      | WatersNGINXInstrumentService |

  Scenario: Alliance iS files
    Then the user should identify the following files present on the system:
      | File                                                          |
      | %empower%\Instruments\HTML\Orion\orion-method-editor          |
      | %empower%\Instruments\Log\OrionICS\Trace.txt                  |
      | %empower%\Instruments\Log\OrionICS\Information.txt            |
      | %empower%\Instruments\Log\OrionICS\NGNIXInstrumentService.txt |


  Scenario: Alliance iS in the registries
    Then the user should identify the "Alliance iS" instrument in the registries
    And the user should identify the following registry values:
      | Registry Key                                                             | Registry Name | Registry Data             |
      | SOFTWARE\\WOW6432Node\\Waters\\Instruments                               | HTMLDirectory | Empower\Instruments\HTML  |
      | SOFTWARE\\WOW6432Node\\Waters\\Instruments                               | NGINXPath     | Empower\Instruments\Nginx |
      | SOFTWARE\\WOW6432Node\\Waters\\Instruments\\InstrumentNames\\Alliance iS |               | =Alliance iS              |
      | SOFTWARE\\WOW6432Node\\Waters\\Instruments\\Setup\\Orion                 | Version       |                           |


      # Future ICS test scenarios

      # @pytest.mark.order(1) @uninstall_if_present
      # Scenario: Installation of the ICS software
      #     Given the installer is available
      #     When the installer is executed
      #     Then the 'Alliance iS System Setup' page is displayed
      #     And the page contians "Options" button
      #     And the page contians "Install" button
      #     And the page contians "Close" button
      #     And the page contians "I agree to the license terms and conitions" check box
      #     When license terms and conditions are checked
      #     And 'Install' button is pressed
      #     Then the page contains "Setup progress"
      #     And the page contains "Processing:"
      #     And the page contians "Cancel" button
      #     And the page contains "Installation Successfully Completed"
      #     When 'Close' button is pressed
      #     Then the "Alliance iS System Setup" window is closed

      # Scenario: NGINX instrument service
      #     Given the driver is already installed
      #     When the user checks the NGINX web server task list
      #     Then the user should identify two console sessions running
      #     And the following file 'Instruments\Nginx\conf\instruments\instruments.conf' exists

      # Scenario: NGINX configuration files
      #     Given the driver is already installed
      #     When the user checks the 'NGINX configuration' files for the installed software
      #     Then the user should identify the following files present on the system:
      #       | NGINX configuration files                                           |
      #       | %empower%\\Instruments\\Ngnix\\conf\\instruments\\instruments.conf  |

      # Scenario: NGINX instrument functionality check
      #     Given the driver is already installed
      #     When the user has access to the instrument
      #     Then the user should identify the following subsystems:
      #       | Subsystems of Alliance iS Link                                                                      |
      #       | Console http://%instrumentdomain%:80/AllianceiSAlliance-system-v9-CCH1/console-app/?dn='ICS'        |
      #       | Control Panel http://%instrumentdomain%/AllianceiSAlliance-system-v9-CCH1/control-panel-app/home    |
      #       | iSymRest http://%instrumentdomain%/AllianceiSAlliance-system-v9-CCH1/iSymRest                       |

      # Scenario: Control pannel
      #     Given the driver is already installed
      #     When the user checks the control pannel programs and features list
      #     Then the user should identify 'Alliance iS System Setup' entry

      # Scenario: Upgrade installation of the ICS software
      #     Given the driver is already installed
      #     And a new version of the software is available
      #     When the user runs the installer executable file for the new version
      #     Then the installer wizard should start
      #     And it should guide the user through the upgrade installation process
      #     And the upgrade installation should complete successfully

      # Checksum scenarios TBD
      # Scenario: Method editor files
      #     Given the driver is already installed
      #     When the user checks the 'Method editor' folder checksum for the installed software
      #     Then the user should have the correct checksum calculation

      # Checksum scenarios TBD
      # Scenario: Report template files
      #     Given the driver is already installed
      #     When the user checks the 'Template report' folder files
      #     Then the user should have the correct checksum calculation

      # Checksum scenarios TBD
      # Scenario: Installation files
      #     Given the driver is already installed
      #     When the user checks the 'ICS' folder checksum for the installed software
      #     Then the user should have the correct checksum calculation

@ICS @ALIST-258 @simulation @daily @configuration_report_feature
Feature: ICS | Configuration report
  The configuration report can be saved
  The report contains the corect values

  Background:
    Given an instrument configuration is done in Empower
    And a report method configured with System Information is available
    And a previously run injection exists

  Scenario: The report can be printed in pdf
    Given the Empower browse samples menu is open
    When a previously run sample is reported using the System information Report method
    Then the report can be saved

  Scenario: The report contains the correct labels
    Given a report is saved
    When the report is opened
    Then the report contains the following sections
      | Section                    |
      | System information         |
      | General information        |
      | System name                |
      | System comments            |
      | Node                       |
      | System create date         |
      | Instrument: Alliance iS    |
      | Type                       |
      | Address                    |
      | Ok ?                       |
      | Modules                    |
      | Serial number              |
      | Last Serviced              |
      | Next Service due           |
      | Prom Version               |
      | Comments                   |
      | Details                    |
      | Optional Pump Head         |
      | Manufacturer               |
      | Purchase Order #           |
      | Owners Equip #             |
      | Location                   |
      | Operators Guide            |
      | Detector Cell Size         |
      | Installation Start         |
      | Site OK?                   |
      | Installation materials OK? |
      | Electrical OK?             |
      | Fluidic OK?                |

  Scenario: The report contains the correct values in the general information
    Given the system has the following settings configured
      | Setting         |
      | System Name     |
      | System comments |
      | Node            |

    When the report is saved
    And the report is closed and opened
    Then the report contains the following settings matched
      | Setting         |
      | System Name     |
      | System comments |
      | Node            |

    And the System Create Date is the date when the system was configured in Empower

      ### The numbers in the table section are examples only and the values are dependant on the build being used  for testing ###
      ### The instrument values should be taken from the instrument and verified they are the right ones ###
      # the manufacturer information is a static field and this is unlikely to change #

  Scenario: The reported Details section contains the correctly reported subsections and the reported manufacturer information is correct
    Given a report is saved
    When the report is opened
    Then the report "Manufacturer" section contains the following text "Waters Corp., 34 Maple Street, Milford, MA 01757. USA"
    And the report "Details" section contains the following readings from the instrument
      | Detail                   |
      | Software version         |
      | Instrument version       |
      | Serial Number            |
      | Needle volume            |
      | Extension Loop Installed |
      | Extension Loop Size      |
      | Mixer Assembly           |
      | Mixer volume             |
      | Dwell volume             |
      | Tubing Kit               |

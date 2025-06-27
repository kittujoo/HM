@method_editor @ALIST-230 @simulation @daily @tuv_bio @pda @pda_bio @method_editor_sample_manager_advanced_feature
Feature: Method Editor | FTN Sample Manager Advanced
  The FTN Advanced setting is composed of:
  Needle Placement - the distance from the tip of the injection needle to the inner bottom of the sample vial.
  Syringe Draw Rate - provides the option to adapt the sample draw rate depending on the sample viscosity.
  JIRA corresponding requirement: SRS-1297.


  Background:
    Given an acquisition method that contains default settings is open
    And the Sample Manager menu is opened
    And the Sample Manager Advanced menu is opened

  Scenario: Titles and descriptions are displayed - default view
    Then the Sample Manager Advanced menu title is "Sample Manager Advanced"
    And the setting group title is "Sample Manager Advanced"
    And the Values setting title is "Values"
    And the Values setting description is "Waters recommends using default values for all settings"
    And the Default selector title is "Default"
    And the Custom selector title is "Custom"
    And the Default selector is selected
    And the setting titles Automatic Vial Bottom Detection title is "Automatic Vial Bottom Detection"
    And the setting titles Needle Placement from Bottom (mm) title is "Needle Placement from Bottom (mm)"
    And the setting titles Syringe Draw Rate (μL/min) title is "Syringe Draw Rate (μL/min)"

  @ignore
  Scenario: Settings descriptions are displayed - Default Values settings
    When the Values selector is set to Default
    Then the Needle Placement from Bottom setting description is "The distance from the tip of the needle to the bottom of the sample container"
    And the Needle Placement from Bottom input hint text is "0.0 to 30.0 mm"
    And the Syringe Draw Rate input hint text is "10.0 to 1000.0 μL/min"

  @ignore
  Scenario: Sample Manager Advanced can be set as Favorite
    When the Sample Manager Advanced setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Sample Manager Advanced" menu title is available

  @quarantine @defect:INSSYS-299
  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Sample Manager Advanced setting group is displayed
    And the "Sample Manager" menu is highlighted

    Examples:
      | Search Text                     |
      | Advanced                        |
      | Automatic Vial Bottom Detection |
      | Needle Placement from Bottom    |
      | Syringe Draw Rate               |

  Scenario: Default selections are correct when Values selector is "Default"
    Then the "Sample Manager" menu is highlighted
    And the "Sample Manager Advanced" menu is highlighted
    And the Default selector is selected
    And the Sample Manager Advanced menu summary is "Default values"

  Scenario: Default settings are correct when Values selector is "Default"
    Then the Default selector is selected
    And the Automatic Vial Bottom Detection toggle is "Off" and "inactive"
    And the Needle Placement from Bottom input is "inactive"
    And the Needle Placement from Bottom input has value set to "4.0"
    And the Syringe Draw Rate input is "inactive"
    And the Syringe Draw Rate input has value set to "100.0"

  Scenario: Menu summary is correct when Values selector is "Custom"
    When the Values selector is set to Custom
    Then the Sample Manager Advanced menu summary is "Custom values"

  Scenario: Automatic Vial Bottom Detection default setting is correct when Values selector is "Custom"
    When the Values selector is set to Custom
    Then the Automatic Vial Bottom Detection toggle is "Off" and "active"

  Scenario: Needle Placement from Bottom default settings are correct when Values selector is "Custom"
    When the Values selector is set to Custom
    Then the Needle Placement from Bottom input is "active"
    And the Needle Placement from Bottom input has value set to "4.0"
    And the Syringe Draw Rate input is "active"
    And the Syringe Draw Rate input has value set to "100.0"

  Scenario Outline: Needle Placement from Bottom valid value is accepted
    When the Values selector is set to Custom
    And the Needle Placement from Bottom input is set to "<value>"
    Then the Needle Placement from Bottom input is not in error
    And no issue is raised

    Examples:
      | value |
      | 0.0   |
      | 30.0  |

  Scenario Outline: An issue is raised when the Needle Placement from Bottom value is out of range
    When the Values selector is set to Custom
    And the Needle Placement from Bottom input is set to out of range value "<value>"
    Then the Needle Placement from Bottom input is in error
    And an issue is raised
    And the issue has title "Sample Manager Advanced" and description "Invalid Range"

    Examples:
      | value |
      | -     |
      | 30.1  |

  Scenario Outline: Syringe Draw Rate valid value is accepted
    When the Values selector is set to Custom
    And the Syringe Draw Rate input is set to "<value>"
    Then the Syringe Draw Rate input is not in error
    And no issue is raised

    Examples:
      | value  |
      | 10.0   |
      | 1000.0 |

  Scenario Outline: An issue is raised when the Syringe Draw Rate value is out of range
    When the Values selector is set to Custom
    And the Syringe Draw Rate input is set to out of range value "<value>"
    Then the Syringe Draw Rate input is in error
    And an issue is raised
    And the issue has title "Sample Manager Advanced" and description "Invalid Range"

    Examples:
      | value  |
      | -      |
      | 8.9    |
      | 1000.1 |


  Scenario: A single Advanced Settings issue is raised when multiple advanced settings inputs are out of range
    When the Values selector is set to Custom
    And the Needle Placement from Bottom input is in error
    And the Syringe Draw Rate input is in error
    Then the Needle Placement from Bottom input is in error
    And the Syringe Draw Rate input is in error
    And an issue is raised
    And the issue has title "Sample Manager Advanced" and description "Invalid Range"

  @ignore
  Scenario Outline: An Advanced Settings issue can be clicked to navigate to the Sample Manager Advanced section
    When the Values selector is set to Custom
    And the "<Input>" input is in error
    And the System menu is opened
    And the "Sample Manager Advanced" issue indicator is selected
    Then the Sample Manager Advanced setting group is displayed

    Examples:
      | Input                        |
      | Needle Placement from Bottom |
      | Syringe Draw Rate            |

  Scenario Outline: Input issue is cleared when the Values selector is "Default"
    When the Values selector is set to Custom
    And the "<Input>" input is in error
    And the Values selector is set to Default
    Then the "<Input>" input input is "inactive"
    And the "<Input>" input has value set to "<Default_value>"
    And no issues are present

    Examples:
      | Input                        | Default_value |
      | Needle Placement from Bottom | 4.0           |
      | Syringe Draw Rate            | 100.0         |

  Scenario: Needle Placement from Bottom issue is cleared when a valid value is entered
    When the Values selector is set to Custom
    And the Needle Placement from Bottom input is in error
    And the Needle Placement from Bottom input is set to valid value "5"
    Then the Needle Placement from Bottom input has value set to "5"
    And the Needle Placement from Bottom input is not in error
    And no issues are present

  Scenario: A Syringe Draw Rate issue is cleared when a valid value is entered
    When the Values selector is set to Custom
    And the Syringe Draw Rate input is in error
    And the Syringe Draw Rate input is set to valid value "12"
    Then the Syringe Draw Rate input has value set to "12"
    And the Syringe Draw Rate input is not in error
    And no issues are present

  Scenario Outline: Needle Placement from Bottom doesn't accept unexpected input
    When the Values selector is set to Custom
    And the Needle Placement from Bottom input is set to "<value>"
    Then the Needle Placement from Bottom input is in error
    And the Needle Placement from Bottom input is empty
    And the Needle Placement from Bottom input hint text is "Required"
    And an issue is raised
    And the issue has title "Sample Manager Advanced" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |

  Scenario Outline: Syringe Draw Rate doesn't accept unexpected input
    When the Values selector is set to Custom
    And the Syringe Draw Rate input is set to "<value>"
    Then the Syringe Draw Rate input is in error
    And the Syringe Draw Rate input is empty
    And the Syringe Draw Rate input hint text is "Required"
    And an issue is raised
    And the issue has title "Sample Manager Advanced" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |

  Scenario: Settings are saved and restored
    When the Values selector is set to Custom
    And the Automatic Vial Bottom Detection toggle is set to "On"
    And the Needle Placement from Bottom input is set to "2"
    And the Syringe Draw Rate input is set to "30"
    And the method is saved
    And the method is closed and reopened
    And the Sample Manager Advanced menu is opened
    Then the Automatic Vial Bottom Detection toggle is set to "On"
    And the Needle Placement from Bottom input has value set to "2"
    And the Syringe Draw Rate input has value set to "30"

  Scenario: An Advanced Settings issue is raised when reopening a method with parameters out of range
    When the Values selector is set to Custom
    And the Needle Placement from Bottom input is in error
    And the Syringe Draw Rate input is in error
    Then an issue is raised
    When the method is saved
    Then an issue is still raised
    When the method is closed and reopened
    Then an issue is still raised

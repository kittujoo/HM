@method_editor @ALIST-230 @simulation @daily @pda @tuv_bio @pda_bio @method_editor_wash_solvents_feature @new @ignore
Feature: Method Editor | FTN Wash Solvents
  The Wash Solvents setting is composed of the Seal Wash and Needle Wash.
  The user can choose the Wash Solvents separately for Seal Wash and Needle Wash from a list of pre-defined solvents or can create a new solvent name.
  Wash Solvents are optional method parameters and can be omitted.
  JIRA corresponding requirement: SRS-1295.

  Background:
    Given an acquisition method that contains default settings is open
    And the Sample Manager menu is open
    And the Wash Solvents menu is open

      ### Scenario testing labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Wash Solvents menu title is "Wash Solvents"
    And the setting group title is "Wash Solvents"
    And the Seal Wash setting title is "Seal Wash"
    And the Needle Wash setting title is "Needle Wash"

      ### Scenario testing favorites and filtering ###

  Scenario: Wash Solvents can be set as favorites
    When the Wash Solvents setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Wash Solvents" menu title is available

      ### Works only for "Wash" and displays 3 options ###
  Scenario Outline: Setting can be searched for
    When the System Menu is opened
    And "<Search_Text>" is entered into the search bar
    Then the Wash Solvents setting group is displayed
    And the "Sample Manager" menu is highlighted

    Examples:
      | Search_Text   |
      | Wash Solvents |
      | Seal Wash     |
      | Needle Wash   |

      ### Scenario testing default values ###

  Scenario Outline: Default settings are correct
    Then the "Sample Manager" menu is highlighted
    And the "Wash Solvents" menu is highlighted
    And the Seal Wash text box displays "Not configured"
    And the Needle Wash text box displays "Not configured"
    And the Wash Solvents menu summary displays "Not configured"
    When "<Wash_Solvent>" solvent catalogue is opened
    Then "Not configured" option is selected

    Examples:
      | Wash_Solvent |
      | Seal Wash    |
      | Needle Wash  |

      ### Scenario testing solvent options from solvent catalogue ###

  Scenario Outline: All solvents available in solvent catalogue can be selected for Seal Wash
    When the "Seal Wash" solvent catalogue is opened
    And "<Pre_defined_Solvent>" is selected
    And "Done" is selected
    Then the "Seal Wash" input displays "<Pre_defined_Solvent>"
    And the Wash Solvents menu summary displayes "Configured"

    Examples:
      | Pre_defined_Solvent      |
      | Acetonitrile             |
      | Methanol                 |
      | Water                    |
      | Tetrahydrofuran          |
      | Ammonia                  |
      | Buffer                   |
      | Formic Acid              |
      | Phosphate                |
      | Trifluoroacetic Acid     |
      | 10:90 Acetonitrile/Water |
      | 50:50 Acetonitrile/Water |
      | 10:90 Methanol/Water     |

  Scenario Outline: All solvents available in solvent catalogue can be selected for Needle Wash
    When the "Needle Wash" solvent catalogue is opened
    And "<Pre_defined_Solvent>" is selected
    And "Done" is selected
    Then the "Needle Wash" input displays "<Pre_defined_Solvent>"
    And the Wash Solvents menu summary displays "Configured"

    Examples:
      | Pre_defined_Solvent      |
      | Acetonitrile             |
      | Methanol                 |
      | Water                    |
      | Tetrahydrofuran          |
      | Ammonia                  |
      | Buffer                   |
      | Formic Acid              |
      | Phosphate                |
      | Trifluoroacetic Acid     |
      | 10:90 Acetonitrile/Water |
      | 50:50 Acetonitrile/Water |
      | 10:90 Methanol/Water     |

      ### Scenario testing Custom solvents ###

  Scenario Outline: Custom solvents can be created for Seal Wash
    When the "Seal Wash" catalogue is opened
    And "Custom" option is selected
    And "<Custom_Solvent>" solvent name is entered
    And "Done" is selected
    Then the "Seal Wash" input displays the newly created "<Custom_Solvent>"
    And the Wash Solvents menu summary displays "Configured"

    Examples:
      | Custom_Solvent                                   |
      | Ethanol                                          |
      | 80:20 Water/Methanol                             |
      | 90:10 Water/Acetonitrile + 0.01% Formic Acid #99 |

  Scenario Outline: Custom solvents can be created for Needle Wash
    When the "Needle Wash" catalogue is opened
    And "Custom" option is selected
    And "<Custom_Solvent>" solvent name is entered
    And "Done" is selected
    Then the "Needle Wash" input displays the newly created "<Custom_Solvent>"
    And the Wash Solvents menu summary displays "Configured"

    Examples:
      | Custom_Solvent                                   |
      | Ethanol                                          |
      | 80:20 Water/Methanol                             |
      | 90:10 Water/Acetonitrile + 0.01% Formic Acid #99 |

      ### Scenarios for saving methods ###

  Scenario: Settings are saved and restored - solvents from catalogue
    Given the "Seal Wash" solvent is set to "Water" option from solvent catalogue
    And the "Needle Wash" solvent is set to "Acetonitrile" option from solvent catalogue
    When the method is saved
    And the method is closed and reopened
    Then the "Seal Wash" input is "Water"
    And the "Needle Wash" input is set to "Acetonitrile"
    And the Wash Solvents menu summary displays "Configured"

  Scenario: Settings are saved and restored - custom solvents
    Given the "Seal Wash" solvent is set to custom
    And "90:10 Water/Acetonitrile" solvent name is entered for "Seal Wash"
    And the "Needle Wash" solvent is set to custom
    And "80:20 Water/Acetonitrile" solvent name is entered for "Needle Wash"
    When the method is saved
    And the method is closed and reopened
    Then the "Seal Wash" input is "90:10 Water/Acetonitrile"
    And the "Needle Wash" input is set to "80:20 Water/Acetonitrile"
    And the Wash Solvents menu summary displays "Configured"
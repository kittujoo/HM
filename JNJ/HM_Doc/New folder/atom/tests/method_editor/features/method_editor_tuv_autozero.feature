@method_editor @ALIST-230 @simulation @daily @method_editor_autozero_feature
Feature: Method Editor | TUV Autozero
  Autozero On Inject Start can be used to adjust the absorbance value to 0.000 AU at the start of each injection.
  Corresponding JIRA requirement: SRS-1387. The Autozero "On Wavelength Change" setting is applicable when an event is executed as planned in the Event Table.
  As the Event Table is not implemented yet, scenarios/steps with "On Wavelength Change" setting should not be executed for the time being.


  Background:
    Given an acqisition method that contains default settings is open
    And the TUV Detector menu is open
    And the Autozero menu is open

      ### If the "On Wavelength Change" setting is not going to be displayed in 1.2, the corresponding step needs to be deleted/ignored. See INSISPP-8497 ###
  Scenario: Titles and description are displayed - default view
    Then the Autozero menu title is "Autozero"
    And the setting group title text is "Autozero"
    And the Inject Start setting title is "On Inject Start"
    And the Wavelength Change setting title is "On Wavelength Change"
    And the Autozero setting summary is "Choose when to autozero"

  Scenario: Autozero can be set as Favorite
    When the Autozero setting group is set as Favorite
    And the Favorites menu is opened
    Then only the "Autozero" menu title is displayed

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And the "<Search Text>" is entered into the search bar
    Then the Autozero setting group is displayed
    And the "TUV Detector" menu is highlighted

    Examples:
      | Search Text |
      | Autozero    |
      | Baseline    |

      ### If the "On Wavelength Change" setting is not going to be displayed in 1.2, the corresponding step needs to be deleted/ignored. See INSISPP-8497 ###
  Scenario: Default settings are correct
    Then the On Inject Start selector is set to "Autozero"
    And the On Wavelength Change selector is set to "Maintain baseline"

  Scenario: Available options are correct for Inject Start
    Then the On Inject Start selector has the options "Inject Start"
      | Inject Start |
      | Do nothing   |
      | Autozero     |

      ### If the "On Wavelength Change" setting is not going to be displayed in 1.2, the corresponding scenario needs to be ignored. See INSISPP-8497 ###
  Scenario: Available options are correct for Wavelength Change
    Then the On Wavelength Change selector has the options "Wavelength Change"
      | Wavelength Change |
      | Do nothing        |
      | Maintain baseline |
      | Autozero          |

      ### If the "On Wavelength Change" setting is not going to be displayed in 1.2, the corresponding step needs to be deleted/ignored. See INSISPP-8497 ###
  Scenario Outline: Settings are saved and restored
    Given the On Inject Start selector is set to "<Inject Start>"
    And the On Wavelength change selector is set to "<Wavelength Change>"
    When the method is saved
    And the method is closed and reopened
    Then the On Inject Start selector is set to "<Inject Start>"
    And the On Wavelength Change selector is set to "<Wavelength Change>"

    Examples:
      | Inject Start | Wavelength Change |
      | Do nothing   | Autozero          |
      | Autozero     | Do nothing        |
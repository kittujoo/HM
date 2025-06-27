@method_editor @ALIST-230 @simulation @daily @tuv_bio @method_editor_tuv_lamp_feature
Feature: Method Editor | TUV Lamp
            No chromatographic data can be acquired when the TUV lamp is off. The lamp should be off for post-acquisition shutdown method only.
              JIRA corresponding requirement: SRS-1289

  Background:
    Given an acquisition method that contains default settings is open
    And the TUV Detector menu is opened
    And the Lamp menu is opened

  @quarantine @defect:INSISPP-8304 @test
  Scenario: Title and description are displayed
    Then the Lamp menu title is "Lamp"
    And the setting group title is "Lamp"
    And the Lamp State setting title is "Lamp State"
    And the Lamp State setting summary is "Caution: Turn off lamp if this is shutdown method only"

  Scenario: Lamp can be set as Favorite
    When the Lamp setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Lamp" menu title should be available

  Scenario Outline: Lamp Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Lamp setting group is displayed
    And the "TUV Detector" menu is highlighted

    Examples:
      | Search Text |
      | Lamp        |
      | Lamp State  |

  Scenario: Default settings are correct
    Then the "TUV Detector" menu is highlighted
    And the "Lamp" menu is highlighted
    And the Lamp selector is set to "On"
    And the Lamp setting group description is "On"

  Scenario Outline: Setting is saved and restored
    Given the Lamp selector is set to "<Lamp Setting>"
    When the method is saved
    And the method is closed and reopened
    Then the Lamp selector is set to "<Lamp Setting>"
    And the setting group description is "<Description>"

    Examples:
      | Lamp Setting | Description |
      | Off          | Off         |
      | On           | On          |

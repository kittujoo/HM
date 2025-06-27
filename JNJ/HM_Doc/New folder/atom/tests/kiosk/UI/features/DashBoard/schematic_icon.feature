@simulation @smoke @kiosk @ALIST-228 @kiosk_schematic_icon_feature
Feature: Kiosk | Schematic icon feature

  Background:
    Given The user taps the "home" icon

  @weekly
  Scenario: To validate schematic icons
    When User taps on the solvent bottle schematic icon
    Then User validates the solvent bottle schematic icon is highlighted
    When User taps on the solvent manager schematic icon
    Then User validates the solvent manager schematic icon is highlighted
    When User taps on the sample manager schematic icon
    Then User validates the sample manager schematic icon is highlighted
    When User taps on the column manager schematic icon
    Then User validates the column manager schematic icon is highlighted
    When User taps on the tuv schematic icon
    Then User validates the tuv schematic icon is highlighted
    When User taps the home icon
    Then User validates none of the schematic icons are highlighted

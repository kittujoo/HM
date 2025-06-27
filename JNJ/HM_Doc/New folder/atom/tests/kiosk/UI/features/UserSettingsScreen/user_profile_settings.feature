@kiosk @user @userProfile @reg
Feature: Kiosk | Test for User profile settings screen

  Background:
    Given User navigates to the user profile screen

      #########################
      # -- Sounds Settings -- #
      #########################

  @ignore # Sound settings removed from KIOSK
  Scenario Outline: To test sound settings
    When User taps the sound tab
    And User sets the volume as "<volume_settings>"
    Then User confirms the user profile settings
      # validate it saved
    And User returns to the dashboard

    Examples:
      | volume_settings |
      | high            |
      | mute            |
      #| low           |

      ################################
      # -- Date and Time Settings -- #
      ################################

  Scenario Outline: To verify when the time option is changed, it is being applied
    When User taps the Date and Time format tab
    And User selects the time format as "<time_format>"
    Then User confirms the user profile settings
    And User taps the Date and Time format tab
    And User verifies the "<time_format>" and the "<displayed_time_format>" were saved

    Examples:
      | time_format | displayed_time_format |
      | 24 Hour     | 13:00                 |
      | 12 Hour     | 1:00 PM               |

  Scenario: To verify the date format changes when the user makes the selection
    When User taps the Date and Time format tab
    Then User selects and validates the date format option


  Scenario Outline: To verify when date format is changed, the change is being applied
    When User taps the Date and Time format tab
    And User scrolls to select the date format as "<date_format>"
    Then User confirms the user profile settings
    And User taps the Date and Time format tab
    And User verifies the "<date_format>" was saved

    Examples:
      | date_format       |
      | Feb/29/2020       |
      | 2020, 29 February |
      | February 29, 2020 |
      | 02/29/2020        |
      | 29 February 2020  |
      | 2020/02/29        |
      | 2020 February 29  |

  Scenario: To verify the time zone subtitle changes when the user makes a selection
    When User taps the Date and Time format tab
    Then User selects and validates the time zone option

  Scenario Outline: To verify when the time zone are changed using the scroll action, The changes being made
    When User taps the Date and Time format tab
    And User taps the time zone tab
    And User scrolls to an "<time_zone_option>" in the time zone
    Then Validate the time zone option "<expected_text>"

    Examples:
      | time_zone_option | expected_text          |
      | Belarus          | Belarus Standard Time  |
      | Central Atlantic | Atlantic Standard Time |
      | UTC              | UTC                    |

  Scenario Outline: To verify when date format type are changed using scroll action, The changes being applied
    When User taps the Date and Time format tab
    And User scrolls to select the date format as "<date_format>"
    Then User confirms the user profile settings
    And User taps the Date and Time format tab
    And User verifies the "<date_format>" was saved

    Examples:
      | date_format       |
      | Feb/29/2020       |
      | 2020, 29 February |


  Scenario Outline: To verify the date format in logs can be modified
    When User taps the Date and Time format tab
    And User scrolls to select the date format as "<date_format>"
    Then User confirms the user profile settings
    And User returns to the dashboard
    And User verifies the date format in logs is "<date_format>"

    Examples:
      | date_format       |
      | Feb/29/2020       |
      | 2020, 29 February |
      | February 29, 2020 |
      | 02/29/2020        |
      | 29 February 2020  |
      | 2020/02/29        |
      | 2020 February 29  |

  @ignore # date changing has been removed, however relies on an NTP service so this should be reintroduced at some point
  Scenario Outline: To verify user can change the date and save it
    When User taps the Date and Time format tab
    And User sets the date as "<month>" "<day>" "<year>"
    Then User confirms the user profile settings
    And User taps the Date and Time format tab
      # validate it saved
    And User cancels the user profile settings
    And User returns to the dashboard

    Examples:
      | month | day | year |
      | July  | 10  | 2020 |


  Scenario Outline: To verify when the time format is changed, it gets reflected in logs
    When User taps the Date and Time format tab
    And User selects the time format as "<time_format>"
    Then User confirms the user profile settings
    And User returns to the dashboard
    And User verifies "<displayed_time_format>" is reflected in logs

    Examples:
      | time_format | displayed_time_format |
      | 24 Hour     | 13:00                 |
      | 12 Hour     | 1:00 PM               |

      #####################################
      # -- Display and Themes Settings -- #
      #####################################

  @ignore # display & themes removed from KIOSK
  Scenario Outline: to test display and themes
    When User taps the display tab
    And User selects the theme settings as "<theme_settings>"
    Then User confirms the user profile settings
      # validate it saved
    And User returns to the dashboard

    Examples:
      | theme_settings |
      | dark           |
      | light          |

      ###############################
      # -- Screen Saver Settings -- #
      ###############################
      # Leaving screen saver for now but it's most likely indefinitely removed from KIOSK 9/14/23

  @ignore # screen saver removed from KIOSK
  Scenario Outline: To verify when screen saver types are changed, the changes are being applied
    #TODO: Code for testing the full screen preview will need to be added once functionality has been added
    When User taps the screen saver tab
    And User selects the screen saver settings period as "<screen_saver_period>"
    And User selects the screen saver style as "<screen_saver_style>"
    Then User confirms the user profile settings
    And User taps the screen saver tab
    And User verifies that the "<screen_saver_style>" was saved
    And User cancels the user profile settings
    And User returns to the dashboard

    Examples:
      | screen_saver_period | screen_saver_style |
      | 5 min               | Orion Logo Time    |
      | 5 min               | Instrument State   |
      | 5 min               | Waters Logo        |
      | 5 min               | Date and Time      |

  @ignore # screen saver removed from KIOSK
  Scenario Outline: To validate Screen Saver Picker will appear, When the user selects a time period other than "Never"
    When User taps the screen saver tab
    And User selects the screen saver settings period as "<screen_saver_period>"
    Then Validate the screen saver picker is displayed "<expected_screen_saver_picker_display_status>"

    Examples:
      | screen_saver_period | expected_screen_saver_picker_display_status |
      | Never               | False                                       |
      | 5 min               | True                                        |
      | 15 min              | True                                        |
      | 20 min              | True                                        |

  @ignore # screen saver removed from KIOSK
  Scenario Outline: To verify when screen saver type is changed but cancelled, it is not saving
    When User taps the screen saver tab
    And User selects the screen saver settings period as "<screen_saver_period>"
    And User scrolls to select the style as "<screen_saver_style>"
    Then User cancels the user profile settings
    And User taps the screen saver tab
    And User verifies that the "<screen_saver_style>" was not saved

    Examples:
      | screen_saver_period | screen_saver_style |
      | 5 min               | Instrument State   |
      | 5 min               | Orion Logo Time    |
      | 5 min               | Waters Logo        |

  @ignore # screen saver removed from KIOSK
  Scenario Outline:  To verify the screen saver changes when the user makes the selection
    When User taps the screen saver tab
    And User selects the screen saver settings period as "<screen_saver_period>"
    Then User selects and validates the screen saver options
    And User cancels the user profile settings
    And User returns to the dashboard

    Examples:
      | screen_saver_period |
      | 5 min               |
      | 20 min              |
      | 15 min              |

  @ignore # screen saver removed from KIOSK
  Scenario Outline: To verify the screen saver option is hidden when the settings period "Never" is selected
    When User taps the screen saver tab
    And User selects the screen saver settings period as Never
    Then User validates the screen saver option displayed is "<is_displayed>"

    Examples:
      | is_displayed |
      | False        |

  @ignore # screen saver removed from KIOSK
  Scenario Outline: To verify when screen saver types are changed using scroll action, the changes are being applied
    #TODO: Code for testing the full screen preview will need to be added once functionality has been added
    When User taps the screen saver tab
    And User selects the screen saver settings period as "<screen_saver_period>"
    And User scrolls to select the style as "<screen_saver_style>"
    Then User confirms the user profile settings
    And User taps the screen saver tab
    And User verifies that the "<screen_saver_style>" was saved
    And User cancels the user profile settings
    And User returns to the dashboard

    Examples:
      | screen_saver_period | screen_saver_style |
      | 5 min               | Instrument State   |
      | 5 min               | Orion Logo Time    |
      | 5 min               | Waters Logo        |
      | 5 min               | Date and Time      |

      ##################################
      # -- Instrument Name Settings -- #
      ##################################

  @ignore # Lock screen unavailable in simulation
  Scenario Outline: To verify instrument name changes in affected areas
    When User taps the instrument name tab
    And User enters the "<instrument_name>"
    And User confirms the user profile settings
      # And User signs out of the KIOSK
      # Then User validates the "<instrument_name> was saved and displayed on lock screen
      # And User signs back into KIOSK

    Examples:
      | instrument_name |
      | P@th. find, 3r  |

      ##############################
      # -- Lock Screen Settings -- #
      ##############################

  @ignore # lock screen unavailable in simulation
  Scenario Outline: to test lock screen setting
    When User taps the lock screen tab
    And User selects the screen lock period as "<screen_lock_period>"
    Then User confirms the user profile settings
      # validate it saved /// wait for modal & lock screen
    And User returns to the dashboard

    Examples:
      | screen_lock_period |
      | Never              |
      | 5 min              |
      | 10 min             |


  Scenario Outline: To test lock screen settings
    When User taps the lock screen tab
    And User selects the lock screen period as "<lock_screen_period>"
    Then User validates lock screen tab for duration "<lock_screen_period>"

    Examples:
      | lock_screen_period |
      | 5 min              |
      | 15 min             |
      | 30 min             |
      | 120 min            |

      ####################################
      # -- Units and Numbers Settings -- # #TODO: This cannot be accessed [INS-26865]
      ####################################

  @ignore
  Scenario: to test units and numbers

    ################################
    # -- Remote Access Settings -- # #TODO: This cannot be accessed [INS-26865]
    ################################

  @ignore
  Scenario: to test remote access

    ############################
    # -- User Note Settings -- # #TODO: This cannot be accessed [INS-26865]
    ############################

  @ignore
  Scenario: to test user note


  Scenario Outline: To verify system name changes in affected areas
    When User taps the system name tab
    And User enters the "<system_name>"
    Then User validates the "<system_name>" was saved and displayed on user preferences screen

    Examples:
      | system_name      |
      | P@th. find, 3r   |
      | KIOSKAPP         |
      | 12345            |
      | 12345abcd        |
      | KIOSK1234%%kiosk |
      | ...456...        |
      | 234:890:456      |
      #      |                |


  Scenario Outline: To verify system name is allowed to have maximum 30 characters
    When User taps the system name tab
    And User enters the "<system_name>"
    Then User validates the comment card shows correct numbers with "<length>" characters

    Examples:
      | system_name                       | length |
      | abcdefgh                          | 8      |
      | abcdefghijklmnopqrstuvwxyz1234    | 30     |
      | abcdefghijklmnopqrstuvwxyz1234>%@ | 30     |
      | q                                 | 1      |
      |                                   | 0      |


  Scenario: To verify erasing system name updates the comment card characters
    When User taps the system name tab
    And User enters the System123
    And User erases 3 characters from system name
    Then User validates the comment card shows correct numbers with 6 characters

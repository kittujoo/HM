@kiosk @autosampler #@link(https://code.waters.com/bitbucket/projects/OSQ/repos/orionisppintegrationtests/browse/Kiosk/tests/UI/features/SystemSettingsScreen/sm_configuration_part_one.feature)
Feature: Kiosk | Sample manager configuration settings screen

   ### This file has been replaced with "sample_manager_configuration_settings.feature" 
  Scenario Outline: To verify the user able to set the different configuration settings by navigating to volume settings screen

    When User navigates to volume settings screen
    And User selects the volume "<single_draw_volume>""
    And User taps the chamber light preference settings tab
    And User selects the chamber light preference "<light_preference_for_plate>"" when the plate is being scanned
    And User selects the chamber light preference "<light_preference_for_door>"" when the door is open
    And User taps the options tab
    And User toggles leak sensor mode "<leak_sensor_enabled>"" to monitor the leak sensor in the system
    And User toggles the door open notification mode "<door_open_notification_enabled>""
    And User toggles multi draw mode "<multi_draw_enabled>""
    And User taps the notification tab
    And User toggles the vial missing detection mode "<vial_missing_detection>""
    And User toggles the wash needle mode "<wash_needle_enabled>""
    And User toggles auto rotate samples "<auto_rotate_samples_enabled>""
    And User toggles the plate detection mode "<plate_detection_enabled>""
    And User confirms the configuration settings for the sample manager
    And User navigates to volume settings screen
    Then Validate "<single_draw_volume>"" option has been selected in volume settings
    And User taps the chamber light preference settings tab
    And Validate "<light_preference_for_plate>"" and "<light_preference_for_door>"" options has been selected in light preference settings
    And Validate "<injection_option>"" options has been selected
    And Validate options settings with "<leak_sensor_enabled>"" and "<multi_draw_enabled>""
    And Validate notification settings with "<vial_missing_detection>"", "<door_open_notification_enabled>"", "<wash_needle_enabled>"", "<plate_detection_enabled>""
    Examples:
      | single_draw_volume | light_preference_for_plate | light_preference_for_door | injection_option | leak_sensor_enabled | multi_draw_enabled | auto_rotate_samples_enabled | vial_missing_detection | door_open_notification_enabled | wash_needle_enabled | plate_detection_enabled |
      | 100                | off                        | off                       | continues        | False               | False              | True                        | False                  | True                           | False               | True                    |
      | 50                 | off                        | on                        | fails            | True                | False              | False                       | False                  | False                          | True                | True                    |
      | 100                | on                         | off                       | fails            | False               | False              | False                       | False                  | True                           | True                | False                   |

  Scenario Outline: To verify user able to set configuration setting by navigates through chamber light preference settings screen

    When User navigates to chamber light preference settings screen
    And User selects the chamber light preference "<light_preference_for_plate>"" when the plate is being scanned
    And User selects the chamber light preference "<light_preference_for_door>"" when the door is open
    And User taps the volume settings tab
    And User selects the volume "<single_draw_volume>""
    And User taps the options tab
    And User toggles leak sensor mode "<leak_sensor_enabled>"" to monitor the leak sensor in the system
    And User toggles the door open notification mode "<door_open_notification_enabled>""
    And User toggles multi draw mode "<multi_draw_enabled>""
    And User taps the notification tab
    And User toggles the vial missing detection mode "<vial_missing_detection>""
    And User toggles the wash needle mode "<wash_needle_enabled>""
    And User toggles auto rotate samples "<auto_rotate_samples_enabled>""
    And User toggles the plate detection mode "<plate_detection_enabled>""
    And User confirms the configuration settings for the sample manager
    And User navigates to volume settings screen
    Then Validate "<light_preference_for_plate>"" and "<light_preference_for_door>"" options has been selected in light preference settings
    And Validate "<injection_option>"" options has been selected
    And Validate options settings with "<leak_sensor_enabled>"" and "<multi_draw_enabled>""
    And Validate notification settings with "<vial_missing_detection>"", "<door_open_notification_enabled>"", "<wash_needle_enabled>", "<plate_detection_enabled>"
    Examples:
      | single_draw_volume | light_preference_for_plate | light_preference_for_door | injection_option | leak_sensor_enabled | multi_draw_enabled | auto_rotate_samples_enabled | vial_missing_detection | door_open_notification_enabled | wash_needle_enabled | plate_detection_enabled |
      | 100                | off                        | off                       | continues        | False               | False              | True                        | False                  | True                           | False               | True                    |
      | 50                 | off                        | on                        | fails            | True                | False              | False                       | False                  | False                          | True                | True                    |
      | 100                | on                         | off                       | fails            | False               | False              | False                       | False                  | True                           | True                | False                   |

  Scenario Outline: To verify user able to set the different configuration settings by navigating to options screen

    When User navigates to options settings screen
    And User toggles leak sensor mode "<leak_sensor_enabled>" to monitor the leak sensor in the system
    And User toggles the door open notification mode "<door_open_notification_enabled>"
    And User toggles multi draw mode "<multi_draw_enabled>"
    And User taps the volume settings tab
    And User selects the volume "<single_draw_volume>"
    And User taps the chamber light preference settings tab
    And User selects the chamber light preference "<light_preference_for_plate>" when the plate is being scanned
    And User selects the chamber light preference "<light_preference_for_door>" when the door is open
    And User taps the notification tab
    And User toggles the vial missing detection mode "<vial_missing_detection>"
    And User toggles the wash needle mode "<wash_needle_enabled>"
    And User toggles auto rotate samples "<auto_rotate_samples_enabled>"
    And User toggles the plate detection mode "<plate_detection_enabled>"
    And User confirms the configuration settings for the sample manager
    And User navigates to volume settings screen
    Then Validate "<light_preference_for_plate>" and "<light_preference_for_door>" options has been selected in light preference settings
    And Validate "<injection_option>" options has been selected
    And Validate options settings with "<leak_sensor_enabled>" and "<multi_draw_enabled>"
    And Validate notification settings with "<vial_missing_detection>", "<door_open_notification_enabled>", "<wash_needle_enabled>", "<plate_detection_enabled>"
    Examples:
      | single_draw_volume | light_preference_for_plate | light_preference_for_door | injection_option | leak_sensor_enabled | multi_draw_enabled | auto_rotate_samples_enabled | vial_missing_detection | door_open_notification_enabled | wash_needle_enabled | plate_detection_enabled |
      | 100                | off                        | off                       | continues        | False               | False              | True                        | False                  | True                           | False               | True                    |
      | 50                 | off                        | on                        | fails            | True                | False              | False                       | False                  | False                          | True                | True                    |
      | 100                | on                         | off                       | fails            | False               | False              | False                       | False                  | True                           | True                | False                   |

  Scenario Outline: To verify user able to set the different configuration settings by navigating to notification screen

    When User navigates to notification settings screen
    And User toggles the vial missing detection mode "<vial_missing_detection>"
    And User toggles the wash needle mode "<wash_needle_enabled>"
    And User toggles auto rotate samples "<auto_rotate_samples_enabled>"
    And User toggles the plate detection mode "<plate_detection_enabled>"
    And User taps the options tab
    And User toggles leak sensor mode "<leak_sensor_enabled>" to monitor the leak sensor in the system
    And User toggles the door open notification mode "<door_open_notification_enabled>"
    And User toggles multi draw mode "<multi_draw_enabled>"
    And User taps the volume settings tab
    And User selects the volume "<single_draw_volume>"
    And User taps the chamber light preference settings tab
    And User selects the chamber light preference "<light_preference_for_plate>" when the plate is being scanned
    And User selects the chamber light preference "<light_preference_for_door>" when the door is open
    And User confirms the configuration settings for the sample manager
    And User navigates to volume settings screen
    Then Validate "<light_preference_for_plate>" and "<light_preference_for_door>" options has been selected in light preference settings
    And Validate "<injection_option>" options has been selected
    And Validate options settings with "<leak_sensor_enabled>" and "<multi_draw_enabled>"
    And Validate notification settings with "<vial_missing_detection>", "<door_open_notification_enabled>", "<wash_needle_enabled>", "<plate_detection_enabled>"
    Examples:
      | single_draw_volume | light_preference_for_plate | light_preference_for_door | injection_option | leak_sensor_enabled | multi_draw_enabled | auto_rotate_samples_enabled | vial_missing_detection | door_open_notification_enabled | wash_needle_enabled | plate_detection_enabled |
      | 100                | off                        | off                       | continues        | False               | False              | True                        | False                  | True                           | False               | True                    |
      | 50                 | off                        | on                        | fails            | True                | False              | False                       | False                  | False                          | True                | True                    |
      | 100                | on                         | off                       | fails            | False               | False              | False                       | False                  | True                           | True                | False                   |
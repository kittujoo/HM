"""
File_Name: sm_configuration_settings.py
Desc: This is the data-holder class which holds the attributes of the sample manager configuration settings value
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/21/2021

"""


class VolumeSettings:
    single_draw_volume: int
    syringe_size: int


class LightPreferences:
    light_preference_for_plate: str
    light_preference_for_door: str


class NotificationSettings:
    leak_detection_enabled: bool
    door_open_notification_enabled: bool
    door_open_audible_alarm_enabled: bool
    plate_detection_enabled: bool


class OptionSettings:
    leak_sensor_enabled: bool
    multi_draw_enabled: bool
    auto_rotate_samples_enabled: bool


class SMConfigurationSettings:
    volume_settings: VolumeSettings
    option_settings: OptionSettings
    notification_settings: NotificationSettings
    light_preferences: LightPreferences




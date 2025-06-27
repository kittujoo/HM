"""
File_Name: tuv_configuration_settings.py
Desc: This is the data-holder class which holds the attributes of the TUV configuration settings value
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/23/2020

"""

class TUVConfigurationSettings:
    optics_temperature_stabilization: str
    close_shutter_preference: str
    leak_sensor_options: str

    def __init__(self, optics_temperature_stabilization: str, close_shutter_preference: float, leak_sensor_options: str):
        self.optics_temperature_stabilization = optics_temperature_stabilization
        self.close_shutter_preference = close_shutter_preference
        self.leak_sensor_options = leak_sensor_options

    def __str__(self):
        return f"optics_temperature_stabilization => {self.optics_temperature_stabilization}, close_shutter_preference => {self.close_shutter_preference}, leak sensor options ={self.leak_sensor_options}"

    def __eq__(self, other):
        if other is not None and isinstance(other, TUVConfigurationSettings):

            if self.optics_temperature_stabilization == other.optics_temperature_stabilization\
                    and self.close_shutter_preference == other.close_shutter_preference\
                    and self.leak_sensor_options == other.leak_sensor_options:
                return True

        return False


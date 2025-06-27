class Notset:
    def __repr__(self):
        return "<NOTSET>"


notset = Notset()

ENVIRONMENT = "environment"
RUN_ON_LOCAL = "run_on_local"
PATH_TO_DEFAULT_CONFIG = "config/default_settings.toml"
PATH_TO_TEMP_CONFIG = "config/temp_settings.toml"
HEADLESS = "headless"
ISPP_HOSTNAME = "ispp_hostname"
HARDWARE_SYSTEM_NAME = "hardware_system_name"
EMPOWER_SYSTEM_NAME = "empower_system_name"
ICS_INSTRUMENT_TYPE = "ics_instrument_type"
METHOD_NAME = "method_name"
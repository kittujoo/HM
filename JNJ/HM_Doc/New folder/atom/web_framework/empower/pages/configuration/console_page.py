from selenium.webdriver.common.by import By

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class ConsoleBasePage(WinAppBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_tab(self):
        self.click_on_element((By.XPATH, "//Text[@Name='Home']"))

    def open_setup_tab(self):
        self.click_on_element((By.XPATH, "//Text[@Name='Setup']"))

    def open_commands_tab(self):
        self.click_on_element((By.XPATH, "//Text[@Name='Commands']"))

    def open_solvents_tab(self):
        self.click_on_element((By.XPATH, "//Text[@Name='Solvents']"))

    def open_counters_tab(self):
        self.click_on_element((By.XPATH, "//Text[@Name='Counters']"))

    def open_acquisition_tab(self):
        self.click_on_element((By.XPATH, "//Text[@Name='Acquisition']"))


class ConsoleHomePage(ConsoleBasePage):
    """
        Due to lack of automation IDs we need to load controls based on position.
        This should be a temporary solution until the ids and supporting structure are added to the apps.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def get_system_state(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[8]"))

    def get_system_label(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[9]"))

    def get_flow_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[10]"))

    def get_flow_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[11]"))

    def get_composition_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[12]"))

    def get_composition_value_a(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[13]"))

    def composition_value_b(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[14]"))

    def composition_value_c(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[15]"))

    def get_composition_value_d(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[16]"))

    def get_column_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[17]"))

    def get_column_name(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[18]"))

    def get_delta_pressure_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[19]"))

    def get_delta_pressure_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[20]"))

    def get_system_pressure_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[21]"))

    def get_system_pressure_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[22]"))

    def get_sample_pressure_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[23]"))

    def get_sample_pressure_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[24]"))

    def get_system_temperature_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[25]"))

    def get_system_temperature_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[26]"))

    def get_sample_temperature_state(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[27]"))

    def get_column_temperature_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[28]"))

    def get_column_temperature_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[29]"))

    def get_column_temperature_state(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[30]"))

    def get_ambient_temperature_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[31]"))

    def get_ambient_temperature_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[32]"))

    def get_lamp_state_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[33]"))

    def get_lamp_state_value(self) -> str:
        return self.get_text((By.XPATH, "//Text[@Name='Lamp State']//following::Text")).strip(" ")

    def get_channel_a_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[35]"))

    def get_channel_a_value(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[36]"))

    def get_channel_b_header(self) -> str:
        return self.get_text((By.XPATH, "(//Document//Text)[37]"))

    def get_channel_b_value(self) -> str:
        value = self.get_text((By.XPATH, "(//Document//Text)[38]"))
        return value

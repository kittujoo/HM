import json
import re

import fitz

from utilities.logger import Logger


class IcsReportsUtilities:
    def __init__(self, json_file_path, report_file_path):
        self._logger = Logger(self.__class__.__name__)
        with open(json_file_path, 'r') as json_file:
            self.json_data = json.load(json_file)

        self.report_text = self.extract_text_from_report(report_file_path)

    def extract_text_from_report(self, report_path):
        try:
            doc = fitz.open(report_path)
            text = "".join([page.get_text() for page in doc])
            return text
        except Exception as e:
            self._logger.error(f"Failed to open pdf report with error: [{e}]")
            raise e

    def find_key_value_in_json(self, json_data, key):
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                if k == key:
                    return v
                elif isinstance(v, dict):
                    result = self.find_key_value_in_json(v, key)
                    if result is not None:
                        return result
        elif isinstance(json_data, list):
            return next((self.find_key_value_in_json(item, key) for item in json_data if item is not None), None)

    def normalize(self, value):
        value_str = str(value)
        regex = re.compile(r'(\d+)(?:\.(\d+))?(\s*\([^)]+\))?')
        match = regex.match(value_str)
        if match:
            return match.group(1)
        else:
            self._logger.debug(f"{match}")
            return value

    def compare_key_value_in_report(self, json_key, report_key):
        if report_key not in self.report_text:
            self._logger.error(f"'{json_key}' not found in report.")
            return False

        report_key_index = self.report_text.find(report_key)
        report_value_start = report_key_index + len(report_key)

        report_value = self.report_text[report_value_start:].split('\n')[1].strip()
        report_value_normalized = str(self.normalize(report_value))
        json_value = self.find_key_value_in_json(self.json_data, json_key)

        if str(json_value) == str(report_value_normalized):
            self._logger.debug(f"'{json_key}' found in report as '{report_key}'. Values match.")
            return True
        else:
            self._logger.error(f"'{json_key} | {json_value}' found in report as '{report_key} | {report_value_normalized}'. Values DO NOT match.")
            return False

    def validate_report(self, key_mapping):
        for json_key, report_key in key_mapping.items():
            return self.compare_key_value_in_report(json_key, report_key)

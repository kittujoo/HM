"""
File_Name: style_attribute_parser.py
Desc: This class is to parse the style attribute in the html element.__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/17/]nh


"""

from utilities.logger import Logger


class StyleAttributeParser:

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    def parse(self, input_string: str, attribute_delimiter: str, value_delimiter: str):
        """
        This function returns dictionary which contains the style attribute and its corresponding value.
        @param input_string: the html element that needs to be parsed
        @param attribute_delimiter:the special character which is used to separate the attribute
        @param value_delimiter: special character which is used to separate the attribute and its value
        @return:
        """
        attribute_key_values = {}

        attribute_list = input_string.split(attribute_delimiter)
        for attribute in attribute_list:
            key_values = attribute.strip().split(value_delimiter)
            if key_values is not None and len(key_values) == 2:
                attribute_key_values[key_values[0].strip()] = key_values[1].strip()
        return attribute_key_values

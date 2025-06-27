"""
File_Name: type_converter.py
Desc: This file has functions that  does  different conversion from one data type to other
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 08/19/2020
__modified__ = "Sharmila Vairamani" Refactored and added doc strings - 09/14/2020
__modified___ = "Sharmila Vairamani" Refactored the to_float function - 09/28/2020
__modified___ = "Sharmila Vairamani" Added is_float function - 11/17/2020
"""

import json
from typing import Any, Type, cast, List, Callable, Optional

from utilities.types import T


class TypeConverter:

    @staticmethod
    def to_list(f: Callable[[Any], T], x: Any) -> List[T]:
        """
        This function converts a given object to list
        @param f: Any callable function
        @param x: The object that needs to be converted
        @return: List
        """
        assert isinstance(x, list)
        return [f(y) for y in x]

    @staticmethod
    def is_float(x: str) -> bool:
        """
        This function returns True if  a given string is float else False
        @param x: variable
        @return: bool
        """
        if isinstance(x, str):
            try:
                float(x)
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def to_float(x: str) -> float:
        """
        This function converts a given string to float
        @param x: variable
        @return: Float
        """
        if not isinstance(x, str):
            assert isinstance(x, (float, int)) and not isinstance(x, bool)
        return float(x)

    @staticmethod
    def to_int(x: Any) -> Optional[int]:
        """
        This function converts a given any data type to int
        @param x: The object that needs to be converted
        @return: Integer
        """
        if x is None:
            return x
        assert isinstance(x, int)
        return x

    @staticmethod
    def to_str(x: Any) -> str:
        """
        This function converts any data type to str
        @param x: The object that needs to be converted str
        @return: String
        """
        assert isinstance(x, str)
        return x

    @staticmethod
    def to_object(x: Any) -> Any:
        """
         This function converts any data type to object
        @param x: The object that needs to be converted
        @return: Object
        """
        if x is None or isinstance(x, dict):
            return x
        if isinstance(x, str):
            return json.loads(x)

    @staticmethod
    def to_dict(c: Type[T], x: Any) -> dict:
        """
         This function converts any data type to dict
        @param c: A class
        @param x: The object that needs to be converted
        @return: dictionary
        """
        assert isinstance(x, c)
        return cast(Any, x).to_dict()

    @staticmethod
    def to_bool(value):
        """
        This function converts any data type to bool
        @rtype: object
        """
        valid = {'true': True, 't': True, '1': True,
                 'false': False, 'f': False, '0': False,
                 }

        if isinstance(value, bool):
            return value

        if not isinstance(value, str):
            raise ValueError('invalid literal for boolean. Not a string.')

        lower_value = value.lower()
        if lower_value in valid:
            return valid[lower_value]
        else:
            raise ValueError('invalid literal for boolean: "%s"' % value)


def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))


def convert(val: str, list_separator=','):
    """
    Convert a string to its proper base type [bool, list, int, float, str]
    :param val: string to convert
    :param list_separator: list separator
    :return: value with proper type
    """
    constructors = [strtobool, int, float, str]
    for c in constructors:
        try:
            if list_separator in val:
                return val.split(list_separator)
            return c(val)
        except ValueError:
            pass

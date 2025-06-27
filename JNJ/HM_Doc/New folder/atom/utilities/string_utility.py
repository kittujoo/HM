import re

def remove_substring(input_string: str, string_to_remove: str) -> str:
    """
    This function remove any substring in a given string
    @param input_string: string in which then given string needs to be removed
    @param string_to_remove: The string that needs to be removed
    @return:
    """
    if string_to_remove in input_string:
        index = input_string.index(string_to_remove)
        return input_string[0:index]
    return input_string


def is_text_present(input_string: str, string_to_find: str):
    """
    This function return true when the text is present in any given string
    :param input_string:
    :param string_to_find:
    :return:
    """
    if input_string.find(string_to_find) == -1:
        return False
    else:
        return True


def get_string_in_range(input_string: str, start: int, end: int):
    """
    This function gives the range of character in a given string
    @param input_string: The string from which the range of character need to be extracted
    @param start: index of the first string
    @param end: index of the last string
    @return:
    """
    string_in_range = input_string[start:end]
    return string_in_range


def convert_to_list(string):
    """
    This function converts any string into a list
    @param string: The string from which needs to be converted
    @return: list
    """
    list1 = []
    list1[:0] = string
    return list1


def get_index_after_text(input_string: str, string_to_find: str):
    """
    This function gives the index right after the first occurrence of a matching text
    @param input_string: The string where to search
    @param string_to_find: If this string is found, return the index after it
    @return: Index after matching text
    """
    index = input_string.find(string_to_find)

    if index > 0:
        index = index + len(string_to_find)

    return index


def str_to_bool(value: str) -> bool:
    if value.lower().strip() in ["true", "yes", "y", "on", "enable"]:
        return True
    elif value.lower().strip() in ["false", "no", "n", "off", "disable"]:
        return False
    else:
        raise ValueError(f"Failed to parse string to bool: [{value}]")

def str_to_int(input_string: str) -> int:
    if input_string.isdigit(): 
        integer = int(input_string) 
        return integer  
    else: 
        raise ValueError(f"Failed to parse string to int: [{input_string}]")    

def is_float(input_string:str)-> bool:
    pattern = r"^[-+]?[0-9]*\.?[0-9]+$"   
    pattern_found = re.match(pattern, input_string)   
    return pattern_found

def str_to_float(input_string: str) -> float:
    if is_float(input_string) : 
        return float(input_string)
    else: 
        raise ValueError(f"Failed to parse string to float: [{input_string}]")          
        

def str_to_seconds(input_string: str):
    """
    This function receives string in format "0:00:00:00" and returns to seconds
    @param input_string: The string in format "0:00:00:00"
    @return: total_seconds converted in seconds
    """
    time_components = input_string.split(':')

    if len(time_components) == 4:
        days, hours, minutes, seconds = map(int, time_components)
        total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        raise ValueError(f"Failed to parse string to seconds: [{input_string}]")

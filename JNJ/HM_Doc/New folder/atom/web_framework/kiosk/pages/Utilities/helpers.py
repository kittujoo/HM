"""
File_Name: helpers.py
Desc: This file contains the function which  converts the given parameter to a boolean value
"""


def to_toggle_state(toggle_state) -> bool:
    """
            This function converts the given parameter to a boolean value
            @param toggle_state: String type data from the feature file
            @return: True or False
        """
    return True if toggle_state == 'ON' else False

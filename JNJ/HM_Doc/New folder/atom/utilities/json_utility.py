import json
import os
from dataclasses import is_dataclass, asdict
from enum import Enum
from typing import Any

from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def read_json_file(file_name):
    """
    Open JSON file and read data
    @param: file name
    @return json data
    """
    try:
        with open(file_name, mode="r", encoding="utf8") as outfile:
            data_buff = json.load(outfile)
    except json.JSONDecodeError as e:
        logger.error(f"Reading json file failed with error: [{e}]")
        raise e from None
    return data_buff


def custom_asdict_factory(data):
    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.name
        return obj

    return dict((k, convert_value(v)) for k, v in data)


def as_dict(data: Any):
    assert is_dataclass(data), "This method supports only dataclasses"
    response = asdict(data, dict_factory=custom_asdict_factory)
    return response

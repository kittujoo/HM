import json
from json import JSONDecodeError
from typing import Optional, Any


def parse_string_to_obj(string: str) -> Optional[Any]:
    try:
        obj = json.loads(string)
        return obj
    except JSONDecodeError:
        return string

from typing import Dict, Any, List

import glom
from glom import PathAccessError


def assign_many(obj, items: Dict[str, Any], missing=None):
    for path, value in items.items():
        glom.assign(obj, path, value, missing=missing)


def delete(obj, *paths, ignore_missing=False):
    for path in paths:
        glom.delete(obj, path, ignore_missing=ignore_missing)


def assert_dicts_equal(actual: dict, expected: dict, ignored_keys: List[str] = None):
    ignored_keys = ignored_keys or []
    errors = []
    for prop in expected:
        if prop in ignored_keys:
            continue
        try:
            res = glom.glom(actual, prop)
            if expected[prop] != res:
                errors.append(f"Invalid property [{prop}] value, expected [{expected[prop]}], actual [{res}]")
        except PathAccessError:
            errors.append(f"Property [{prop}] is absent in actual dictionary")

    assert not errors, "\n".join(errors)

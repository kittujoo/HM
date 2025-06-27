from deepdiff import DeepDiff


def assert_object_equal(json_1, json_2, **kwargs):
    """
    Comparing 2 objects for equality using deepdiff library
    @param: str_list1 - Testdata endpoint list string, str_list2 - Rest API JSON response string
    @returns: True/False
    """
    # compare json strings
    kwargs.setdefault("ignore_order", True)
    diff = DeepDiff(json_1, json_2, **kwargs)
    if diff:
        raise AssertionError(f"Difference found in endpoints and json response:\n{diff.to_json(indent=4)}")

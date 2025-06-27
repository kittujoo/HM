from utilities.string_utility import str_to_bool, str_to_int


def string_converter(value):
    return value


CONVERTERS = {
    "str": string_converter,
    "bool": str_to_bool,
    "int": str_to_int
}

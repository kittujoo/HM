from csv import reader
from io import StringIO

from pytest_bdd import parsers

from utilities.convertion_utilities import parse_string_to_obj


class HeadlessDataTable:
    """
    Class to parse a headless table string into a list of lists
    """

    def __call__(self, table, *args, **kwargs):
        self._parse_table(table)
        return self

    def _parse_table(self, table):
        self.data = []
        for row in reader(StringIO(table), delimiter='|'):
            parsed_row = [v.strip() for v in row if v.strip() != '']
            self.data.append(parsed_row)

    def as_dict(self, horizontal=False, convert=False):

        if horizontal:
            if len(self.data) != 2:
                raise ValueError("To convert horizontal table to dict table should have 2 rows")
            result = dict(zip(self.data[0], self.data[1]))
        else:
            result = dict(self.data)
            if len(result) != len(self.data):
                raise ValueError("Table contains duplicated keys")

        if convert:
            result = {key: parse_string_to_obj(value) for key, value in result.items()}

        return result

    def __iter__(self):
        return iter(self.data)


def headlesstable(name, fixture="table"):
    """
    :param name: step definition name
    :param fixture: name of the fixture that should be used in step definition as a consumer of table data
    :return:
    """
    formatted_str = "{name}\n{{{fixture}:HeadlessDataTable}}".format(
        name=name,
        fixture=fixture,
    )

    return parsers.cfparse(formatted_str, extra_types=dict(HeadlessDataTable=HeadlessDataTable()))

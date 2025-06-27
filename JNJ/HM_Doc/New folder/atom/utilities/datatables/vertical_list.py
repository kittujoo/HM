from csv import reader
from io import StringIO

from pytest_bdd import parsers


class VerticalListTable:
    """
    Class to parse a headless table string into a list of lists
    """

    def __init__(self, table):
        self.data = []
        for row in reader(StringIO(table), delimiter='|'):
            parsed_row = [v.strip() for v in row if v.strip() != '']
            if len(parsed_row) != 1:
                raise ValueError("There should be only one item in list table per row")
            self.data.append(parsed_row[0])

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


def verticallist(name, fixture="table"):
    formatted_str = "{name}\n{{{fixture}:VerticalListTable}}".format(
        name=name,
        fixture=fixture,
    )

    return parsers.cfparse(formatted_str, extra_types=dict(VerticalListTable=VerticalListTable))

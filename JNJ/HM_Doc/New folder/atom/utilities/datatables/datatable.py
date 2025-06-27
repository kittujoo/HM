from csv import DictReader
from io import StringIO

from pytest_bdd import parsers


class DataTable:
    """
    Class to parse a table string with headers into a list of maps
    """

    def __init__(self, table):
        self.data = []
        for row in DictReader(StringIO(table), delimiter='|'):
            parsed_row = {h.strip(): v.strip() for h, v in row.items() if h.strip() != ''}
            self.data.append(parsed_row)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


def datatable(name, fixture="table"):
    formatted_str = "{name}\n{{{fixture}:DataTable}}".format(
        name=name,
        fixture=fixture,
    )

    return parsers.cfparse(formatted_str, extra_types=dict(DataTable=DataTable))

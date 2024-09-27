import csv
from prettytable import PrettyTable
from functools import wraps


def display_csv_as_table(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        csv_data = func(*args, **kwargs)

        # Create a PrettyTable object
        table = PrettyTable()

        # Read CSV data
        reader = csv.reader(csv_data.splitlines())
        headers = next(reader)
        table.field_names = headers

        for row in reader:
            table.add_row(row)

        print(table)

    return wrapper

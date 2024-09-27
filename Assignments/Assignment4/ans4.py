# 04. open a csv file, decorator should display the data from the csv file in a prettytable

import csv
from prettytable import PrettyTable

def csv_to_prettytable_decorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if data:
            table = PrettyTable()
            table.field_names = data[0].keys()
            for row in data:
                table.add_row(row.values())
            print(table)
        else:
            print("No data found.")
    return wrapper

@csv_to_prettytable_decorator
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

if __name__ == "__main__":
    read_csv('example.csv')

from ans2_csv_decorator import display_csv_as_table

@display_csv_as_table
def get_csv_data():
    """Simulated CSV data retrieval."""
    return """Name, Age, Occupation
John, 30, Engineer
Jane, 25, Designer
Doe, 22, Artist"""

if __name__ == "__main__":
    get_csv_data()

"""Dictionary related utility functions."""

__author__ = "730460892"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_given: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Column with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    if len(data_given) <= rows:
        return data_given
    for column in data_given:
        first_values: list[str] = []
        i: int = 0
        while i < rows:
            first_values.append(data_given[column][i])
            i += 1
        result[column] = first_values

    return result


def select(table_data: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """New table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in col_names:
        result[column] = table_data[column]
    
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Dictionary of two seperate dictionaries combined."""
    result: dict[str, list[str]] = {}
    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in result:
            result[column] = result[column] + (table_two[column]) 
        else:
            result[column] = table_two[column]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the amount of times a value appeared in the input list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else: 
            result[value] = 1
    
    return result

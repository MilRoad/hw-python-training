"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Function reads input line-by-line and returns a tuple with the max and min value.

    Args:
        file_name: The name of input file.

    Returns:
        The tuple with the max and min values.

    """
    list_value = []
    with open(file_name) as fi:
        for line in fi:
            list_value.append(int(line))
    return min(list_value), max(list_value)

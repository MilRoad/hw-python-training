import os
from typing import Tuple

import pytest

from homework1.tasks.task3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/files/test1.txt", (1, 8)),
        (os.path.abspath(os.path.dirname(__file__)) + "/files/test2.txt", (-1, 97)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result

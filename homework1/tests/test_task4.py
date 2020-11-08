from typing import List

import pytest

from homework1.tasks.task4 import check_sum_of_four


@pytest.mark.parametrize(
    ["a_value", "b_value", "c_value", "d_value", "expected_result"],
    [
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        ([1, 1], [-1, 1], [-1, 1], [1, -1], 6),
        ([1, 1, 3], [-1, 5, 1], [-1, -5, 1], [8, 1, -1], 10),
    ],
)
def test_check_sum_of_four(
    a_value: List[int],
    b_value: List[int],
    c_value: List[int],
    d_value: List[int],
    expected_result: int,
):
    actual_result = check_sum_of_four(a_value, b_value, c_value, d_value)

    assert actual_result == expected_result

from typing import List

import pytest

from homework1.tasks.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums_value", "k_value", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([2, 3, -5, 7, 8, -9], 2, 15),
        ([2, 4, -2, 0], -2, 0),
    ],
)
def test_find_maximal_subarray_sum(
    nums_value: List[int], k_value: int, expected_result: bool
):
    actual_result = find_maximal_subarray_sum(nums_value, k_value)

    assert actual_result == expected_result

"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Checks if the given sequence is a Fibonacci sequence.

    Args:
        data: The sequence of integers.

    Returns:
        True if the given sequence is a Fibonacci sequence, False otherwise.

    """
    if len(data) < 3:
        return False
    else:
        a, b, c = data[0], data[1], data[2]
        if a != 0 and b != 1 and c != 1:
            return False
        else:
            while len(data) >= 3:
                if not a + b == c:
                    return False
                if len(data) > 3:
                    a, b, c = b, c, data[3]
                data = data[1:]

            return True

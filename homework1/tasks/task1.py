def check_power_of_2(a: int) -> bool:
    """Checks if a number is a power of 2.

    Args:
        a: The number.

    Returns:
        True if a number is a power of 2, False otherwise.

    """
    if a <= 0:
        return False
    else:
        return not (bool(a & (a - 1)))

def check_power_of_2(a: int) -> bool:
    """Function checks if a number is a power of 2.

    Args:
        a: The number.

    Returns:
        The return value. True for success, False otherwise.

    """
    return not (bool(a & (a - 1)))

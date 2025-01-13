def add(numbers: str) -> int:
    """
    This function takes a string of numbers separated by commas and returns their sum.
    params:
        numbers: str: A string of numbers separated by commas.
    returns:
        int: The sum of the numbers.
    """
    if numbers == '':
        return 0

    if len(numbers) == 1:
        return int(numbers)

    pass

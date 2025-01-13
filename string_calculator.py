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

    nums = numbers.split(',')
    if len(nums) == 1:
        return int(nums)

    pass

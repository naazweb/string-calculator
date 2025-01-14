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

    if '\n' in numbers:
        numbers = numbers.replace('\n', ',')

    nums = list(map(int, numbers.split(',')))
    if len(nums) == 1:
        return nums[0]

    return sum(nums)

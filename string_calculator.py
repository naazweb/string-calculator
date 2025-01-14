from typing import List


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

    # split and get numbers as integers
    nums = get_int_numbers(numbers)

    if len(nums) == 1:
        return nums[0]

    # check for negative numbers
    negatives = [str(num) for num in nums if num < 0]
    if negatives:
        raise ValueError(
            f'negative numbers not allowed: {", ".join(negatives)}')

    return add_nums(nums)


def get_int_numbers(numbers: str) -> List[int]:
    """
    This function takes a string of numbers separated by some delimiter and returns a list of integers.
    params:
        numbers: str: A string of numbers separated by some delimiter.
    returns:
        list[int]: A list of integers.
    """
    # default delimiters
    delimiters = [',', '\n']
    # check if the string has a custom delimiter
    if numbers.startswith('//'):
        # split at first \n
        delimiter, numbers = numbers.split('\n', 1)
        # check if the delimiter is multiple characters
        if delimiter.startswith('//['):
            # check if there are multiple delimiters
            if delimiter.count('[') > 1:
                delimiters.extend(delimiter[3:-1].split(']['))
            else:
                delimiters.append(delimiter[3:-1])
        else:
            delimiters.append(delimiter[2:])

    # replace all delimiter with a comma
    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ',')

    return list(map(int, numbers.split(',')))


def add_nums(nums: List[int]) -> int:
    """
    This function takes a list of numbers and returns their sum.
    params:
        nums: list[int]: A list of numbers.
    returns:
        int: The sum of the numbers.
    """
    # check for large numbers above 1000
    nums = [num for num in nums if num <= 1000]
    return sum(nums)

from typing import List, Tuple


def get_delimiters(numbers: str) -> Tuple[List[str], str]:
    """
    This function takes a string of numbers separated by some delimiter and returns a list of delimiters.
    params:
        numbers: str: A string of numbers separated by some delimiter.
    returns:
        list[str]: A list of delimiters.
    """
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
    return delimiters, numbers
    

def get_numbers_at_indexes(numbers: List[int], indexes: str) -> List[int]:
    """
    This function takes a string of numbers separated by some delimiter and a string of indexes and returns a list of integers at those indexes.
    params:
        numbers: str: A string of numbers separated by some delimiter.
        indexes: str: A string of indexes.
    returns:
        list[int]: A list of integers at the specified indexes.
    """
    if indexes == 'E':
        return numbers[::2]
    elif indexes == 'O':
        return numbers[1::2]
    

def get_int_numbers(numbers: str) -> List[int]:
    """
    This function takes a string of numbers separated by some delimiter and returns a list of integers.
    params:
        numbers: str: A string of numbers separated by some delimiter.
    returns:
        list[int]: A list of integers.
    """
    # default delimiters
    # check if mentions E or O
    index_specified = False

    if numbers.startswith('E') or numbers.startswith('O'):
        index_specified = True
        use_indexes = numbers[0]
        numbers = numbers[1:]
   
    delimiters, numbers = get_delimiters(numbers)

    # replace all delimiter with a comma
    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ',')

    all_numbers = list(map(int, numbers.split(',')))
    if index_specified:
        all_numbers = get_numbers_at_indexes(all_numbers, use_indexes)
    return all_numbers


def add_nums(nums: List[int]) -> int:
    """
    This function takes a list of numbers and returns their sum.
    params:
        nums: list[int]: A list of numbers.
    returns:
        int: The sum of the numbers.
    """
    # check for large numbers above 500 and below 1000 and ignore them
    nums = [num for num in nums if (num<=500 or num >= 1000)]
    return sum(nums)


def add(numbers: str) -> int:
    """
    This function takes a string of numbers separated by commas and returns their sum.
    params:
        numbers: str: A string of numbers separated by commas.
    returns:
        int: The sum of the numbers.
    """
    # check if the string is empty -> return 0
    if numbers == '':
        return 0

    # split and get numbers as integers
    nums = get_int_numbers(numbers)

    # check if there is only one number -> return the number
    if len(nums) == 1:
        return nums[0]

    # check for negative numbers -> raise an error
    negatives = [str(num) for num in nums if num < 0]
    if negatives:
        raise ValueError(
            f'negative numbers not allowed: {", ".join(negatives)}')

    # return the sum of the numbers
    return add_nums(nums)

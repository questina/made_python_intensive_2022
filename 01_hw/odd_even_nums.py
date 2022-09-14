from typing import List, Tuple


def split_odd_even(nums: List[int]) -> Tuple[List[int], List[int]]:
    """
    This function splits given array into two,
    containing only odd and only even elements of input array
    :param nums: list of numbers;
    :return: tuple of two lists of even and odd elements of input array
    """
    odd_nums = []
    even_nums = []
    for num in nums:
        if num == 0:
            # 0 is not odd or even
            continue
        if num % 2 == 0:
            # if num is even add it to list of evens
            even_nums.append(num)
        elif num % 2 == 1:
            # if num is odd add it to list of odds
            odd_nums.append(num)
        else:
            continue

    return even_nums, odd_nums

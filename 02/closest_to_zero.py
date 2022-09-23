from typing import List


def closest_to_zero(nums: List[int]) -> List[int]:
    """
    This function finds elements of input array, which are closest to zero
    :param nums: array of numbers
    :return: array of elements of input array, that are closest to zero
    """
    res = []
    if len(nums) == 0:
        return res
    cur_closest = max(nums)
    for i in range(len(nums)):
        if abs(nums[i]) < cur_closest:
            res = [nums[i]]
            cur_closest = abs(nums[i])
        elif abs(nums[i]) == cur_closest:
            res.append(nums[i])
        else:
            continue

    return res

from typing import List


def merge(sorted_arr1: List[int], sorted_arr2: List[int]) -> List[int]:
    """
    This function merges two sorted arrays into one
    :param sorted_arr1: first sorted array
    :param sorted_arr2: second sorted array
    :return: new array of elements that both input arrays has without duplicates
    """
    res_arr = []
    if len(sorted_arr1) == 0 or len(sorted_arr2) == 0:
        return res_arr
    idx1, idx2 = 0, 0
    while idx1 < len(sorted_arr1) and idx2 < len(sorted_arr2):
        if sorted_arr1[idx1] < sorted_arr2[idx2]:
            idx1 += 1
        elif sorted_arr2[idx2] < sorted_arr1[idx1]:
            idx2 += 1
        else:
            if sorted_arr1[idx1] not in set(res_arr):
                res_arr.append(sorted_arr1[idx1])
            idx1 += 1
            idx2 += 1
    while idx1 < len(sorted_arr1):
        if sorted_arr1[idx1] == sorted_arr2[idx2 - 1]:
            res_arr.append(sorted_arr1[idx1])
        idx1 += 1
    while idx2 < len(sorted_arr2):
        if sorted_arr2[idx2] == sorted_arr1[idx1 - 1]:
            res_arr.append(sorted_arr2[idx2])
        idx2 += 1

    return res_arr

import subprocess
import unittest
from parameterized import parameterized

from custom_list import CustomList
from utils_for_test import compare_custom_lists


class TestCustomList(unittest.TestCase):
    @parameterized.expand([
        ["basic_list", [1, 2, 3, 4], "1 2 3 4 10"],
        ["empty_list", [], "0"],
    ])
    def test_print(self, name, init_list, res_print):
        custom_l = CustomList(init_list)
        line = subprocess.run(
            [
                'python3',
                '-c',
                'from custom_list import CustomList;'
                'print(CustomList([' + ",".join(str(elem) for elem in custom_l) + ']))',
            ],
            text=True,
            capture_output=True,
        ).stdout
        assert line.strip() == res_print

    def test_equal(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 3])
        list3 = CustomList([1, 2, 3, 4])
        assert list1 == list2
        assert (list1 == list3) is False
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([3, 3]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_not_equal(self):
        list1 = CustomList([1, 2])
        list2 = CustomList([1, 1, 1])
        list3 = CustomList([1, 2, 3, 4])
        assert (list1 != list2) is False
        assert list1 != list3
        assert compare_custom_lists(list1, CustomList([1, 2]))
        assert compare_custom_lists(list2, CustomList([1, 1, 1]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_lower_than(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3])
        list3 = CustomList([1, 2, 3, 4])
        assert list2 < list1
        assert list1 < list3
        assert (list3 < list2) is False
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([3]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_lower_or_equal(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 4, 1])
        list3 = CustomList([1, 2, 3, 4])
        assert list1 <= list2
        assert list1 <= list3
        assert (list3 <= list2) is False
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([1, 4, 1]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_greater_than(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3])
        list3 = CustomList([1, 2, 3, 4])
        assert list1 > list2
        assert list3 > list1
        assert (list2 > list3) is False
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([3]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_greater_or_equal(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 4, 1])
        list3 = CustomList([1, 2, 3, 4])
        assert list2 >= list1
        assert list3 >= list1
        assert (list2 >= list3) is False
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([1, 4, 1]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_sum_custom(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        list3 = CustomList([1, 2, 3, 4])
        assert compare_custom_lists(list1 + list2, CustomList([2, 4, 6]))
        assert compare_custom_lists(list1 + list3, CustomList([2, 4, 6, 4]))
        assert compare_custom_lists(list3 + list1, CustomList([2, 4, 6, 4]))
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([1, 2, 3]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_sum_original(self):
        custom_list1 = CustomList([1, 2, 3])
        custom_list2 = CustomList([1, 2, 3, 4])
        original_list1 = [1, 2, 3]
        original_list2 = [1, 2, 3, 4]
        assert compare_custom_lists(custom_list1 + original_list1, CustomList([2, 4, 6]))
        assert compare_custom_lists(original_list1 + custom_list1, CustomList([2, 4, 6]))
        assert compare_custom_lists(custom_list1 + original_list2, CustomList([2, 4, 6, 4]))
        assert compare_custom_lists(original_list2 + custom_list1, CustomList([2, 4, 6, 4]))
        assert compare_custom_lists(custom_list2 + original_list1, CustomList([2, 4, 6, 4]))
        assert compare_custom_lists(original_list1 + custom_list2, CustomList([2, 4, 6, 4]))
        assert compare_custom_lists(custom_list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(custom_list2, CustomList([1, 2, 3, 4]))

    def test_sub_custom(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        list3 = CustomList([1, 2, 3, 4])
        assert compare_custom_lists(list1 - list2, CustomList([0, 0, 0]))
        assert compare_custom_lists(list1 - list3, CustomList([0, 0, 0, -4]))
        assert compare_custom_lists(list3 - list1, CustomList([0, 0, 0, 4]))
        assert compare_custom_lists(list1, CustomList([1, 2, 3]))
        assert compare_custom_lists(list2, CustomList([1, 2, 3]))
        assert compare_custom_lists(list3, CustomList([1, 2, 3, 4]))

    def test_sub_original(self):
        custom_list1 = CustomList([1, 4, 7])
        custom_list2 = CustomList([1, 4, 7, 4])
        original_list1 = [1, 2, 3]
        original_list2 = [1, 2, 3, 4]
        assert compare_custom_lists(custom_list1 - original_list1, CustomList([0, 2, 4]))
        assert compare_custom_lists(original_list1 - custom_list1, CustomList([0, -2, -4]))
        assert compare_custom_lists(custom_list1 - original_list2, CustomList([0, 2, 4, -4]))
        assert compare_custom_lists(original_list2 - custom_list1, CustomList([0, -2, -4, 4]))
        assert compare_custom_lists(custom_list2 - original_list1, CustomList([0, 2, 4, 4]))
        assert compare_custom_lists(original_list1 - custom_list2, CustomList([0, -2, -4, -4]))
        assert compare_custom_lists(custom_list1, CustomList([1, 4, 7]))
        assert compare_custom_lists(custom_list2, CustomList([1, 4, 7, 4]))

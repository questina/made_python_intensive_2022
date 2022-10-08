from custom_list import CustomList
import subprocess


def test_print(l):
    line = subprocess.run(
        [
            'python3',
            '-c',
            'from custom_list import CustomList;print(CustomList([' + ",".join(str(elem) for elem in l) + ']))',
        ],
        text=True,
        capture_output=True,
    ).stdout
    return line.strip()


def compare_custom_lists(l1, l2):
    if len(l1) != len(l2):
        return False
    i = 0
    while i < len(l1):
        if l1[i] != l2[i]:
            return False
        i += 1
    return True


def run_test():
    list1 = CustomList([1, 2, 3])
    list2 = CustomList([5, 6, 7, 8])
    assert list1 < list2
    assert list1 <= list2
    assert (list1 > list2) is False
    assert (list1 >= list2) is False
    assert list1 != list2
    assert (list1 == list2) is False
    assert list1 == list1
    assert compare_custom_lists(CustomList([6, 8, 10, 8]), list1 + list2)
    assert compare_custom_lists(CustomList([4, 4, 4, 8]), list2 - list1)
    assert compare_custom_lists(CustomList([-3, -1, 1, -1, 0]), list1 - [4, 3, 2, 1, 0])
    assert compare_custom_lists(CustomList([5, 14, 23, 32]), [10, 20, 30, 40] - list2)
    assert compare_custom_lists(CustomList([2, 4, 6, 4, 5]), list1 + [1, 2, 3, 4, 5])
    assert compare_custom_lists(CustomList([0, 0, 7, 8]), [-5, -6] + list2)
    assert "1 2 3 4 10" == test_print(CustomList([1, 2, 3, 4]))
    assert "0" == test_print(CustomList([]))


if __name__ == "__main__":
    run_test()

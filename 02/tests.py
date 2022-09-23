from closest_to_zero import closest_to_zero
from merge_arrays import merge


def run_test_closest_to_zero():
    assert closest_to_zero([-5, 9, 6, -8]) == [-5]
    assert closest_to_zero([-1, 2, -5, 1, -1]) == [-1, 1, -1]
    assert closest_to_zero([-2, -1, 0, 1, 2]) == [0]
    assert closest_to_zero([-1, -1, -1, -1, 1, 1, 1, 1]) == [-1, -1, -1, -1, 1, 1, 1, 1]
    assert closest_to_zero([]) == []
    assert closest_to_zero([-5, 5, 10, -10, 2, 4, 2, 9, -4]) == [2, 2]


def run_test_merge_arrays():
    assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
    assert merge([-3, -2, -1, 0, 1, 2, 3, 4], [-1, 0, 1, 4]) == [-1, 0, 1, 4]
    assert merge([], [-1, 0, 1, 4]) == []
    assert merge((), [-1, 0, 1, 4]) == []
    assert merge([-1, 0, 1, 4], []) == []
    assert merge([-1, 0, 1, 4], ()) == []


def run_tests():
    run_test_closest_to_zero()
    run_test_merge_arrays()


if __name__ == "__main__":
    run_tests()

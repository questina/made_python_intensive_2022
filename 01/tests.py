from quadratic_equation import solve_quad_eq
from odd_even_nums import split_odd_even
from math import isclose


def test_quad_eq():
    assert solve_quad_eq(0, 0, 0) is None
    assert solve_quad_eq(0, 100, 101) is None
    assert (
            len(solve_quad_eq(1, -5, 4)) == 2
            and (
                    isclose(solve_quad_eq(1, -5, 4)[0], 1)
                    and isclose(solve_quad_eq(1, -5, 4)[1], 4)
            ) or (
                    isclose(solve_quad_eq(1, -5, 4)[1], 4)
                    and isclose(solve_quad_eq(1, -5, 4)[0], 1)
            )
    )
    assert (
                   solve_quad_eq(9 / 5, 6, 5) is not None
                   and len(solve_quad_eq(9 / 5, 6, 5)) == 1
                   and isclose(-30 / 18, solve_quad_eq(9 / 5, 6, 5)[0])
    )
    assert (
                   solve_quad_eq(1, -1 / 2, -3) is not None
                   and len(solve_quad_eq(1, -1 / 2, -3)) == 2
                   and isclose(solve_quad_eq(1, -1 / 2, -3)[1], 2)
                   and isclose(-1.5, solve_quad_eq(1, -1 / 2, -3)[0])
            )
    assert solve_quad_eq(1, 0, 4) is None
    assert (
            len(solve_quad_eq(1, 0, -4)) == 2
            and (
                    isclose(solve_quad_eq(1, 0, -4)[0], -2)
                    and isclose(solve_quad_eq(1, 0, -4)[1], 2)
            ) or (
                    isclose(solve_quad_eq(1, 0, -4)[1], -2)
                    and isclose(solve_quad_eq(1, 0, -4)[0], 2)
            )
    )
    assert (
            len(solve_quad_eq(1, 1, 0)) == 2
            and (
                    isclose(solve_quad_eq(1, 1, 0)[0], -1)
                    and isclose(solve_quad_eq(1, 1, 0)[1], 0)
            ) or (
                    isclose(solve_quad_eq(1, 1, 0)[1], -1)
                    and isclose(solve_quad_eq(1, 1, 0)[0], 0)
            )
    )
    assert (
            solve_quad_eq(13, 0, 0) is not None
            and len(solve_quad_eq(13, 0, 0)) == 1
            and isclose(solve_quad_eq(13, 0, 0)[0], 0)
    )

    print("Tests for quadratic equation are passed !")


def test_odd_even():
    assert split_odd_even([0, 0, 0, 0, 0, 0]) == ([0, 0, 0, 0, 0, 0], [])
    assert split_odd_even([0, 1, 2, 3, 4, 5, 6, 7, 8]) == ([0, 2, 4, 6, 8], [1, 3, 5, 7])
    assert split_odd_even([]) == ([], [])
    assert split_odd_even([1, 3, 5, 7, 9]) == ([], [1, 3, 5, 7, 9])
    assert split_odd_even([2, 4, 6, 8, 10]) == ([2, 4, 6, 8, 10], [])
    assert split_odd_even([-1, -2, -3, -4, -5, -6, -7, -8]) == ([-2, -4, -6, -8], [-1, -3, -5, -7])
    assert split_odd_even([-1.5, -1, -0.5, 0, 0.5, 1, 1.5]) == ([0], [-1, 1])

    print("Tests for odd even split are passed !")


if __name__ == '__main__':
    test_quad_eq()
    test_odd_even()

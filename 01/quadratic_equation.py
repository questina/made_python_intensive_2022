from typing import Union, Tuple
from math import sqrt, isclose


def solve_quad_eq(a: float, b: float, c: float) -> Union[None, Tuple[float], Tuple[float, float]]:
    """
    This function finds real roots for quadratic equation ax^2 + bx + c = 0 by discriminant
    :param a: coefficient of equation, called the quadratic coefficient (a != 0);
    :param b: coefficient of equation, called the linear coefficient;
    :param c: coefficient of equation, called the constant or free term;
    :return: list of roots or None if real roots do not exist or if the quadratic coefficient equals to 0.
    """

    # if a == 0, when it is not a quadratic equation
    if a == 0:
        return None
    # count discriminant of quadratic equation
    d = b ** 2 - 4 * a * c
    if isclose(d, 0):
        # if discriminant equals to zero when where is only one real root
        return -b / (2 * a),
    elif d > 0:
        # if discriminant greater than zero when where is two real roots
        return (-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
    else:
        # if discriminant less than zero when where is no real roots
        return None

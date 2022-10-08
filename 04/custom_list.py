"""
Module for class CustomList
"""


class CustomList(list):
    """
    Class that adds functionality to list to perform
    summation and subtraction on lists and compare the sums of elements
    """

    def __add__(self, other):
        res = CustomList()
        i = 0
        while i < len(self) and i < len(other):
            res.append(self[i] + other[i])
            i += 1
        while i < len(self):
            res.append(self[i])
            i += 1
        while i < len(other):
            res.append(other[i])
            i += 1
        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        res = CustomList()
        i = 0
        while i < len(self) and i < len(other):
            res.append(self[i] - other[i])
            i += 1
        while i < len(self):
            res.append(self[i])
            i += 1
        while i < len(other):
            res.append(-1 * other[i])
            i += 1
        return res

    def __rsub__(self, other):
        return CustomList(other).__sub__(self)

    def __str__(self):
        return " ".join(str(elem) for elem in self) + " " + str(sum(self))

    def __le__(self, other):
        return sum(self).__le__(sum(other))

    def __lt__(self, other):
        return sum(self).__lt__(sum(other))

    def __eq__(self, other):
        return sum(self).__eq__(sum(other))

    def __ne__(self, other):
        return sum(self).__ne__(sum(other))

    def __gt__(self, other):
        return sum(self).__gt__(sum(other))

    def __ge__(self, other):
        return sum(self).__ge__(sum(other))

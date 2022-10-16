"""
This module contains base classes
to implement methods to read and write
different data types
"""


class BaseReader:
    """
    Base class to implement method
    to read different data types
    """

    def read(self, file, **params):
        """
        This method reads different data types
        :param file: input file
        :param params: parameters, needed to process files
        :return: data from file
        """
        raise NotImplementedError


class BaseWriter:
    """
    Base class to implement method
    to write different data types
    """

    def dump(self, data, file, **params):
        """
        This method writes data into different data types
        :param data: data with needed type
        :param file: output file
        :param params: parameters, needed to process files
        :return: None
        """
        raise NotImplementedError

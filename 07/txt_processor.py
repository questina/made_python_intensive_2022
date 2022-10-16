"""
This module has classes TxtReader and TetWriter,
that implements methods read and dump
of classes BaseReader and BaseWriter for txt format files
"""
from base_processor import BaseReader, BaseWriter


class TxtReader(BaseReader):
    """
    This class inherits from BaseReader
    and implements method to read txt format files
    """

    def read(self, file, **params):
        contents = []
        for line in file.readlines(**params):
            contents.append(line)
        return contents


class TxtWriter(BaseWriter):
    """
    This class inherits from BaseWriter
    and implements method to write data into txt format files
    """

    def dump(self, data, file, **params):
        for line in data:
            file.write(line, **params)

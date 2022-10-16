"""
This module has classes JsonReader and JsonWriter,
that implements methods read and dump
of classes BaseReader and BaseWriter for json format files
"""
import json

from base_processor import BaseReader, BaseWriter


class JsonReader(BaseReader):
    """
    This class inherits from BaseReader
    and implements method to read json format files
    """
    def read(self, file, **params):
        data = json.load(file, **params)
        return data


class JsonWriter(BaseWriter):
    """
    This class inherits from BaseWriter
    and implements method to write data into json format files
    """
    def dump(self, data, file, **params):
        json.dump(data, file, **params)

"""
This module has classes CSVReader and CSVWriter,
that implements methods read and dump
of classes BaseReader and BaseWriter for csv format files
"""
import csv

from base_processor import BaseReader, BaseWriter


class CSVReader(BaseReader):
    """
    This class inherits from BaseReader
    and implements method to read csv format files
    """
    def read(self, file, **params):
        csv_reader = csv.reader(file, **params)
        contents = []
        for row in csv_reader:
            contents.append(row)
        return contents


class CSVWriter(BaseWriter):
    """
    This class inherits from BaseWriter
    and implements method to write data into csv format files
    """
    def dump(self, data, file, **params):
        csv_writer = csv.writer(file, **params)
        for row in data:
            csv_writer.writerow(row)

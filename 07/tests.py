import unittest
import io

from json_processor import JsonReader, JsonWriter
from csv_processor import CSVReader, CSVWriter
from txt_processor import TxtReader, TxtWriter
from read_generator import read_and_filter
from test_utils import txt_text, csv_text, json_text


def read_data(fileobj, reader, **kwargs):
    return reader.read(fileobj, **kwargs)


def dump_data(data, fileobj, writer, **kwargs):
    writer.dump(data, fileobj, **kwargs)


class TestPreprocessors(unittest.TestCase):

    def test_txt(self):
        input = io.StringIO()
        input.write("".join(txt_text))
        input.seek(0)
        data = read_data(input, reader=TxtReader())
        assert data == txt_text
        input.close()

        output = io.StringIO()
        dump_data(txt_text, output, writer=TxtWriter())
        assert "".join(txt_text) == output.getvalue()

    def test_csv(self):
        input = io.StringIO()
        input.write("\n".join([",".join(elem) for elem in csv_text]))
        input.seek(0)
        data = read_data(input, reader=CSVReader())
        assert data == csv_text

        output = io.StringIO()
        dump_data(csv_text, output, writer=CSVWriter(), lineterminator="\n")
        assert "\n".join([",".join(elem) for elem in csv_text]) + "\n" == output.getvalue()

    def test_json(self):
        input = io.StringIO()
        input.write(str(json_text).replace("\'", "\""))
        input.seek(0)
        data = read_data(input, reader=JsonReader())
        assert data == json_text

        output = io.StringIO()
        dump_data(json_text, output, writer=JsonWriter())
        assert str(json_text).replace("\'", "\"") == output.getvalue()


class TestFilter(unittest.TestCase):

    def test_small_file(self):
        input = io.StringIO()
        input.write("\n".join(txt_text))
        input.seek(0)
        res = []
        for line in read_and_filter(input, ["ICE"]):
            res.append(line)

        assert res == ['Some say in ice\n', 'To say that for destruction ice\n']
        assert "But if it had to perish twice,\n" not in res

    def test_empty_file(self):
        input = io.StringIO()
        res = []
        for line in read_and_filter(input, ["ice"]):
            res.append(line)

        assert not res

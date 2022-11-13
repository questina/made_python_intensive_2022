import os
import sys
import unittest
from unittest import mock
from threading import Thread
from server import Server
from client import Client

REAL_URLS_FILE = "urls.txt"
TEST_URLS_FILE = "urls_test.txt"
TEST_URLS_ANSWER = {"https://en.wikipedia.org/wiki/Oraison": "{'the': 22, 'of': 16, 'with': 10, "
                                                             "'is': 10, 'La': 10, 'in': 8, 'Le': 8, "
                                                             "'to': 7, 'Oraison': 6, 'from': 6}",
                    "https://en.wikipedia.org/wiki/Johnny_Cymbal": "{'—': 209, 'the': 31, 'of': 21, 'and': 18, "
                                                                   "'with': 16, 'a': 15, 'Cymbal': 14, "
                                                                   "'in': 13, '^': 13, 'Retrieved': 13}",
                    "https://en.wikipedia.org/wiki/First_Inauguration_of_Uhuru_Kenyatta": "{'the': 107, 'of': 70, "
                                                                                          "'March': 50, "
                                                                                          "'2013.': 49, 'to': 45, "
                                                                                          "'and': 44, "
                                                                                          "'President': 38, "
                                                                                          "'Kenyatta': 28, 'on': 28, "
                                                                                          "'^': 23}",
                    "https://en.wikipedia.org/wiki/Blackburn_Law_F.C.": "{'the': 43, 'Blackburn': 42, 'and': 20, "
                                                                        "'in': 19, "
                                                                        "'of': 17, 'to': 16, '^': 16, 'F.C.': 14, "
                                                                        "'club': 13, 'Darwen': 13}",
                    "https://en.wikipedia.org/wiki/Jabrill_Peppers": "{'the': 156, 'Peppers': 99, 'in': 65, "
                                                                     "'of': 65, 'a': 65, 'and': 62, '^': 56, "
                                                                     "'Retrieved': 43, 'was': 42, 'to': 37}"}


class TestThreading(unittest.TestCase):
    def test_client(self):
        res = {}
        s = Server(workers_num=2)
        t = Thread(target=s.run)
        c = Client(workers_num=2)
        with open(TEST_URLS_FILE, "w+") as test_f:
            for url in TEST_URLS_ANSWER:
                test_f.write(url + "\n")
        t.start()
        with mock.patch("builtins.print") as mock_print:
            c.connect(TEST_URLS_FILE)
            t.join()
            for call in mock_print.call_args_list:
                if call.args[0].startswith("Processed"):
                    continue
                else:
                    res[call.args[0].split()[0]] = call.args[0]
        assert len(TEST_URLS_ANSWER) == len(res)
        for url in TEST_URLS_ANSWER:
            assert url in res
            assert res[url] == url + " " + TEST_URLS_ANSWER[url]
        os.remove(TEST_URLS_FILE)

    def test_server(self):
        res = []
        s = Server(workers_num=3)
        t = Thread(target=s.run)
        c = Client(workers_num=5)
        t.start()
        with mock.patch("builtins.print") as mock_print:
            c.connect(REAL_URLS_FILE)
            t.join()
            for call in mock_print.call_args_list:
                if call.args[0].startswith("Processed"):
                    res.append(call.args[0])
        urls_cnt = 0
        with open(REAL_URLS_FILE, "r") as urls_file:
            for _ in urls_file.readlines():
                urls_cnt += 1
        assert len(res) == urls_cnt
        for i in range(urls_cnt):
            assert f"Processed {i + 1}" in res

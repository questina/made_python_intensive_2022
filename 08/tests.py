import unittest
from find_anagrams import find_anagrams


class TestAnagrams(unittest.TestCase):

    def test_empty(self):
        assert not find_anagrams("", "aaa")
        assert not find_anagrams("aaa", "")
        assert not find_anagrams("", "")

    def test_no_anagrams(self):
        assert not find_anagrams("abcdefghijk", "lmn")
        assert not find_anagrams("aaaaaaaaaaa", "bbb")
        assert not find_anagrams("aaaaaa", "aaaaaaaaaaaa")

    def test_correct_anagrams(self):
        assert not find_anagrams("abcba", "abc")
        assert not find_anagrams("aaa", "a")
        assert not find_anagrams("abc cba xabcd", "abc")
        assert not find_anagrams("aaaaaaaaa", "a")
        assert not find_anagrams("aaaaaaaaa", "aa")

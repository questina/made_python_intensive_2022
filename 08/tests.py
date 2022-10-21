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
        assert find_anagrams("abcba", "abc") == [0, 2]
        assert find_anagrams("aaa", "a") == [0, 1, 2]
        assert find_anagrams("abc cba xabcd", "abc") == [0, 4, 9]
        assert find_anagrams("aaaaaaaaa", "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        assert find_anagrams("aaaaaaaaa", "aa") == [0, 1, 2, 3, 4, 5, 6, 7]

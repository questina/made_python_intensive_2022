import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_small_cache(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        assert cache.get("k3") is None
        assert cache.get("k2") == "val2"
        assert cache.get("k1") == "val1"

        cache.set("k3", "val3")

        assert cache.get("k3") == "val3"
        assert cache.get("k2") is None
        assert cache.get("k1") == "val1"

    def test_big_cache(self):
        cache = LRUCache(50)
        for i in range(50):
            cache.set(f"k_{i}", f"val_{i}")
        for _ in range(50):
            cache.set("k_1", "val_2")
        assert cache.get("k_3") == "val_3"
        assert cache.get("k_1") == "val_2"
        cache.set("k_50", "val_50")
        assert cache.get("k_0") is None
        assert cache.get("k_50") == "val_50"

    def test_one_size_cache(self):
        cache = LRUCache(1)
        cache.set("k_1", "val_1")
        assert cache.get("k_1") == "val_1"
        cache.set("k_2", "val_2")
        assert cache.get("k_1") is None
        assert cache.get("k_2") == "val_2"

    def test_change_existing_key(self):
        cache = LRUCache(10)
        cache.set("k_1", "val_1")
        cache.set("k_1", "val_2")
        assert cache.get("k_1") == "val_2"
        cache.set("k_2", "val_2")
        cache.set("k_3", "val_3")
        cache.set("k_1", "val_4")
        assert cache.get("k_2") == "val_2"
        assert cache.get("k_3") == "val_3"
        assert cache.get("k_1") == "val_4"

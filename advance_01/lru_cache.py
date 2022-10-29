import logging
import sys


class CacheNode:
    """
    This class is a basic node for LRUCache class
    """

    def __init__(self, node_key, node_val):
        logging.debug("Initialize new cache element with "
                      "key = %s and value = %s", node_key, node_val)
        self.key = node_key
        self.val = node_val
        self.next = None
        self.prev = None


class LRUCache:
    """
    This class implements LRUCache mechanism
    via LinkedList structure
    """

    def __init__(self, limit=42):
        if limit <= 0:
            logging.error("Incorrect LRU cache size = %s", limit)
            raise ValueError("Incorrect LRU cache size. "
                             "LRU cache size has to be larger than 0")
        logging.debug("Initialize LRU Cache with size = %s", limit)
        self.cache_dict = {}
        self.limit = limit
        self.recent_elem = None
        self.last_elem = None

    def get(self, key):
        """
        Method finds a value in cache based on a key and updates the cache
        :param key: value of the key to search in cache
        :return: value of a key or None if the key is not in the cache
        """
        logging.info("Method 'get' called with key = %s", key)
        if key in self.cache_dict:
            logging.debug("key = %s was found in LRU cache. "
                          "Refreshing its position in cache", key)
            cache_node = self.cache_dict[key]
            if len(self.cache_dict) == 1:
                logging.debug("key = %s was the first key in LRU cache", key)
                return self.cache_dict[key].val
            if cache_node.key == self.last_elem.key:
                logging.debug("key = %s was last element in LRU cache", key)
                self.last_elem.next.prev = None
                self.last_elem = self.last_elem.next
            elif cache_node.key == self.recent_elem.key:
                logging.debug("key = %s is the most recent element "
                              "in LRU cache. "
                              "Doing nothing with it", key)
                return self.cache_dict[key].val
            else:
                cache_node.prev.next = cache_node.next
                cache_node.next.prev = cache_node.prev
            cache_node.prev = self.recent_elem
            self.recent_elem.next = cache_node
            self.recent_elem = cache_node
            cache_node.next = None
            logging.debug("key = %s is found and refreshed in LRU cache", key)
            return self.cache_dict[key].val
        logging.debug("key = %s was not found in LRU cache. Done nothing", key)

    def set(self, key, value):
        """
        This method add new key or update value of key to the cache
        :param key: key
        :param value: value
        :return: None
        """
        logging.info("Method 'set' called with "
                     "key = %s and value = %s", key, value)
        new_node = CacheNode(key, value)
        if self.last_elem is None:
            self.recent_elem = new_node
            self.last_elem = new_node
            self.cache_dict[key] = new_node
        else:
            if key in self.cache_dict:
                logging.debug("key = %s is already in cache, "
                              "refresh its value from %s to %s",
                              key, self.cache_dict[key].val, value)
                self.cache_dict[key].val = value
                self.get(key)
            else:
                if len(self.cache_dict) == self.limit:
                    logging.debug("LRU cache is full, "
                                  "deleting last element with key = %s "
                                  "and value = %s",
                                  self.last_elem.key, self.last_elem.val)
                    self.cache_dict.pop(self.last_elem.key, None)
                    if self.last_elem.next is None:
                        self.last_elem = new_node
                    else:
                        self.last_elem = self.last_elem.next
                    self.last_elem.prev = None
                self.recent_elem.next = new_node
                new_node.prev = self.recent_elem
                self.recent_elem = new_node
                self.cache_dict[key] = new_node


def main(argv):
    print(argv)
    if "-s" in argv:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s:%(levelname)s:%(funcName)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
    else:
        logging.basicConfig(
            filename='cache.log',
            level=logging.DEBUG,
            format='%(asctime)s:%(levelname)s:%(funcName)s:  %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
    logging.info("LRUCache program has started")
    try:
        cache = LRUCache(-1)
    except ValueError as error:
        print(error)
    cache = LRUCache(2)
    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.get("k3")
    cache.get("k2")
    cache.get("k1")
    cache.set("k3", "val3")
    cache.get("k3")
    cache.get("k2")
    cache.get("k1")
    logging.info("LRUCache program has ended")


if __name__ == "__main__":
    main(sys.argv)

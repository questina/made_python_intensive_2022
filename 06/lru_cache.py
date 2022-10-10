class CacheNode:
    def __init__(self, node_key, node_val):
        self.key = node_key
        self.val = node_val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, limit=42):
        self.cache_dict = {}
        self.limit = limit
        self.recent_elem = None
        self.last_elem = None

    def get(self, key):
        if key in self.cache_dict:
            cache_node = self.cache_dict[key]
            if len(self.cache_dict) == 1:
                return self.cache_dict[key].val
            if cache_node.key == self.last_elem.key:
                self.last_elem.next.prev = None
                self.last_elem = self.last_elem.next
            elif cache_node.key == self.recent_elem.key:
                return self.cache_dict[key].val
            else:
                cache_node.prev.next = cache_node.next
                cache_node.next.prev = cache_node.prev
            cache_node.prev = self.recent_elem
            self.recent_elem.next = cache_node
            self.recent_elem = cache_node
            cache_node.next = None
            return self.cache_dict[key].val

    def set(self, key, value):
        new_node = CacheNode(key, value)
        if self.last_elem is None:
            self.recent_elem = new_node
            self.last_elem = new_node
            self.cache_dict[key] = new_node
        else:
            if key in self.cache_dict:
                self.cache_dict[key].val = value
                self.get(key)
            else:
                if len(self.cache_dict) == self.limit:
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

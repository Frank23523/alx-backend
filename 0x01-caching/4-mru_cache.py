#!/usr/bin/env python3
"""
MRUCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A Most Recently Used (MRU) caching system that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop()
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]
        self.mru_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]

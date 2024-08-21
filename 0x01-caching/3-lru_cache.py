#!/usr/bin/env python3
"""
LRUCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A Least Recently Used (LRU) caching system that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]
        self.lru_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]

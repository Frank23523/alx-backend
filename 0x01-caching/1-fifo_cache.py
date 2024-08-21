#!/usr/bin/env python3
"""
FIFOCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO caching system that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

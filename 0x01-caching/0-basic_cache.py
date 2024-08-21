#!/usr/bin/env python3
"""
BasicCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching
    """
    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

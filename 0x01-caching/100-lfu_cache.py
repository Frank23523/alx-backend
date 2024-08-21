#!/usr/bin/env python3
"""
LFUCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A Least Frequently Used (LFU) caching system that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super().__init__()
        self.freq_dict = {}
        self.lru_dict = {}

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.update_freq(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_freq_keys = [k for k, v in self.freq_dict.items()
                               if v == min(self.freq_dict.values())]
            if len(least_freq_keys) == 1:
                discard_key = least_freq_keys[0]
            else:
                discard_key = min(least_freq_keys,
                                  key=lambda x: self.lru_dict[x])
            print(f"DISCARD: {discard_key}")
            del self.cache_data[discard_key]
            del self.freq_dict[discard_key]
            del self.lru_dict[discard_key]
        self.update_freq(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.update_freq(key)
        return self.cache_data[key]

    def update_freq(self, key):
        """
        Updates the frequency and LRU of a key
        """
        if key in self.freq_dict:
            self.freq_dict[key] += 1
        else:
            self.freq_dict[key] = 1
        self.lru_dict[key] = len(self.lru_dict)

#!/usr/bin/env python3
"""
Module for defining a cache eviction policy
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU eviction policy class implementation that inherits
    from BaseCaching
    """

    def __init__(self):
        """
        Initialises the class and its super class
        """
        super().__init__()
        self.access_count = {}

    def put(self, key, item):
        """
        Assigns key-value/item pair to a self.cache_data
        """
        if key is None or item is None:
            return
        if self.cache_data.__len__() >= self.MAX_ITEMS:
            least_used = min(self.access_count, key=self.access_count.get)
            print(f"DISCARD: {least_used}")
            del self.cache_data[least_used]
            del self.access_count[least_used]
        self.cache_data[key] = item
        self.access_count[key] = 0
        return self.cache_data

    def get(self, key):
        """
        Gets data using key if it exists
        """
        if key is None:
            return
        try:
            self.access_count[key] += 1
            return self.cache_data[key]
        except KeyError:
            return None

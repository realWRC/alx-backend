#!/usr/bin/env python3
"""
Module for defining a cache eviction policy
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU eviction policy class implementation that inherits
    from BaseCaching
    """

    def __init__(self):
        """
        Initialises the class and its super class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns key-value/item pair to a self.cache_data
        """
        if key is None or item is None:
            return
        if self.cache_data.__len__() >= self.MAX_ITEMS:
            least_recent = list(self.cache_data)[0]
            print(f"DISCARD: {least_recent}")
            del self.cache_data[least_recent]
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """
        Gets data using key if it exists
        """
        if key is None:
            return
        try:
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
            return item
        except KeyError:
            return None

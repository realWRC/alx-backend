#!/usr/bin/env python3
"""
Module for defining a cache eviction policy
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO eviction policy class implementation that inherits
    from BaseCaching
    """

    def __init__(self):
        """
        Initialises the class and its super class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns key - value/item pair to a self.cache_data
        """
        if key is None or item is None:
            return
        if self.cache_data.__len__() == self.MAX_ITEMS:
            for first_key in self.cache_data.keys():
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
                break
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """
        Gets data using key if it exists
        """
        if key is None:
            return
        try:
            return self.cache_data[key]
        except KeyError:
            return None

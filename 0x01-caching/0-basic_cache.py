#!/usr/bin/env python3
"""
Module for caching classes
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching and is a
    caching system.
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
